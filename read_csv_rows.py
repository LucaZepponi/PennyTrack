import csv
from tkinter import messagebox
def read_csv_rows(filename: str) -> list[str]:
  try:
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      return list(reader)
  except FileNotFoundError:
    messagebox.showerror("Errore", "Il file '{filename}' non è stato trovato.")
    return[]
      