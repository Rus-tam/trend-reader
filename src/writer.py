import pandas as pd


class Writer:
    def __init__(self):
        pass

    @staticmethod
    def df_to_csv(normal_df, path):
        # path - путь сохранения файла (в этот путь уже должно быть добавлено наименование файла)
        file_name = path.split("\\")[-1]
        print("++++++++++++++++++++++++++")
        print(f'Сохраняю файл {file_name}')
        print("++++++++++++++++++++++++++")
        print(" ")
        normal_df.to_csv(path)

    def df_to_excel(self, data_frame, path):
        pass