### Library Management System This project is a 
**Library Management System** built using
**Python** and **MySQL**.
The system is designed to manage books,
library members, and employees. It supports basic functionalities like adding, updating
, and searching for data. --- ### Features ####
1. **Book Management**
2. - Add new books to the library.
- Search for books by title.
-  #### 2. **Member Management**
- Register new members.
- Remove members by ID. ####
-  3. **Employee Management**
   4.  - Add new employees. - View a list of all employees.
--- ### Requirements - Python 3.7+ - MySQL Server - Required Python packages:
 ```bash pip install mysql-connector-python ``` --- ### How to Use 1. **Setup the Database** - Create a MySQL database named `library_db`.
 - Create the following tables: ```sql CREATE TABLE books ( book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255),
 -  publication_year INT, genre VARCHAR(100) ); CREATE TABLE members ( member_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50),
 -   last_name VARCHAR(50), email VARCHAR(100) ); CREATE TABLE employees ( employee_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50),
 -    last_name VARCHAR(50), role VARCHAR(100) ); ``` 2. **Run the Program** - Save the Python script as `library_management.py`.
   Run the script using: ```bash python library_management.py ``
 3. **Follow the Menu** - Use the interactive menu to manage books, members, and employees.
   - ### Error Handling The system uses `try-except` blocks to handle common errors, such as:
 - Database connection issues. - Invalid input data. --- ### Example Usage #### Add a New Book:
   ``` Enter your choice: 1 Enter book title: The Great Gatsby Enter author: F. Scott Fitzgerald Enter publication year: 1925 Enter genre: Fiction ``` #### Search for a Book:
    ``` Enter your choice: 2 Enter book title to search: Gatsby (1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction') ```
    --- ### Future Enhancements - Add functionality to track book borrowing and returns. - Include login and authentication for employees.
   - Enhance the search functionality with filters for authors, genres, etc. --- This project is a simple foundation for managing a library and can be extended for more complex functionalities.
