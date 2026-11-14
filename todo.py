#!/usr/bin/python3

import argparse
import json
from pathlib import Path

DATA_FILE = Path.home() / ".todo.json"


def load_tasks():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


def add_task(args):
    tasks = load_tasks()

    new_id = max([task["id"] for task in tasks], default=0) + 1

    tasks.append({
        "id": new_id,
        "task": args.task
    })

    save_tasks(tasks)
    print(f"Task added: {args.task}")


def list_tasks(args):
    tasks = load_tasks()

    if not tasks:
        print("No tasks.")
        return

    print("ID  TASK")
    for task in tasks:
        print(f'{task["id"]}   {task["task"]}')


def done_task(args):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == args.id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f'Task completed: {task["task"]}')
            return

    print("Task not found.")


def remove_task(args):
    tasks = load_tasks()

    new_tasks = [task for task in tasks if task["id"] != args.id]

    if len(tasks) == len(new_tasks):
        print("Task not found.")
        return

    save_tasks(new_tasks)
    print("Task removed.")


def count_tasks(args):
    tasks = load_tasks()
    print(f"Remaining tasks: {len(tasks)}")


def main():
    parser = argparse.ArgumentParser(
        description="A simple command-line TODO manager"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("task")
    add_parser.set_defaults(func=add_task)

    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=list_tasks)

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)
    done_parser.set_defaults(func=done_task)

    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("id", type=int)
    remove_parser.set_defaults(func=remove_task)

    count_parser = subparsers.add_parser("count")
    count_parser.set_defaults(func=count_tasks)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
