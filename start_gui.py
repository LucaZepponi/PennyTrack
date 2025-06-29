from tkinter import *
from initialise_file import initialise_file
from add_expense import add_expense
from delete_expense import delete_expense
from view_expense import view_expense
from write_sorted_expenses import write_sorted_expenses
from total_expenses import total_expenses

def start_gui(name: str, headers: list[str]) -> None:
  # If csv does not exists, create it
  initialise_file(name, headers)
  
  # Windows initializzation
  root = Tk()
  root.title("Gestione Spese Personali")
  root.geometry("300x250")
  
  Label(root, text="Gestore Spese", font=("Arial", 12)).pack(pady=10)
  
  # Buttons
  Button(root, text="Aggiungi Spesa", width=20, command=lambda: add_expense(name)).pack(pady=5)
  Button(root, text="Elimina Spesa", width=20, command=lambda: delete_expense(name, headers)).pack(pady=5)
  Button(root, text="Visualizza Spese", width=20, command=lambda: view_expense(name, headers)).pack(pady=5)
  Button(root, text="Riordina Spese", width=20, command=lambda: write_sorted_expenses(name, headers)).pack(pady=5)
  Button(root, text="Somma Spese", width=20, command=lambda: total_expenses(name)).pack(pady=5)
  
  root.mainloop()