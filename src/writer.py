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

    @staticmethod
    def multiple_df_to_csv(multiple_df, src_path):
        # path - путь сохранения файла в котором НЕ прописанно наименование файла
        file_names = list(multiple_df.keys())

        for name in file_names:
            print("+++++++++++++++++++++++")
            print(f"Сохраняю файл 'отделение-{name}'")
            print("+++++++++++++++++++++++")
            multiple_df[name].to_csv(rf"{src_path}/trends/sorted_by_department/отделение-{name}")


    def df_to_excel(self, data_frame, path):
        pass