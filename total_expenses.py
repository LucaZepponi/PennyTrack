import csv
from datetime import datetime
from tkinter import *
from tkinter import messagebox

from read_csv_rows import read_csv_rows

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
      if place and place.lower() not in row.get("Luogo di acquisto", "").strip().lower():
        continue
      
      total_expenses += float(row.get("Importo", 0))
    except ValueError:
      messagebox.showerror("Errore", "Non è stato possibile calcolare il totale")
      continue
    
  return total_expenses

def show_total_expenses(name: str) -> None:
  rows = read_csv_rows(name)
  total = compute_total_expenses(rows)
  
  # Initialize the modal window
  modal = Toplevel()
  modal.title("Totale Spese")
  modal.resizable(False, False) # Prevents changing the window size

  Label(modal, text="Totale Spese", font=("Arial", 12)).grid(row=0, columnspan=2, pady=10)
  label_result = Label(modal, text=f"Il totale dei soldi spesi è {total:.2f} €.", font=("Arial", 10))
  label_result.grid(row=1, column=0, columnspan=2, pady=10)
  
  # Month filter
  Label(modal, text="Mese:").grid(row=2, column=0, sticky=E, pady=2)
  entry_month = Entry(modal)
  entry_month.grid(row=2, column=1, pady=2)
  
  # Year filter
  Label(modal, text="Anno:").grid(row=3, column=0, sticky=E, pady=2)
  entry_year  = Entry(modal)
  entry_year.grid(row=3, column=1, pady=2)
  
  # Place filter
  Label(modal, text="Luogo di acquisto:").grid(row=4, column=0, sticky=E, pady=2)
  entry_place = Entry(modal)
  entry_place.grid(row=4, column=1, pady=2)
  
  def apply_filters():
    try:
      month = int(entry_month.get()) if entry_month.get().strip() else None
    except ValueError:
      month = None
      
    try:
      year = int(entry_year.get()) if entry_year.get().strip() else None
    except ValueError:
      year = None
    
    place = entry_place.get().strip()
    if place == "":
      place = None
      
    filtered_total = compute_total_expenses(rows, month, year, place)
    label_result.config(text=f"Il totale dei soldi spesi è {filtered_total:.2f} €.")
  
  Button(modal, text="Applica filtri", command=lambda: apply_filters()).grid(row=5, column=1, padx=5)
  
  
  modal.grab_set()    # Makes the window modal
  modal.transient()   # Keeps it in the foreground of the main window
  modal.wait_window() # Waits for the window to close
  

def total_expenses(name: str) -> None:
  show_total_expenses(name)