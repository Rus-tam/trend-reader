import pandas as pd

from src.files_handler import FilesHandler
from src.data_manipulator import DataManipulator

files_handler = FilesHandler()
files_handler.ansi_to_utf8()

data_manipulator = DataManipulator()


for file in files_handler.ansi_files:
    saving_path = rf"{files_handler.src_path}\trends\processed_files\{file}"
    data = pd.read_csv(rf"{files_handler.src_path}\trends\utf8_files\{file}", low_memory=False)
    data_manipulator.df_to_csv(data, saving_path)

data_manipulator.make_overall_csv(files_handler.src_path, files_handler.processed_files)

df = pd.read_csv(rf"{files_handler.src_path}/trends/overall-file.csv", low_memory=False)
print(df.head(5))

# data = data_manipulator.make_overall_csv(files_handler.src_path, files_handler.processed_files)
#
# data_manipulator.clean_df(data)

