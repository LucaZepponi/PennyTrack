import csv
from sort_expenses import sort_expenses

def write_sorted_expenses(name: str, headers:list[str], ID_column: str = "ID", descending: bool = False) -> None:
  # Sort the rows using the sort_expenses function with filter "Data di acquisto".
  rows = sort_expenses(name, column_to_sort="Data di acquisto", descending=descending)
  
  # Reassessment ID afert sorting
  for i, row in enumerate(rows, start=1):
    row[ID_column] = str(i)
    
  # Overwrite the original file with sorted data
  with open(name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)