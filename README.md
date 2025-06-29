
# 💸 PennyTrack

PennyTrack is a simple desktop application built with Python and Tkinter to help users keep track of their daily expenses.
It allow you to easily record and view purchases, including details like the place of purchase, datem amount, VAT, payment method, category, and additional notes.

## ✨ Features

- Add and view expenses throught a user-friendly graphocal interface
- Data stored in a local CSV file
- Automatic file creation on first run
- Input validation and clear error messages
- Responsive table view with adjustable column widths

## 💻 Requirements

- Python 3.7 or higher
- Tkinter (GUI)
- CSV (for persistent data storage)

## 🛠️ Installation

1. Clone the repository to your local machine:

    ```bash
        git clone https://github.com/LucaZepponi/PennyTrack.git
        cd PennyTrack
    ```
2. run the application
    ```bash
        python main.py
    ```
  (Make sure all required file like `add_expense.py`, `view_expense.py` and `initialise_file.py` are in the same directory)

## 💡 Usage

Once you run `main.py`, a graphical window will appear with tow options:
- Add Expense
- View Expences

The first button opens a form to enter:
- Place of purchase
- Date (default: today)
- Amount
- VAT
- Category (e.g. groceries, transport)
- Payment method (e.g. cash, card)
- (Optional) Notes

The second button opens a table which shows all saved expenses with column headings.

The data is stored in a local `.csv` file automatically created at first run.
You can open this file with Excel, LiberOffice, or any spreadsheet program.
## 📁 File Structure
```
PennyTrack
    ├── .gitignore
    ├── add_expense.py
    ├── delete_expense.py
    ├── initialise_file.py
    ├── main.py
    ├── README.md
    ├── sort_expenses.py
    ├── start_gui.py
    ├── view_expense.py
    └── write_sorted_expenses.py
```
## 📜 License

[GNU AFFERO GENERAL PUBLIC LICENSE](https://www.gnu.org/licenses/agpl-3.0.en.html#license-text)

## 👨🏻‍💻 Authors

- [Luca Zepponi](https://github.com/LucaZepponi)