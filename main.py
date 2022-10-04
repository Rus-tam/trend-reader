import pandas as pd

from src.files_handler import FilesHandler
from src.data_manipulator import DataManipulator
from src.writer import Writer

files_handler = FilesHandler()
files_handler.ansi_to_utf8()

data_manipulator = DataManipulator()


for file in files_handler.ansi_files:
    saving_path = rf"{files_handler.src_path}\trends\processed_files\{file}"
    data = pd.read_csv(rf"{files_handler.src_path}\trends\utf8_files\{file}", low_memory=False)
    normal_df = data_manipulator.make_normal_df(data)
    Writer.df_to_csv(normal_df, saving_path)

overall_df = data_manipulator.make_overall_df(files_handler.src_path, files_handler.processed_files)
multiple_df = data_manipulator.sort_by_department(overall_df, files_handler.src_path)

Writer.multiple_df_to_csv(multiple_df, files_handler.src_path)

# Writer.df_to_csv(overall_df, rf'{files_handler.src_path}\trends\overall-file.csv')


