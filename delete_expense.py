import csv
# import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog

def delete_expense(name: str, headers: list[str], ID_column: str = "ID") -> None:
  # # Create an hide window for selecting ID_todelete
  # root = Tk()
  # root.withdraw() # It hides the windos
  
  # Dummy modal window to act as a container
  modal = Toplevel()
  modal.withdraw() # Does not show window
  modal.grab_set() # Modal rendering
  
  # Show the window for the ID entry
  ID_to_delete = simpledialog.askstring("Elimina spesa", "Inserisci l'ID da eliminare:")
  
  if not ID_to_delete: # The user cancelled the input
    messagebox.showinfo("Operazione annullata", "Nessun ID inserito: nessuna modifica effettuata")
    return
  
  # Read the file content
  with open(name, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader).copy()
  file.close()
  
  # filter the rows to write
  new_rows = [row for row in rows if row.get(ID_column) != ID_to_delete]
  
  # If no line has been selected, it signals and ends
  if len(new_rows) == len(rows):
    messagebox.showinfo("Nessuna corrispondenza", f"Nessuna riga con ID '{ID_to_delete}' trovata.")
    return
  
  # Write only filtered lines
  with open(name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(new_rows)
    
  messagebox.showinfo("Eliminazione completata", f"La riga con ID '{ID_to_delete}' è stata eliminata.")