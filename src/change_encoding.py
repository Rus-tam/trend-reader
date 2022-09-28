import io
import os
from os import listdir
import shutil

class EncodingChanger:
    def __init__(self):
        pass

    def ansi_to_utf8(self):
        src_path = os.getcwd()
        ansi_files = listdir(fr"{src_path}/trends/ansi_files")
        # Всяческие проверки
        if not os.path.isdir(f"{src_path}/trends/ansi_files"):
            os.mkdir(f"{src_path}/trends/ansi_files")
            print("Папка ansi_files создана. Необходимо добавить в нее файлы с трендами")
        if not os.path.isdir(f"{src_path}/trends/utf8_files"):
            os.mkdir(f"{src_path}/trends/utf8_files")
        if os.path.isdir(f"{src_path}/trends/ansi_files") and len(ansi_files) == 0:
            print("Нет исходных файлов в формате ANSI")

        # Меняем кодировку файла
        for file in ansi_files:
            print("+++++++++++++++++++++++++++++")
            print(f"Меняю кодировку файла {file}")
            print("+++++++++++++++++++++++++++++")
            print(" ")
            with io.open(f"{src_path}/trends/ansi_files/{file}", encoding="ANSI", errors="ignore") as source:
                with io.open(f"{src_path}/trends/utf8_files/{file}", mode="w", encoding="UTF-8") as target:
                    shutil.copyfileobj(source, target)