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
    sorted_by_department = data_manipulator.sort_by_department(normal_df)
    Writer.multiple_df_to_csv(sorted_by_department, files_handler.src_path)

for file in files_handler.sorted_by_department_files:
    file_xlsx = file.split('.')[0] + '.xlsx'
    saving_path = rf"{files_handler.src_path}\trends\{file_xlsx}"
    data = pd.read_csv(rf"{files_handler.src_path}\trends\sorted_by_department\{file}", low_memory=False)
    sorted_by_time = data_manipulator.sort_by_time(data)
    Writer.multiple_df_to_excel(sorted_by_time, saving_path)



# overall_df = data_manipulator.make_overall_df(files_handler.src_path, files_handler.processed_files)
# multiple_df = data_manipulator.sort_by_department(overall_df)
#
# Writer.multiple_df_to_csv(multiple_df, files_handler.src_path)
#
# sorted_files = files_handler.sorted_by_department_files
#
# for file in sorted_files:
#     data = pd.read_csv(rf"{files_handler.src_path}\trends\sorted_by_department\{file}")
#     sorted_by_time_data = data_manipulator.sort_by_time(data)
#     file_xlsx = file.split('.')[0] + '.xlsx'
#     Writer.multiple_df_to_excel(sorted_by_time_data, rf"{files_handler.src_path}\trends\{file_xlsx}")

# Writer.df_to_csv(overall_df, rf'{files_handler.src_path}\trends\overall-file.csv')


