import tkinter as tk
from pathlib import Path
from tkinter import filedialog

import pandas as pd
import pyreadstat
import typer
from typing_extensions import Annotated

app = typer.Typer()

@app.command()
def transform_sav_to_excel(
        input_sav_file: Annotated[Path, typer.Argument()] = None, 
        output_xlsx_file: Annotated[Path, typer.Argument()] = None):
    """
    Transforms the given .sav file to a .xlsx file, preserving the .sav metadata
    """
    
    if not input_sav_file:
        root = tk.Tk()
        root.withdraw()
        input_sav_file = Path(filedialog.askopenfilename(filetypes=[("SPSS Files",".sav")], initialdir=Path.cwd()))
    
    df, meta = pyreadstat.read_sav(input_sav_file)
    
    meta_df_data = []
    for variable_name, variable_values_and_labels in meta.variable_value_labels.items():
        for variable_value, variable_label in variable_values_and_labels.items():
            meta_df_data.append([variable_name, variable_value, variable_label])
    meta_df = pd.DataFrame(data=meta_df_data, columns=["Variable name","Variable value","Variable label"])
    
    if not output_xlsx_file:
        output_xlsx_file = input_sav_file.with_suffix(".xlsx")
    
    with pd.ExcelWriter(output_xlsx_file) as writer:
        df.to_excel(writer, sheet_name="data", index=False)
        meta_df.to_excel(writer, sheet_name="meta", index=False)
    
if __name__ == '__main__':
    transform_sav_to_excel()