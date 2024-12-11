import mysql.connector
from mysql.connector import Error
# Function to connect to the database with error handling
def connect_db():
   try:
     db = mysql.connector.connect( host="localhost",
            user="root",
            password="",
            database="library_db" )
     return db
   except Error as e:
     print(f"Error connecting to database: {e}")
     return None
# Function to execute SQL queries with error handling
def execute_query(query, params=None, fetch=False):
   db = connect_db()
   if db is None:
     return [] if fetch else None
   try:
     cursor = db.cursor()
     cursor.execute(query, params) if params else cursor.execute(query)
     if fetch:
       result = cursor.fetchall()
       return result
     db.commit()
     print("Query executed successfully.")
   except Error as e:
     print(f"Error executing query: {e}")
   finally:
     db.close()
# Book management class 
class Book:
   def __init__(self, title, author, publication_year, genre):
     self.title = title
     self.author = author
     self.publication_year = publication_year
     self.genre = genre
   def add_book(self):
     query = "INSERT INTO books (title, author, publication_year, genre) VALUES (%s, %s, %s, %s)"
     params = (self.title, self.author, self.publication_year, self.genre)
     execute_query(query, params)
   @staticmethod
   def search_book(title):
     query = "SELECT * FROM books WHERE title LIKE %s"
     params = ('%' + title + '%',)
     return execute_query(query, params, fetch=True)
# Member management class
class Member:
   def __init__(self, first_name, last_name, email):
     self.first_name = first_name
     self.last_name = last_name
     self.email = email
   def register_member(self):
     query = "INSERT INTO members (first_name, last_name, email) VALUES (%s, %s, %s)"
     params = (self.first_name, self.last_name, self.email)
     execute_query(query, params)
   @staticmethod
   def remove_member(member_id):
     query = "DELETE FROM members WHERE member_id = %s"
     params = (member_id,)
     execute_query(query, params)
# Employee management class
class Employee:
   def __init__(self, first_name, last_name, role):
     self.first_name = first_name
     self.last_name = last_name
     self.role = role
   def add_employee(self):
     query = "INSERT INTO employees (first_name, last_name, role) VALUES (%s, %s, %s)"
     params = (self.first_name, self.last_name, self.role)
     execute_query(query, params)
   @staticmethod
   def show_employee_details():
     query = "SELECT * FROM employees"
     return execute_query(query, fetch=True)
# Menu for user interaction
def show_menu():
  print("Library Management System")
  print("1. Add Book")
  print("2. Search Book")
  print("3. Register Member")
  print("4. Remove Member")
  print("5. Add Employee")
  print("6. Show Employees")
  print("7. Exit")
def main():
   while True:
     show_menu()
     choice = input("Enter your choice: ")
     if choice == '1':
       title = input("Enter book title: ")
       author = input("Enter author: ")
       publication_year = input("Enter publication year: ")
       genre = input("Enter genre: ")
       book = Book(title, author, publication_year, genre)
       book.add_book()
     elif choice == '2':
       title = input("Enter book title to search: ")
       books = Book.search_book(title)
       if books:
        for book in books:
         print(book)
       else:
        print('no books found')
     elif choice == '3':
       first_name = input("Enter first name: ")
       last_name = input("Enter last name: ")
       email = input("Enter email: ")
       member = Member(first_name, last_name, email)
       member.register_member()
     elif choice == '4':
       member_id = input("Enter member ID to remove: ")
       Member.remove_member(member_id)
     elif choice == '5':
       first_name = input("Enter first name: ")
       last_name = input("Enter last name: ")
       role = input("Enter role: ")
       employee = Employee(first_name, last_name, role)
       employee.add_employee()
     elif choice == '6':
       employees = Employee.show_employee_details()
       for employee in employees:
           print(employee)
     elif choice == '7':
       break
if __name__ == "__main__":
   main()
