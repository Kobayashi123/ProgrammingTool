#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python生成プログラム：Pythonファイルを生成します。
"""

__author__ = 'Kobayashi Shun'
__version__ = '2.0.0'
__date__ = '2022/09/10 (Created: 2022/08/05)'

import sys
import os
from datetime import date
import subprocess


def framework() -> str:
    """
    Pythonの シェバン、マジックコメント、author、version、date の文字列を応答します。
    """

    dt_today = date.today()
    dt_today = str(dt_today)
    date_info = dt_today[0:4] + '/' + dt_today[5:7] + '/' + dt_today[8:10]
    print(date_info)

    return f"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

\"""
Python生成プログラム：Pythonファイルを生成します。
\"""

__author__ = 'Kobayashi Shun'
__version__ = '0.0.0'
__date__ = '{date_info} (Created: {date_info})'

def main():
    \"""
    Pythonファイルを生成するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    \"""


if __name__ == '__main__':  # このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    sys.exit(main())
"""

def command_check() -> int:
    """
    コマンドのチェックを行います。
    コマンドの長さが 1 または 2 以外のとき、プログラムを終了します。
    """
    num_args = len(sys.argv)

    if len(sys.argv) != 1 and len(sys.argv) != 2:
        print("The use of the command is wrong.")
        sys.exit(1)

    return num_args

def make_file_name(num_args) -> str:
    """
    pythonファイルの名前を決めるプログラムです。
    作成するPythonファイルの名前を返します。
    """
    if num_args == 1:
        file_name = input('Please enter the name of the file to be created: ')
    else:
        file_name = sys.argv[1]

    if '.py' not in file_name:
        file_name = file_name + '.py'

    return file_name

def main():
    """
    Pythonファイルを生成するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """

    num_args = command_check()

    file_name = make_file_name(num_args)

    choice_directory = input('Generate python file in current_directory or optional_directory? [C/o] : ')
    if choice_directory != 'o':
        current_directory = os.getcwd()
        directory = current_directory
    else:
        directory = input('What directory name in absolute path?: ')

    a_file = os.path.join(directory, file_name)
    with open(a_file, 'w', encoding='utf-8') as a_file:
        a_file.write(framework())

    print('Finish generating ' + file_name + ' in ' + directory)

    subprocess.run("pylint modified_pylintrc.txt", shell=True)

if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    # このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
