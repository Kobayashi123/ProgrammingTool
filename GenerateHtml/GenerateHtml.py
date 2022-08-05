#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HTML生成プログラム：HTMLを生成します。
"""

__author__ = 'Kobayashi Shun'
__version__ = '1.1.0'
__date__ = '2022/08/05 (Created: 2022/08/01)'

import os
import sys


def head_part() -> str:
    """
    HTMLのヘッダー部分の文字列を応答します。
    """

    return """<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta http-equiv="Content-Style-Type" content="text/css">
        <meta http-equiv="Content-Script-Type" content="text/javascript">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="keywords" content="Program, Security, Kobayashi Shun, Shun">
        <meta name="description" content="HTML生成">
        <meta name="author" content="Kobayashi Shun">
        <link rev="made" href="mailto:shun123k@gmail.com">
        <link rel="index" href="index-j.html">
        <style type="text/css">
        </style>
        <title>自動生成したHTMLです。</title>
    </head>
"""


def body_part() -> str:
    """
    HTMLのボディー部分の文字列を応答します。
    """
    return """    <body>
        <header>
            <h1><a href="index.html"></a></h1>
        </header>

            ここに本文を入力してください。

        <footer>
            <p><small>&copy; All rights reserved by shun.</small></p>
        </footer>
    </body>"""


def foot_part() -> str:
    """
    HTMLのフッター部分の文字列を応答します。
    """

    return """
</html>
"""


def main():
    """
    HTMLファイルを生成するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """
    num_args = len(sys.argv)

    if num_args == 1:
        file_name = input('作成するファイル名を入力してください: ')
    else:
        file_name = sys.argv[1]

    if '.html' not in file_name:
        file_name = file_name + '.html'

    current_directory = os.getcwd()
    a_file = os.path.join(current_directory, file_name)
    with open(a_file, 'w', encoding='utf-8') as write_file:
        write_file.write(head_part())
        write_file.write(body_part())
        write_file.write(foot_part())

    print('Generate ', file_name)


if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    # import sys

    if len(sys.argv) > 2:
        print("The use of the command is wrong.")
        sys.exit(1)

    # このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
