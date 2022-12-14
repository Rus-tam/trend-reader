import io
import os
from os import listdir
import shutil


class FilesHandler:
    def __init__(self):
        self.src_path = os.getcwd()
        if not os.path.isdir(f"{self.src_path}/trends/ansi_files"):
            os.mkdir(f"{self.src_path}/trends/ansi_files")
            print("Папка ansi_files создана. Необходимо добавить в нее файлы с трендами")
        if not os.path.isdir(f"{self.src_path}/trends/utf8_files"):
            os.mkdir(f"{self.src_path}/trends/utf8_files")
        self.ansi_files = listdir(fr"{self.src_path}/trends/ansi_files")
        self.processed_files = listdir(fr"{self.src_path}/trends/processed_files")
        self.utf8_files = listdir(fr"{self.src_path}/trends/utf8_files")
        if os.path.isdir(f"{self.src_path}/trends/ansi_files") and len(self.ansi_files) == 0:
            print("Нет исходных файлов в формате ANSI")
        if not os.path.isdir(f"{self.src_path}/trends/processed_files"):
            os.mkdir(f"{self.src_path}/trends/processed_files")
            print("Папка processed_files создана.")
        if not os.path.isdir(f"{self.src_path}/trends/sorted_by_department"):
            os.mkdir(f"{self.src_path}/trends/sorted_by_department")
            print("Создана папка sorted_by_department")
        self.sorted_by_department_files = listdir(fr"{self.src_path}/trends/sorted_by_department")

    def ansi_to_utf8(self):
        # Меняем кодировку файла
        for file in self.ansi_files:
            print("+++++++++++++++++++++++++++++")
            print(f"Меняю кодировку файла {file}")
            print("+++++++++++++++++++++++++++++")
            print(" ")
            with io.open(f"{self.src_path}/trends/ansi_files/{file}", encoding="ANSI", errors="ignore") as source:
                with io.open(f"{self.src_path}/trends/utf8_files/{file}", mode="w", encoding="UTF-8") as target:
                    shutil.copyfileobj(source, target)

    def delete_files(self):
        # Удаляем файлы в папках processed_files, sorted_by_department, utf8_files
        for file in self.processed_files:
            os.remove(rf"{self.src_path}/trends/processed_files/{file}")
        for file in self.sorted_by_department_files:
            os.remove(rf"{self.src_path}/trends/sorted_by_department/{file}")
        for file in self.utf8_files:
            os.remove(rf"{self.src_path}/trends/utf8_files/{file}")
