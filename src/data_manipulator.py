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

        print(transposed_values)
        print("========================")
        print(" ")

        return transposed_values


    def df_to_csv(self, data_frame):
        self.__make_normal_df(data_frame)




