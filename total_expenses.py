import csv
from tkinter import *

def compute_total_expenses(reader: csv.DictReader) -> float:
  total_expenses = 0.0
  
  for row in reader:
    # In the first row of reader there are the headers
    try:
      total_expenses += float(row.get("Importo", 0))
    except ValueError:
      pass
  
  return total_expenses

def show_total_expenses(total_expenses: float) -> None:
  # Initialize the modal window
  modal = Toplevel()
  modal.title("Totale Spese")
  modal.resizable(False, False) # Prevents changing the window size

  Label(modal, text="Totale Spese", font=("Arial", 12)).pack(pady=10)
  Label(modal, text=f"Il totale dei soldi spesi è {total_expenses} €.", font=("Arial", 10)).pack(pady=10)
  
  modal.grab_set()    # Makes the window modal
  modal.transient()   # Keeps it in the foreground of the main window
  modal.wait_window() # Waits for the window to close
  

def total_expenses(name: str) -> None:
  with open(name, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    total_expenses = compute_total_expenses(reader)
  
  # Create a new window to display the total of expenses
  # TODO : Add some filter
  show_total_expenses(total_expenses)