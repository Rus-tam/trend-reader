import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment, Font


class DataManipulator:
    def __init__(self):
        pass

    def __make_normal_df(self, data_frame):
        sensor_names = data_frame.iloc[3][5:]
        sensor_assigment = data_frame.iloc[4][5:]
        sensor_units = data_frame.iloc[8][5:]

        # Таблица с временем и показаниями датчиков
        deleting_rows = []
        for i in range(0, 12):
            deleting_rows.append(i)
        time_data = data_frame.drop(deleting_rows, axis=0)

        # Получаем значения времени и даты
        time = time_data.iloc[:, 2] + " " + time_data.iloc[:, 3]
        values = time_data.iloc[:, 5:]

        # Вертим таблицу и добавляем столбцы
        transposed_values = values.transpose()
        transposed_values.columns = time
        transposed_values.insert(0, "Датчик", sensor_assigment, True)
        transposed_values.insert(1, "Имя датчика", sensor_names, True)
        transposed_values.insert(2, "Ед. измерения", sensor_units, True)

        transposed_values.drop(transposed_values.columns[0], axis=1, inplace=True)
        return transposed_values

    def df_to_csv(self, data_frame, path):
        # path - путь сохранения файла (в этот путь уже должно быть добавлено наименование файла)
        file_name = path.split("\\")[-1]
        normal_df = self.__make_normal_df(data_frame)
        print("++++++++++++++++++++++++++")
        print(f'Сохраняю нормализованный файл {file_name}')
        print("++++++++++++++++++++++++++")
        print(" ")
        normal_df.to_csv(path)

    def make_overall_csv(self, src_path, processed_files):
        try:
            df_list = []
            for file in processed_files:
                df = pd.read_csv(rf"{src_path}/trends/processed_files/{file}", low_memory=False)
                df_list.append(df)
            overall_df = pd.concat(df_list)
            # Очищаем датафрейм
            cleaned_overall_df = self.clean_df(overall_df)
            print("++++++++++++++++++++++++")
            print("Сохраняю файл с обобщенными данными overall-file.csv")
            print("++++++++++++++++++++++++")
            print(" ")
            print(cleaned_overall_df)
            cleaned_overall_df.to_csv(rf"{src_path}/trends/overall-file.csv")
        except:
            print("Возникла какая-то ошибка!")

    def clean_df(self, df):
        columns = df.columns
        trash_indexes = []
        i = 0
        while columns[i] != 'Имя датчика':
            trash_indexes.append(i)
            i += 1
        new_df = df.drop(df.columns[trash_indexes], axis=1)
        new_df = new_df.reset_index(drop=True)

        return new_df
