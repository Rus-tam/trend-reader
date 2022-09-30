import pandas as pd

from src.change_encoding import EncodingChanger
from src.data_manipulator import DataManipulator

encoding_changer = EncodingChanger()
encoding_changer.ansi_to_utf8()

data_manipulator = DataManipulator()


for file in encoding_changer.ansi_files:
    data = pd.read_csv(rf"{encoding_changer.src_path}\trends\utf8_files\{file}", low_memory=False)
    data_manipulator.df_to_csv(data)


