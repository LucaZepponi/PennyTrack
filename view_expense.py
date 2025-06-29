import csv
from tkinter import *
from tkinter import messagebox, ttk

def view_expense(name: str, headers: list[str]) -> None:
  # Create a secondary window
  window = Toplevel()
  window.title("Tutte le spese")
  
  # Frame to control the table and scrollbar
  frame = Frame(window)
  frame.pack(expand=True, fill=BOTH)
  
  # Vertical scrollbar
  scrollbar = Scrollbar(frame)
  scrollbar.pack(side=RIGHT, fill=Y)
  
  # Table with specified columns
  table = ttk.Treeview(
    frame,
    columns=headers,
    show="headings",
    yscrollcommand=scrollbar.set)
  scrollbar.config(command=table.yview)
  
  # Configure Headers
  for column in headers:
    table.heading(column, text=column)
    table.column(column, width=100)
    
  # Load data from CSV file
  try:
    with open(name, mode="r", newline="", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      for row in reader:
        values = [row.get(col, "") for col in headers]
        table.insert("", END, values=values)
  except FileNotFoundError:
    messagebox.showerror("Errore", f"Il file '{name}' non è stato trovato.")
    window.destroy()
    return
  
  table.pack(expand=True, fill=BOTH)