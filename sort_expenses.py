import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def sort_expenses(name:str, column_to_sort: str, descending: bool = False, date_format: str = "%Y-%m-%d") -> list[dict[str, any]]:
  # CSV file reading
  with open(name, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
  
  # If the file is empty, it returns
  if not rows or column_to_sort not in rows[0]:
    messagebox.showinfo("Dataset vuoto", "Nessuna voce presente nel dataset")
    return
  
  # If the column is absent, it returns
  if column_to_sort not in rows[0]:
    messagebox.showinfo("Informazione mancante", "La colonna inserita non è presente come voce nel dataset")
    return
  
  # Prova ad ordinare per data
  try:
    rows.sort(
      key=lambda row: datetime.strptime(row[column_to_sort], date_format),
      reverse=descending
    )
  except (ValueError, KeyError) as e:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Errore di ordinamento", f"Impossibile ordinare per la colonna '{column_to_sort}':\n{e}")  
  return rows

# TODO : Generalise the function to order with other filters as well