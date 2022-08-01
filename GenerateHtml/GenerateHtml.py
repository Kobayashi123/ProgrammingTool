#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HTML生成プログラム：HTMLを生成します。
"""

__author__ = 'Kobayashi Shun'
__version__ = '1.0.0'
__date__ = '2022/08/01 (Created: 2022/08/01)'

import os


def head_part():
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


def body_part():
    """
    HTMLのボディー部分の文字列を応答します。
    """
    return """    <body>
        ここに本文を入力してください。
    </body>"""


def foot_part():
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
    # home_directory = os.path.expanduser('~')
    # a_file = os.path.join(home_directory, 'Desktop', 'temp.html')
    current_directory = os.getcwd()
    file_name = input('作成するファイル名を入力してください: ')
    a_file = os.path.join(current_directory, file_name + '.html')
    with open(a_file, 'w', encoding='utf-8') as a_file:
        a_file.write(head_part())
        a_file.write(body_part())
        a_file.write(foot_part())


if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    # このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
