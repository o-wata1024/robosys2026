# robosys2026
 このリポジトリはロボットシステム学の授業で利用するリポジトリです。

## 著作権とLICENSE
 このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
 このパッケージのコードは、下記のスライド（CC BY-SA 4.0 by Taro Suzuki）のものを、
 本人の許可を得て自身の著作としたものです。
    https://github.com/tarolab-cit/lectures/tree/main/robosys2026
 © 2026 Wataru Ono

# Todo Manager

 ![test](https://github.com/o-wata1024/robosys2026/actions/workflows/test.yml/badge.svg)

## 概要

 Todo Managerは、ターミナル上でタスクを登録・管理するためのコマンドライン型Todo管理プログラムです。
 
 タスクの追加、一覧表示、完了、削除などを簡単に行うことができます。
 登録したタスクはJSONファイルに保存されるため、プログラムを終了してもデータが保持されます。

## インストール方法

 以下のコマンドでリポジトリを取得してください。

 $ git clone https://github.com/o-wata1024/robosys2026.git

 $ cd robosys2026

 以下のコマンドでPython3がインストールされていることを確認してください。

 $ python3 --version

 本プログラムPython3の標準ライブラリを使用しているため、追加のライブラリをインストールする必要はありません。

## 使用方法

### タスクの追加

 $ python3 todo.py add "task"

 出力例: Task added: task

### タスク一覧の表示

 $ python3 todo.py list

 出力例:ID  TASK

1  task

### タスクの完了

 $ python3 todo.py done 1 (リスト内で表示された数字で)

 出力例:Task completed: task

### タスクの削除

 $ python3 todo.py remove 1

 出力例:Task removed: task

### データの保存

 タスクはホームディレクトリにある~/.todo.jsonに保存されます。

## 使用技術

 ・Python3
 ・argparse
 ・json
 ・pathlib

## ライセンス

 このソフトウェアパッケージは、3条項BSDライセンスの下で公開されています。
 詳細については、リポジトリ内のLICENSEファイルを参照してください。
