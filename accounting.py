import csv
import os
import unittest, datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_DIR = os.path.join(CURRENT_DIR, 'db.csv')


class Menu:
    def __init__(self, title_menu=None, left=None, right=None):
        '''
        constructor witch warante me a correct view
        :param title_menu: "My Accounting"
        :param left: at least 20
        :param right: at least 20
        :param menu_dict: {
            '1': "Expanses",
            '2': "Add Expanse",
            '3': "Incomes",
            '4': "Add Income",
            '5': "Accounting list",
            '6': 'Search',
            '7': 'Edit'
        }
        '''
        self.title_menu = title_menu if title_menu is not None else "My Accounting"
        self.left = left if left is not None and left >= 20 else 20
        self.right = right if right is not None and right >= 20 else 20
        self.menu_dict = {
            '1': "Add Rec",
            '2': "Expanses",
            '3': "Incomes",
            '4': "View all list",
            '5': "Search",
            '6': "Edit",
            '0': "Exit"
        }

    def __str__(self):
        result = self.title_menu.center(self.left + self.right, '*') + '\n'
        result += 'Balance'.ljust(self.left, ".") + f'{get_balance():.2f}'.rjust(self.right, '.') + '\n'
        for k, v in self.menu_dict.items():
            result += k.ljust(self.left, ".") + v.rjust(self.right, '.') + '\n'
        return result


class Record:
    '''
    record is a rec for 1 moviment from your accountig
    '''

    class Category:
        '''
        two possibles vars in category
        '''
        income = ('INCOME', 'income')
        expense = ('EXPENSE', 'expense')

    def __init__(self, date=None, date_updated=None, category='income', amount=None, description=None):
        self.date = date if date is not None else datetime.datetime.now()
        self.date_updated = date_updated if date_updated is not None else datetime.datetime.now()
        self.category = category if category in (self.Category.income[1], self.Category.expense[1]) else 'income'
        self.amount = amount if amount is not None and float(amount) >= 0 else 0
        self.description = description if description is not None and isinstance(description, str) else None

    def setter_category(self):
        self.category = 'a'
        while self.category not in (self.Category.income[1], self.Category.expense[1]):
            self.category = input('Insert category (income, expense): ')
        return self.category

    def setter_amount(self):
        self.amount = 'a'
        while isinstance(self.amount, str):
            try:
                self.amount = float(input('Insert amount (float, int): '))
            except:
                print('Incorect format amount!')
        return self.amount

    def setter_description(self):
        self.description = input('Insert description: ')
        return self.description

    def __str__(self):
        return f'{self.date} {self.date_updated} {self.category} {self.amount} {self.description}'


import os
import csv

def csv_open(new_rec):
    if not os.path.exists(CSV_DIR):
        # Create the CSV file with header if it doesn't exist
        with open(CSV_DIR, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(['creation_date', 'updated_date', 'category', 'amount', 'description'])
        print(f"CSV file '{CSV_DIR}' has been created successfully.")
    try:
        with open(CSV_DIR, 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([str(new_rec.date), str(new_rec.date_updated), new_rec.category, new_rec.amount, new_rec.description])
        print("New record has been added to the CSV file.")
    except (IOError, PermissionError) as e:
        print(f"Error occurred while writing to the CSV file: {e}")



def add_rec():
    record = Record()
    category = record.setter_category()
    amount = record.setter_amount()
    description = record.setter_description()
    new_rec = Record(category=category, amount=amount, description=description)
    csv_open(new_rec)



def get_balance():
    balance = 0.00
    try:
        with open(CSV_DIR) as file:
            reader = csv.DictReader(file)
            for obj in reader:
                if obj['category'] == 'income':
                    balance += float(obj['amount'])
                else:
                    balance -= float(obj['amount'])
    except:
        print('file csv does not exist yet')
    return balance


def print_list(list=[]):
    print("\033[91m" + 'id'.center(8), '\033[94m' + 'creation_date'.ljust(26), 'updated_date'.ljust(33),
          'category'.rjust(0),
          'amount'.rjust(15), 'description'.rjust(15), "\033[0m")

    for i, row in enumerate(list):
        print(f"{i + 1}".center(8), "\033[0m" + row['creation_date'].rjust(25), row['updated_date'].rjust(25),
              row['category'].rjust(15),
              row['amount'].rjust(15), row['description'].rjust(15))


def get_list(category=None):
    res = []
    with open(CSV_DIR) as file:
        reader = csv.DictReader(file)
        if not category:
            for row in reader:
                res.append(row)
        else:
            for i, row in enumerate(reader):
                if row['category'] == category:
                    res.append(row)
    print_list(res)


def search_some_rec():
    res_list = []
    str_text = input('Insert category,create date or amount:')
    with open(CSV_DIR) as file:
        reader = csv.DictReader(file)
        for row in reader:
            for obj in row:
                if str_text in row[obj] and row not in res_list:
                    res_list.append(row)
                    continue
    print_list(res_list)


def edit_record():
    get_list()
    edit_rec = None
    rows = []

    # Read the CSV file and store its contents in memory
    with open(CSV_DIR, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header
        for row in reader:
            rows.append(row)

    while True:
        try:
            edit_rec = int(input('ID to edit: '))
            if 0 < edit_rec <= len(rows):
                break  # Exit the loop if the input is valid
            else:
                print("Invalid ID. Please enter a valid ID.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    old_rec = rows[edit_rec - 1]
    print(old_rec)

    # Assuming Record class has appropriate methods for setting category, amount, and description
    rec = Record()
    category = rec.setter_category()
    amount = rec.setter_amount()
    description = rec.setter_description()

    # Create a new record with the updated data
    new_row = [
        old_rec[0],  # Date (assuming it's not edited)
        datetime.datetime.now(),  # Updated date
        category,
        amount,
        description
    ]
    rows[edit_rec - 1] = new_row  # Replace the old row with the new one

    # Write the updated data back to the CSV file
    with open(CSV_DIR, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header back
        writer.writerows(rows)


menu_option = 'a'
while not menu_option.isdecimal() or menu_option != '0':
    menu = Menu()
    print(menu.__str__())
    menu_option = input('Your option: ')

    if menu_option == '1':
        add_rec()

    if menu_option == '2':
        get_list('expense')

    if menu_option == '3':
        get_list('income')

    if menu_option == '4':
        get_list()

    if menu_option == '5':
        search_some_rec()

    if menu_option == '6':
        edit_record()

    if menu_option == '0':
        print(menu_option)
