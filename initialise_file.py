import csv
import os

def initialise_file(name: str, headers:list[str]) -> None:
  if not os.path.exists(name):
    with open(name, mode="x", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(headers)