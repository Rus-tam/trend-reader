import pandas as pd


class DataManipulator:
    def __init__(self):
        pass

    def make_normal_df(self, data_frame):
        sensor_names = data_frame.iloc[3][5:]
        sensor_assignment = data_frame.iloc[4][5:]
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
        transposed_values.insert(0, "Датчик", sensor_assignment, True)
        transposed_values.insert(1, "Имя датчика", sensor_names, True)
        transposed_values.insert(2, "Ед. измерения", sensor_units, True)

        return transposed_values

    def make_overall_df(self, src_path, processed_files):
        try:
            df_list = []
            for file in processed_files:
                df = pd.read_csv(rf"{src_path}/trends/processed_files/{file}", low_memory=False)
                df_list.append(df)
            overall_df = pd.concat(df_list)
            return overall_df
        except:
            print("Возникла какая-то ошибка!")

    def sort_by_department(self, overall_df):
        departments = []
        multiple_df = {}
        sensors = overall_df["Имя датчика"].tolist()
        all_sensors = [sensor for sensor in sensors if not pd.isna(sensor)]
        for sensor in all_sensors:
            if sensor[0:2] not in departments:
                departments.append(sensor[0:2])
        for department in departments:
            indexes = [i for i in range(0, len(all_sensors)) if all_sensors[i][0:2] == department]
            df = overall_df.iloc[indexes]
            multiple_df[department] = df

        return multiple_df

    def sort_by_time(self, data_frame):
        print("+++++++++++++++++++++++++")
        print("Начинаю сортировать дата фрейм по времени")
        print("+++++++++++++++++++++++++")
        data = {}
        selected_times = []
        selected_times.append(data_frame.columns[0])
        selected_times.append(data_frame.columns[1])
        selected_times.append(data_frame.columns[2])
        times = list(data_frame.columns)[3:]
        current_day = times[0].split(' ')[0]
        for time in times:
            day = time.split(' ')[0]
            if current_day != day:
                current_day = day
                selected_times = []
                selected_times.append(data_frame.columns[0])
                selected_times.append(data_frame.columns[1])
                selected_times.append(data_frame.columns[2])
            current_time = time.split(' ')[1]

            if current_time.split(':')[1][1] == '0':
                selected_times.append(current_day + ' ' + current_time)
            data[f"{current_day}"] = data_frame[selected_times]

        return data

    def sort_by_minutes(self, data_frame):
        print('+++++++++++++++++++++++++++++')
        print('Произвожу предварительную сортировку по времени')
        print('+++++++++++++++++++++++++++++')
        temp_arr = []
        selected_times = []
        selected_times.append(data_frame.columns[0])
        selected_times.append(data_frame.columns[1])
        selected_times.append(data_frame.columns[2])
        times = list(data_frame.columns)[3:]

        for time in times:
            if time.split(' ')[1].split(':')[1][1] == '0' and time[:len(time) - 3] not in temp_arr:
                selected_times.append(time)
                temp_arr.append(time[:len(time) - 3])

        return data_frame[selected_times]




