#!/usr/bin/python3
import argparse
import json
from pathlib import Path

DATA_FILE = Path.home() / ".todo.json"

def load_tasks(): 					 #タスクを読み込むファイルを定義
    if not DATA_FILE.exists():
        return[]

    with open(DATA_FILE, "r", encoding = "utf-8") as f : #読み込んだファイルの文字コードをUTF-8にし、fとする
        return json.load(f)

def save_tasks(tasks):					 #タスクの保存を定義
    with open(DATA_FILE, "w", encoding = "utf-8") as f : #書き込みモード
        json.dump(tasks, f, ensure_ascii = False, indent = 4) #JSONファイルに書き込み

def add_task(args):					 #タスクの追加
    tasks = load_tasks()				 #保存されているTodoを読み込む
    new_id = max([task["id"] for task in tasks], default = 0) + 1 #タスクのリストの最大値を1追加する
    tasks.append({ "id" : new_id, "task" : args.task})   #リストの末尾にタスクを追加
    save_tasks(tasks)					 #追加したタスクをファイルに保存
    print(f"Taskk added: {args.task}")			 #id:Todoの番号 task:Todoの内容 args.task:コマンド入力で指定されたTodoの内容

def list_tasks(args):					 #Todoのリスト表示
    tasks = load_tasks()
    if not tasks:					 #リストがなかった場合
        print("No tasks.")
        return
    print("ID TASK")
    for task in tasks:
        print(f'{task["id"]}  {task["task"]}')

def done_task(args):					 #タスク完了
    tasks = load_tasks()
    for task in tasks:					 #指定されたidとタスクのidが一致してるか
        if task["id"] == args.id:
            tasks.remove(task)				 #一致したタスクの削除
            save_tasks(tasks)
            print(f'Task completed: {task["task"]}')
            return					 #指定されたタスクを消したら終了
    print("Task not found.")

def remove_task(args):					 #タスクの削除
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == args.id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f'Task removed: {task["task"]}')
            return
    print("Task not found.")

def main():
    parser = argparse.ArgumentParser(
        description = "A simple command-line Todo manager"
    )
    subparsers = parser.add_subparsers(
        dest = "command", required = True
    )

    add_parser = subparsers.add_parser("add")		 #addというコマンドを作る
    add_parser.add_argument("task")			 #taskという引数を受け取る
    add_parser.set_defaults(func=add_task)		 #addが選ばれたらadd_task関数を実行

    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=list_tasks)

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type = int)
    done_parser.set_defaults(func=done_task)

    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("id", type = int)
    remove_parser.set_defaults(func=remove_task)

    args = parser.parse_args()				 #入力されたコマンドを分析
    args.func(args)					 #選択された関数を実行

    if __name__ == "__main__":				 #このファイルを実行したときにmainを呼び出す
        main()
