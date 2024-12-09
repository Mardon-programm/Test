'''Задание 1'''
# import sqlite3
# from sqlite3 import Error

# class DatabaseManager:
#     def __init__(self, base_db ):
#         self.base_db = base_db
#         self.connect = None

#     def open_connect(self):
#         try:
#             self.connect = sqlite3.connect(self.base_db)
#             print(f'Соединение с базой данных {self.base_db} успешно установен!')
#         except Error as a:
#             print(f'Ошибка при подключении к базе данных: {a}')

#     def close_connect(self):
#         if self.connect:
#             self.connect.close()
#             print(f'Соединение с базой данных {self.base_db} закрыт!')
#         else:
#             print(f'Соединение с базой данных {self.base_db} не было открыто!')

#     def get_connect(self):
#         return self.connect
    
# if __name__  == "__main__":
#     db_manager = DatabaseManager('example.db')

#     db_manager.open_connect()

#     conn = db_manager.get_connect()

#     db_manager.close_connect()


'''Задание 2'''
# import sqlite3
# connect = sqlite3.connect('Geeks_students.db')
# cursor = connect.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         full_name VARCHAR (40) NOT NULL,
#         age  INT DEFAULT NULL,
#         is_have BOOLEAN NOT NULL DEFAULT FALSE,
#         birth_date DATE
#     )       
# """)

# def student_register():
#     full_name = input('Введите своё Ф.И.О :')
#     age = int(input('Введите ваш возраст:'))
#     is_have = bool(input('Наличие ноутбука:'))
#     birth_date = input('Введите дату рождения:')

#     cursor.execute(""" INSERT INTO users
#                    (full_name, age, direction, is_have, rating, birth_date)
#                    VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, is_have, birth_date))
#     connect.commit()

# def all_students():
#     cursor.execute("SELECT * FROM users")
#     students = cursor.fetchall()
#     print(students)

# def delete_student(id):
#     cursor.execute("SELECT * FROM users")
#     students = cursor.fetchall()
#     print(students)


# register()
# all_students()
# delete_students(1)
    

'''Задание 3'''
# import sqlite3
# from sqlite3 import Error

# class DatabaseManager:
#     def __init__(self, db_file):
#         self.db_file = db_file
#         self.connection = None

#     def open_connection(self):
#         try:
#             self.connection = sqlite3.connect(self.db_file)
#             print(f"Соединение с базой данных {self.db_file} успешно установлено.")
#         except Error as b:
#             print(f"Ошибка при подключении к базе данных: {b}")
    
#     def close_connection(self):
#         if self.connection:
#             self.connection.close()
#             print("Соединение с базой данных закрыто.")
#         else:
#             print("Соединение не было открыто.")
    
#     def get_connection(self):
#         return self.connection

# class User:
#     def __init__(self, user_id, username, email):
#         self.user_id = user_id
#         self.username = username
#         self.email = email
    
#     def __str__(self):
#         return f"User {self.username} (ID: {self.user_id}, Email: {self.email})"

#     def save(self, db_manager):
#         conn = db_manager.get_connection()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (self.username, self.email))
#         db_manager.get_connection().commit()
#         self.user_id = cursor.lastrowid  
#         print(f"User {self.username} saved with ID {self.user_id}")

#     def load(cls, db_manager, user_id):
#         conn = db_manager.get_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
#         user_data = cursor.fetchone()
#         if user_data:
#             return cls(*user_data)
#         return None

# class Admin(User):
#     def __init__(self, user_id, username, email, admin_role):
#         super().__init__(user_id, username, email)
#         self.admin_role = admin_role  

#     def __str__(self):
#         return f"Admin {self.username} (ID: {self.user_id}, Email: {self.email}, Role: {self.admin_role})"

#     def save(self, db_manager):
#         super().save(db_manager)  
#         conn = db_manager.get_connection()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO admins (user_id, admin_role) VALUES (?, ?)", (self.user_id, self.admin_role))
#         db_manager.get_connection().commit()
#         print(f"Admin {self.username} saved with role {self.admin_role}")

#     def load(cls, db_manager, user_id):
#         conn = db_manager.get_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT users.user_id, users.username, users.email, admins.admin_role "
#                        "FROM users JOIN admins ON users.user_id = admins.user_id WHERE users.user_id = ?", (user_id,))
#         admin_data = cursor.fetchone()
#         if admin_data:
#             return cls(*admin_data)
#         return None

# class Customer(User):
#     def __init__(self, user_id, username, email, customer_level):
#         super().__init__(user_id, username, email)
#         self.customer_level = customer_level  

#     def __str__(self):
#         return f"Customer {self.username} (ID: {self.user_id}, Email: {self.email}, Level: {self.customer_level})"

