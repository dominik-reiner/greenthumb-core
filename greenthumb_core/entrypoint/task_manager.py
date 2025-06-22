import importlib
import pkgutil
import inspect
import json
import os
import time
import threading
from greenthumb_core.core import task as task_pkg
from greenthumb_core.domains.i_task import I_Task
from greenthumb_core.config import DATA_DIR


class TaskManager:
    def __init__(self, poll_interval=5):
        self.poll_interval = poll_interval
        # Load task arguments from a flat file (JSON)
        args_file = os.path.join(DATA_DIR, "task_args.json")
        if os.path.exists(args_file):
            with open(args_file, "r") as f:
                self.task_args = json.load(f)
        else:
            print(f"Warning: {args_file} not found. Using empty task_args.")
            self.task_args = {}
        self._stop_event = threading.Event()
        self._threads = []
        self._instances = []

    def _task_loop(self, instance):
        while not self._stop_event.is_set():
            try:
                instance.run()
            except Exception as e:
                print(f"Exception in {instance.__class__.__name__}: {e}")
            time.sleep(self.poll_interval)

    def run_all_tasks(self) -> None:
        """
        Discover all modules in the greenthumb_core.core.task subpackage,
        instantiate and run only classes that are subclasses of I_Task
        and have an entry in the task_args config, then call cleanup.
        Uses arguments from task_args.json.
        Spawns a thread for each task and repeatedly calls run().
        """
        for finder, name, ispkg in pkgutil.iter_modules(task_pkg.__path__):
            module_name = f"greenthumb_core.core.task.{name}"
            module = importlib.import_module(module_name)
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, I_Task) and obj is not I_Task and obj.__name__ in self.task_args:
                    args = self.task_args.get(obj.__name__, {})
                    try:
                        instance = obj(**args)
                        self._instances.append(instance)
                        t = threading.Thread(target=self._task_loop, args=(instance,), daemon=True)
                        t.start()
                        self._threads.append(t)
                        print(f"Started thread for {obj.__name__} from {module_name}")
                    except Exception as e:
                        print(f"Error running {obj.__name__} from {module_name}: {e}")
        print("All task threads started. Main process will wait for threads to finish.")
        if not self._threads:
            print("No tasks to run. Exiting.")
            return
        try:
            for t in self._threads:
                t.join()
        except KeyboardInterrupt:
            print("Shutting down tasks...")
            self._stop_event.set()
            for t in self._threads:
                t.join()
            for instance in self._instances:
                if hasattr(instance, "cleanup"):
                    instance.cleanup()
            print("Shutdown complete.")


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run_all_tasks()
