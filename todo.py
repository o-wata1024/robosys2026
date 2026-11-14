#!/usr/bin/python3
import argparse
import json
from pathlib import Path

DATA_FILE = Path.home() / ".todo.json"

def load_task(): 					 #タスクを読み込むファイルを定義
    if not DATA_FILE.exists()
        return[]

    with open(DATA_FILE, "r", encoding = "utf-8") as f : #読み込んだファイルの文字コードをUTF-8にし、fとする
        return json.load(f)

def save_task(task):					 #タスクの保存を定義
    with open(DATA_FILE, "w", encoding = "utf-8") as f : #
        json.dump(task, f, ensure_ascii = False, indent = 4)
