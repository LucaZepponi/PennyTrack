import csv
from datetime import datetime
from tkinter import *

def compute_total_expenses(reader: csv.DictReader, month: int = None, year: int = None, place: str = None) -> float:
  total_expenses = 0.0
  
  for row in reader:
    # In the first row of reader there are the headers
    try:
      # Extract and interpret the date
      date_str = row.get("Data di acquisto", "")
      date = datetime.strptime(date_str, "%Y-%m-%d")
      # The conversion from str to datetime is useful because then I can access month and year more easily
      
      # Filters
      if month is not None and date.month != month:
        continue
      if year is not None and date.year != year:
        continue
      if place and place.lower() not in row.get("Luogo di acquisto", "").lower():
        continue
      total_expenses += float(row.get("Importo", 0))
    except ValueError:
      # Ignore badly formatted lines
      pass
  print(total_expenses)
  return total_expenses

def show_total_expenses(reader: csv.DictReader, total_expenses: float) -> None:
  # Initialize the modal window
  modal = Toplevel()
  modal.title("Totale Spese")
  modal.resizable(False, False) # Prevents changing the window size

  Label(modal, text="Totale Spese", font=("Arial", 12)).grid(row=0, columnspan=2, pady=10)
  Label(modal, text=f"Il totale dei soldi spesi è {total_expenses} €.", font=("Arial", 10)).grid(row=1, column=0, columnspan=2, pady=10)
  
  Label(modal, text="Mese:").grid(row=2, column=0, sticky=E, pady=2)
  entry_month = Entry(modal)
  entry_month.grid(row=2, column=1, pady=2)
  Label(modal, text="Anno:").grid(row=3, column=0, sticky=E, pady=2)
  entry_year  = Entry(modal)
  entry_year.grid(row=3, column=1, pady=2)
  Label(modal, text="Luogo di acquisto:").grid(row=4, column=0, sticky=E, pady=2)
  entry_place = Entry(modal)
  entry_place.grid(row=4, column=1, pady=2)
  
  Button(modal, text="Applica filtri", command=lambda: compute_total_expenses(reader, entry_month.get(), entry_year.get(), entry_place.get())).grid(row=5, column=1, padx=5)
  
  
  modal.grab_set()    # Makes the window modal
  modal.transient()   # Keeps it in the foreground of the main window
  modal.wait_window() # Waits for the window to close
  

def total_expenses(name: str) -> None:
  with open(name, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    total_expenses = compute_total_expenses(reader)
  
    # Create a new window to display the total of expenses
    # TODO : Add some filter
    show_total_expenses(reader, total_expenses)