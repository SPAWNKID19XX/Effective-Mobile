# Effective-Mobile
Test task for effective mobile

Тестовое задание: Разработка консольного приложения "Личный финансовый
кошелек"

Цель: Создать приложение для учета личных доходов и расходов.

Основные возможности:
1. Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.
2. Добавление записи: Возможность добавления новой записи о доходе или расходе.
3. Редактирование записи: Изменение существующих записей о доходах и расходах.
4. Поиск по записям: Поиск записей по категории, дате или сумме.

Требования к программе:
1. Интерфейс: Реализация через консоль (CLI), без использования веб- или
графического интерфейса (также без использования фреймворков таких как Django,
FastAPI, Flask и тд).
2. Хранение данных: Данные должны храниться в текстовом файле. Формат файла
определяется разработчиком.
3. Информация в записях: Каждая запись должна содержать дату, категорию
(доход/расход), сумму, описание (возможны дополнительные поля).

Будет плюсом:
1. Аннотации: Аннотирование функций и переменных в коде.
2. Документация: Наличие документации к функциям и основным блокам кода.
3. Описание функционала: Подробное описание функционала приложения в README
файле.
4. GitHub: Размещение кода программы и примера файла с данными на GitHub.
5. Тестирование.
6. Объектно-ориентированный подход программирования.

Пример структуры данных в файле:
Дата: 2024-05-02
Категория: Расход
Сумма: 1500
Описание: Покупка продуктов

Дата: 2024-05-03
Категория: Доход
Сумма: 30000
Описание: Зарплата

Это задание направлено на проверку навыков работы с файлами, понимания основ
программирования и способности к созданию структурированного и читаемого кода.
Удачи в реализации!



Program Name: Accounting System

Description:
This program serves as an accounting system to manage financial records. It allows users to perform various operations such as adding records, viewing records, searching for records, 
and editing records.

Features:
1. Add Record: Allows users to add new financial records to the system.
2. View Expenses: Displays a list of expense records.
3. View Incomes: Displays a list of income records.
4. View All Records: Displays a list of all financial records.
5. Search Records: Allows users to search for records by category, creation date, or amount.
6. Edit Records: Allows users to edit existing records.

Program Components:
1. Menu Class:
   - Initializes a menu with options for different operations.
   - Provides a formatted menu display.

2. Record Class:
   - Represents a financial record with attributes such as creation date, updated date, category, amount, and description.
   - Provides methods to set category, amount, and description.
   - Provides a string representation of the record.

3. csv_open Function:
   - Handles opening and writing to the CSV file that stores financial records.
   - Creates the CSV file if it doesn't exist.
   - Appends new records to the CSV file.

4. add_rec Function:
   - Prompts users to input data for a new financial record.
   - Creates a new Record object with the input data.
   - Calls csv_open to add the new record to the CSV file.

5. get_balance Function:
   - Calculates the balance by summing up income and subtracting expenses from the financial records stored in the CSV file.

6. print_list Function:
   - Prints a list of financial records in a formatted manner.

7. get_list Function:
   - Retrieves financial records from the CSV file based on the specified category.
   - Calls print_list to display the retrieved records.

8. search_some_rec Function:
   - Allows users to search for financial records based on a given search string.
   - Calls print_list to display the search results.

9. edit_record Function:
   - Allows users to edit existing financial records.
   - Retrieves the record to be edited.
   - Prompts users to input new data for the record.
   - Updates the record with the new data and writes the updated records back to the CSV file.

Usage:
- Run the program and follow the menu prompts to perform different operations.
- Input data as prompted to add, view, search, or edit financial records.
- The program ensures proper formatting and error handling throughout the operations.
- The financial records are stored in a CSV file ('db.csv') located in the same directory as the program. It created after add first rec

Final Programm is in master branch

Author: Boris Isac
Date: 07-05-2024
