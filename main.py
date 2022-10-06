import pandas as pd

from src.files_handler import FilesHandler
from src.data_manipulator import DataManipulator
from src.writer import Writer

files_handler = FilesHandler()
files_handler.delete_files()
files_handler.ansi_to_utf8()

data_manipulator = DataManipulator()

for file in files_handler.ansi_files:
    saving_path = rf"{files_handler.src_path}\trends\processed_files\{file}"
    data = pd.read_csv(rf"{files_handler.src_path}\trends\utf8_files\{file}", low_memory=False)
    normal_df = data_manipulator.make_normal_df(data)
    sorted_by_minutes = data_manipulator.sort_by_minutes(normal_df)
    sorted_by_department = data_manipulator.sort_by_department(sorted_by_minutes)
    Writer.multiple_df_to_csv(sorted_by_department, files_handler.src_path)

for file in files_handler.sorted_by_department_files:
    file_xlsx = file.split('.')[0] + '.xlsx'
    saving_path = rf"{files_handler.src_path}\trends\{file_xlsx}"
    data = pd.read_csv(rf"{files_handler.src_path}\trends\sorted_by_department\{file}", low_memory=False)
    sorted_by_time = data_manipulator.sort_by_time(data)
    Writer.multiple_df_to_excel(sorted_by_time, saving_path)


