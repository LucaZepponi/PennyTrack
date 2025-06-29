import csv
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import Calendar

def save_expense(name: str, place: str, date: str, expence_amount: str, iva: str, category: str, payment_method: str, notes: str, window: Toplevel) -> None:
  # Control of expence_amount and vat values
  try:
    # The input `expence_amount` and `iva` are strings, but I need floats
    expence_amount = float(expence_amount)
    iva = float(iva)
  except ValueError:
    messagebox.showerror("Errore", "Importo e IVA devono essere numerici.")
    return
  
  with open(name, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    id_expense = sum(1 for _ in open(name)) # Counts the existing rows
    
    # Compiling dataset fields
    writer.writerow([
      id_expense,
      place,
      date,
      "{:.2f}".format(float(expence_amount)),
      "{:.2f}".format(float(iva)),
      category,
      payment_method,
      notes
    ])
    
    window.destroy()
    messagebox.showinfo("Successo", "Spesa aggiunta correttamente")

def confirm_date(cal: Calendar, entry_date: Entry, cal_wind: Toplevel) -> None:
  selected = cal.get_date()
  # Per poter modificare la data, il campo entry_date deve tornare normale
  entry_date.config(state="normal")
  entry_date.delete(0, END)
  entry_date.insert(0, selected)
  entry_date.config(state="readonly")
  cal_wind.destroy()

def open_calendar(entry_date: Entry) -> None:
  # Window initializzation
  cal_wind = Toplevel()
  cal_wind.title("Seleziona una data")
  # I make the cal_wind window 'child' of the 'main' window
  cal_wind.transient(entry_date.master)
  # Making the child window modal to the main window
  cal_wind.grab_set()
  
  # Calendar
  cal = Calendar(cal_wind, selectmode="day", year = 2025, month=6, day=28, date_pattern="yyyy-mm-dd")
  cal.pack(pady=20)
  
  # Confirm button
  # The syntax `command=confirm_date(...)` immediately executes the function instead of passing it as a reference: a lambda function must be used
  Button(cal_wind, text="Conferma", command= lambda: confirm_date(cal, entry_date, cal_wind)).pack(pady=5)
  
  cal_wind.wait_window() # Waiting for the calendar to close
  

def add_expense(name: str) -> None:
  window = Toplevel()
  window.title("Aggiungi spesa")
  
  # Labels
  Label(window, text="Luogo di acquisto").grid(row=0, column=0, sticky=W)
  Label(window, text="Data (YYYY-MM-DD)").grid(row=1, column=0, sticky=W)
  Label(window, text="Importo (€)").grid(row=2, column=0, sticky=W)
  Label(window, text="IVA (€)").grid(row=3, column=0, sticky=W)
  Label(window, text="Categoria").grid(row=4, column=0, sticky=W)
  Label(window, text="Metodo di pagamento").grid(row=5, column=0, sticky=W)
  Label(window, text="Note").grid(row=6, column=0, sticky=W)
  
  # Entry fields
  entry_field_width = 23
  entry_place = Entry(window, width=entry_field_width)     # CSV file name
  entry_date = Entry(window, width=entry_field_width)      # Place of purchase
  entry_import = Entry(window, width=entry_field_width)    # Amount spent (entered as string and then converted to float)
  entry_iva = Entry(window, width=entry_field_width)       # IVA value (entered as string and then converted to float)
  entry_notes = Entry(window, width=entry_field_width)     # Optional notes
  
  # Compobox for cathegory
  combo_width = entry_field_width - 3 # the arrow occupies a space of width = 3
  combo_category = ttk.Combobox(window, state="readonly", width=combo_width)
  combo_category["values"] = ["Alimentari", "Trasporti", "Bollette", "Tempo libero", "Cartoleria", "Altro"]
  combo_category.set("Alimentari")
  
  # Compobox for payment method
  combo_pay_meth = ttk.Combobox(window, state="readonly", width=combo_width)
  combo_pay_meth["values"] = ["Contanti", "Carta di credito", "Bancomat", "Bonifico", "Prepagata", "Altro"]
  combo_pay_meth.set("Contanti")
  
  # Insert current date
  entry_date.insert(0, datetime.today().strftime("%Y-%m-%d"))
  # I change the status of the field to enter the date as "readonly" so that one cannot edit that field without going through the calendar button
  entry_date.config(state="readonly")
  
  # Entry fields grid
  entry_place.grid(row=0, column=1, pady=2)
  entry_date.grid(row=1, column=1, pady=2)
  entry_import.grid(row=2, column=1, pady=2)
  entry_iva.grid(row=3, column=1, pady=2)
  combo_category.grid(row=4, column=1, pady=2)
  combo_pay_meth.grid(row=5, column=1, pady=2)
  entry_notes.grid(row=6, column=1, pady=2)
  
  # Calendar Button
  Button(window, text="🗓️", command=lambda: open_calendar(entry_date)).grid(row=1, column=2, padx=5)
  # Save Button
  Button(
    window, text="Salva",
    command=lambda: save_expense(
      name,
      entry_place.get(),    # 
      entry_date.get(),
      entry_import.get(),
      entry_iva.get(),
      combo_category.get(),
      combo_pay_meth.get(),
      entry_notes.get(),
      window
    )
  ).grid(row=7, column=0, columnspan=2, pady=10)
  
  # Makes the window modal: you cannot interact with other functions as long as this one remains open
  window.grab_set()