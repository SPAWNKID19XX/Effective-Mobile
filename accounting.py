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
            '1': "Expanses",
            '2': "Add Expanse",
            '3': "Incomes",
            '4': "Add Income",
            '5': "Accounting list",
            '6': "Search",
            '7': "Edit",
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



    def __str__(self):
        return f'{self.date} {self.date_updated} {self.category} {self.amount} {self.description}'

def csv_open(new_rec = None):
    if not os.path.exists(CSV_DIR):
        #todo when csv file is created, first rec is ignored. solve it
        #todo try to put creation of csv in main script
        with open(CSV_DIR, 'w',newline="") as file:
            writer = csv.writer(file)
            writer.writerow(['creation_date', 'updated_date', 'category', 'amount', 'description'])
        file.close()
        print(f"CSV file '{CSV_DIR}' has been created successfully.")
    else:
        csv_file = open(CSV_DIR, 'a')
        writer = csv.writer(csv_file)
        writer.writerow([str(new_rec.date), str(new_rec.date_updated), new_rec.category,new_rec.amount, new_rec.description])

        del writer
        csv_file.close()

def add_rec(category):
    if category == '2':
        category = Record.Category.expense[1]

    elif category == '4':
        category = Record.Category.income[1]

    amount = input('Insert amount: ')
    description =  input('Insert short description: ')

    new_rec = Record(category=category, amount=amount,description=description)
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

def get_list(category=None, search_list = []):
    try:
        with open(CSV_DIR) as file:
            reader = csv.DictReader(file)
            print('\033[94m'+'creation_date'.ljust(26), 'updated_date'.ljust(33), 'category'.rjust(0),
                  'amount'.rjust(15), 'description'.rjust(15),"\033[0m" )

            if not search_list:
                if not category:
                    for row in reader:
                        print(row['creation_date'].rjust(25), row['updated_date'].rjust(25), row['category'].rjust(15), row['amount'].rjust(15),row['description'].rjust(15))
                else:
                    for row in reader:
                        if row['category'] == category:
                            print(row['creation_date'].rjust(25), row['updated_date'].rjust(25), row['category'].rjust(15), row['amount'].rjust(15),row['description'].rjust(15))

            else:
                for row in search_list:
                    print(row['creation_date'].rjust(25), row['updated_date'].rjust(25), row['category'].rjust(15),
                      row['amount'].rjust(15), row['description'].rjust(15))
    except:
        print('No records')

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
    get_list(search_list=res_list)

menu_option = 'a'
while not menu_option.isdecimal() or menu_option != '0':
    menu = Menu()
    print(menu.__str__())
    menu_option = input('Your option: ')
    if menu_option == '1':
        get_list('expense')

    if menu_option == '2':
        add_rec(menu_option)

    if menu_option == '3':
        get_list('income')

    if menu_option == '4':
        add_rec(menu_option)

    if menu_option == '5':
        get_list()

    if menu_option == '6':
        search_some_rec()
    if menu_option == '7':
        print(menu_option)

    if menu_option == '0':
        print(menu_option)
