#!/bin/bash
# SPDX-FileCopyrightText: 2026 Wataru Ono
# SPDX-License-Identifier: BSD-3-Clause

set -e

ng () {                               # 関数ngの定義（P18と同じ）
         echo ${1}行目のテスト失敗
         res=1                          # 失敗したことを記録
 }

res=0                                  # 0: 失敗なし（ngが呼ばれると1になる）

out=$(seq 5 | ./plus)                  # 表の1行目: plusの出力を変数outに記録
[ "${out}" = 15 ] || ng "$LINENO"      # 期待する出力（15）でなければngを呼び出す

[ "${res}" = 0 ] && echo OK            # 通ったのが（人間に）分かるように表示







# TODOのテスト
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

export HOME="$tmp"

# タスクを追加
python3 todo.py add "test task"

# 一覧に表示されるか
python3 todo.py list | grep -q "test task"

# タスクを完了する
python3 todo.py done 1

# 完了後に一覧が空になるか
python3 todo.py list | grep -q "No tasks."

# タスクの削除
python3 todo.py add "test task"
python3 todo.py remove 1
python3 todo.py list | grep -q "No tasks."

echo "TODO test passed"

exit $res
