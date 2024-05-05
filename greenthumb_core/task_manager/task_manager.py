import importlib


class TaskManager:
    def __init__(self, task_definitions):
        self.task_definitions = task_definitions

    def execute_task(self, task_name):
        task_def = self.task_definitions[task_name]
        components = []
        for component_name in task_def['components']:
            component_module = importlib.import_module(component_name)
            components.append(component_module)
        task_module = importlib.import_module(task_def['python_module'])
        task = task_module.Task(*components)
        task.execute()

    def list_tasks(self):
        for task_name in self.task_definitions:
            print(f"  {task_name}")