#     def save(self, db_manager):
#         """Сохранить клиента в таблице customers"""
#         super().save(db_manager)  
#         conn = db_manager.get_connection()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO customers (user_id, customer_level) VALUES (?, ?)", (self.user_id, self.customer_level))
#         db_manager.get_connection().commit()
#         print(f"Customer {self.username} saved with level {self.customer_level}")

#     def load(cls, db_manager, user_id):
#         """Загрузить клиента по ID"""
#         conn = db_manager.get_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT users.user_id, users.username, users.email, customers.customer_level "
#                        "FROM users JOIN customers ON users.user_id = customers.user_id WHERE users.user_id = ?", (user_id,))
#         customer_data = cursor.fetchone()
#         if customer_data:
#             return cls(*customer_data)
#         return None

# if __name__ == "__main__":
#     db_manager = DatabaseManager('example.db')
#     db_manager.open_connection()

#     conn = db_manager.get_connection()
#     cursor = conn.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         username TEXT NOT NULL,
#                         email TEXT NOT NULL);''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
#                         user_id INTEGER PRIMARY KEY,
#                         admin_role TEXT NOT NULL,
#                         FOREIGN KEY(user_id) REFERENCES users(user_id));''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
#                         user_id INTEGER PRIMARY KEY,
#                         customer_level TEXT NOT NULL,
#                         FOREIGN KEY(user_id) REFERENCES users(user_id));''')

#     db_manager.get_connection().commit()

#     admin = Admin(None, "admin_user", "admin@example.com", "super_admin")
#     admin.save(db_manager)

#     customer = Customer(None, "customer_user", "customer@example.com", "premium")
#     customer.save(db_manager)

#     loaded_admin = Admin.load(db_manager, admin.user_id)
#     loaded_customer = Customer.load( db_manager,  customer.user_id, 1)

#     print(loaded_admin)
#     print(loaded_customer)

#     db_manager.close_connection()

'''Задание 4'''
# import sqlite3
# from sqlite3 import Error

# class DatabaseManager:
#     def __init__(self, db_file):
#         self.db_file = db_file
#         self.connection = None

#     def open_connection(self):
#         try:
#             self.connection = sqlite3.connect(self.db_file)
#             print(f"Соединение с базой данных {self.db_file} успешно установлено.")
#         except Error as c:
#             print(f"Ошибка при подключении к базе данных: {c}")
    
#     def close_connection(self):
#         if self.connection:
#             self.connection.close()
#             print("Соединение с базой данных закрыто.")
#         else:
#             print("Соединение не было открыто.")
    
#     def get_connection(self):
#         return self.connection
#     def search_user_username(self, user_name):
#         conn = self.get_connection()
#         cursor = conn.cursor()

#         cursor.execute("SELECT * FROM users WHERE username = ?", (user_name,))
#         user_data = cursor.fetchone()

#         if user_data:
#             print(f'Пользователь найден: {user_data}')

#         else:
#             print(f'Пользователь с именен {user_name} не найден!')

# if __name__ == "__main__":
#     db_manager = DatabaseManager('example.db')
#     db_manager.open_connection()

#     conn = db_manager.get_connection()
#     cursor = conn.cursor()

#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         username TEXT NOT NULL,
#                         email TEXT NOT NULL);''')
    
#     db_manager.get_connection().commit()

#     cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("test_user", "test@example.com"))
#     db_manager.get_connection().commit()

#     db_manager.search_user_username("test_user")

#     db_manager.close_connection()

'''Задание 5'''
import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def open_connection(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            print(f"Соединение с базой данных {self.db_file} успешно установлено.")
        except Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Соединение с базой данных закрыто.")
        else:
            print("Соединение не было открыто.")
    
    def get_connection(self):
        return self.connection

    def perform_transaction(self, operations):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            conn.execute("BEGIN TRANSACTION;")
            
            for operation in operations:
                cursor.execute(operation)
            
            conn.commit()
            print("Транзакция выполнена успешно.")
        
        except Error as e:

            conn.rollback()
            print(f"Ошибка при выполнении транзакции: {e}. Откат изменений.")
        
if __name__ == "__main__":
    db_manager = DatabaseManager('example.db')
    db_manager.open_connection()

    conn = db_manager.get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL);''')

    db_manager.get_connection().commit()

    operations = [
        "INSERT INTO users (username, email) VALUES ('user1', 'user1@example.com')",
        "INSERT INTO users (username, email) VALUES ('user2', 'user2@example.com')",
        "INSERT INTO users (username, email) VALUES ('user3', 'user3@example.com')"
    ]

    db_manager.perform_transaction(operations)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Текущие пользователи в базе данных:", users)

    db_manager.close_connection()
