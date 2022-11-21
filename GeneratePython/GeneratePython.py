#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pythonファイル生成プログラム：PythonプロジェクトもしくはPythonファイルを生成します。
"""

__author__ = 'Kobayashi Shun'
__version__ = '3.0.0'
__date__ = '2022/11/20 (Created: 2022/08/05)'

import sys
import os
from datetime import date
import subprocess


def header():
    """
    ヘッダー文字列（シェバン、マジックコメント、author、version、date）を応答します。
    """
    dt_today = str(date.today())
    date_info = dt_today[0:4] + '/' + dt_today[5:7] + '/' + dt_today[8:10]

    return f"""#!/usr/bin/env python
# -*- coding: utf-8 -*-

\"""
Python生成プログラム：Pythonファイルを生成します。
\"""

__author__ = 'Kobayashi Shun'
__version__ = '0.0.0'
__date__ = '{date_info} (Created: {date_info})'

import sys

"""

def gen_class(project_name) -> str:
    """
    クラスの情報を応答します。
    """
    return f"""
class {project_name}:
	\"""
	{project_name}クラスです。
	\"""

	def __init__(self):
		\"""
		インスタンスを生成します。
		\"""
"""

def footer():
    """
    フッター文字列を応答します。
    """

    return f"""
def main():
    \"""
    Pythonファイルを生成するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    \"""

if __name__ == '__main__':  # このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    sys.exit(main())
"""

def framework(project_name, project = True) -> str:
    """
    Pythonファイルの文字列を応答します。
    """
    if project:
        return header() + gen_class(project_name) + footer()
    else:
        return header() + footer()


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

    mode = input('Project mode? or Create file mode? (P/c): ')
    if ('c' in mode) or ('C' in mode):
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
            a_file.write(framework('', False))

        print('Finish generating ' + file_name + ' in ' + directory)

    else:
        project_name = input('Please enter the name of the project to be created: ')
        if project_name == '':
            project_name = 'Project'
        elif project_name[0].islower():
            project_name = project_name.capitalize()

        subprocess.run(['mkdir', project_name], check=True)
        subprocess.run(f"cp ~/programing_language/python/ProgrammingTool/GeneratePython/Makefile {project_name}", shell=True, check=True)
        subprocess.run(f"cp ~/programing_language/python/ProgrammingTool/GeneratePython/modified_pylintrc.txt {project_name}", shell=True, check=True)
        subprocess.run(f"mv {project_name}/modified_pylintrc.txt {project_name}/.pylintrc", shell=True, check=True)

        a_file = os.path.join(os.getcwd(), project_name, project_name + '.py')
        with open(a_file, 'w', encoding='utf-8') as a_file:
            a_file.write(framework(project_name, True))

        print()
        print(f'linting result (pylint {project_name}/{project_name}.py)')
        subprocess.run(f"pylint {project_name}/{project_name}.py", shell=True, check=True)

        print('Finish generating ' + project_name + ' in ' + os.getcwd())

if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    sys.exit(main())
