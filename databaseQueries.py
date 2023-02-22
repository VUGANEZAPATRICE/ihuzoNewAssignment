import sqlite3

conn = sqlite3.connect('Assign_database') 
c = conn.cursor()

c.execute('''
            CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
            )

          ''')


c.execute('''
          CREATE TABLE IF NOT EXISTS promotion (
           id INT AUTO_INCREMENT PRIMARY KEY,
           employeeid INT,
           FOREIGN KEY (employeeid) REFERENCES Employees(id)
)

          ''')
# c.execute('''
#           CREATE TABLE IF NOT EXISTS prices
#           ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
#           ''')
# c.execute('''INSERT INTO employees (name) VALUES ("Joe")''')
# c.execute('''INSERT INTO employees (name) VALUES ("Henry")''')
# c.execute('''INSERT INTO employees (name) VALUES ("Sam")''')
# c.execute('''INSERT INTO employees (name) VALUES ("Max")''')
# c.execute('''INSERT INTO employees (name) VALUES ("Patrice Vuganeza")''')

# c.execute('''INSERT INTO promotion (employeeid) VALUES ("Joe")''')
# c.execute('''INSERT INTO promotion (employeeid) VALUES ("Joe")''')


c.execute('''
        SELECT e.name as employees
        FROM employees e
        LEFT JOIN promotion p ON e.id = p.employeeId
        WHERE p.id IS NULL
''')
                     
conn.commit()