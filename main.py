from start_gui import start_gui

if __name__ == "__main__":
  # File name
  name = "prova.csv"

  # Dataset's informations
  headers = [
    "ID",
    "Luogo di acuisto",
    "Data di acquisto",
    "Importo",
    "IVA",
    "Categoria",
    "Metodo di pagamento",
    "Note"
  ]
  start_gui(name, headers)