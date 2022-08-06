#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Python生成プログラム：Pythonファイルを生成します。
"""

__author__ = 'Kobayashi Shun'
__version__ = '1.0.0'
__date__ = '2022/08/05 (Created: 2022/08/05)'

import os


def flamework() -> str:
    """
    Pythonの シェバン、マジックコメント、author、version、date の文字列を応答します。
    """
    return """
#!/usr/bin/env python
# -*- coding: utf-8 -*-

\"""
Python生成プログラム：Pythonファイルを生成します。
\"""

__author__ = 'Kobayashi Shun'
__version__ = '1.0.0'
__date__ = '2022/08/05 (Created: 2022/08/05)'

def main():
    \"""
    Pythonファイルを生成するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    \"""


if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    # このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
"""


def main():
    """
    Pythonファイルを生成するメイン（main）プログラムです。
    常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
    """
    num_args = len(sys.argv)

    if num_args == 1:
        file_name = input('作成するファイル名を入力してください: ')
    else:
        file_name = sys.argv[1]

    if '.py' not in file_name:
        file_name = file_name + '.py'

    current_directory = os.getcwd()
    a_file = os.path.join(current_directory, file_name)
    with open(a_file, 'w', encoding='utf-8') as a_file:
        a_file.write(flamework())

    print('Generate ', file_name)


if __name__ == '__main__':  # ifによって、このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
    import sys
    if len(sys.argv) > 2:
        print("The use of the command is wrong.")
        sys.exit(1)
    # このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
    sys.exit(main())
