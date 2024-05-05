import argparse
import os
import yaml


def list_tasks(tasks_dir):
    print("Tasks:")
    for task_file in os.listdir(tasks_dir):
        if task_file.endswith(".yaml"):
            task_name = os.path.splitext(task_file)[0]
            print(f"  {task_name}")


def list_components(components_dir):
    print("Components:")
    for component_file in os.listdir(components_dir):
        if component_file.endswith(".yaml"):
            component_name = os.path.splitext(component_file)[0]
            print(f"  {component_name}")


def run_task(tasks_dir, task_name):
    task_file = os.path.join(tasks_dir, f"{task_name}.yaml")
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            task_def = yaml.safe_load(f)
        # Execute the task here
        print(f"Running task: {task_name}")
    else:
        print(f"Task not found: {task_name}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tasks-dir", help="Directory containing task definitions")
    parser.add_argument("--components-dir", help="Directory containing component definitions")
    subparsers = parser.add_subparsers(dest="command")

    list_tasks_parser = subparsers.add_parser("list-tasks", help="List all tasks")
    list_components_parser = subparsers.add_parser("list-components", help="List all components")
    run_task_parser = subparsers.add_parser("run-task", help="Run a task")
    run_task_parser.add_argument("task_name", help="Name of the task to run")

    args = parser.parse_args()

    if args.command == "list-tasks":
        list_tasks(args.tasks_dir)
    elif args.command == "list-components":
        list_components(args.components_dir)
    elif args.command == "run-task":
        run_task(args.tasks_dir, args.task_name)


if __name__ == "__main__":
    main()
