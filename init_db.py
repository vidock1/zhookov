import sqlite3
connection = sqlite3.connect('database.db')
cur = connection.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS 'employees' (
	'id_employee' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' TEXT,
	'email' TEXT,
	'phone_number' TEXT,
	'position' TEXT,
	'department' TEXT,
	'chief_id' INTEGER
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS 'clients' (
	'id_client' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' TEXT,
	'email' TEXT,
	'phone_number' TEXT,
	'passport' TEXT
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS 'events' (
	'id_event' INTEGER PRIMARY KEY AUTOINCREMENT,
	'address' TEXT,
	'people' INTEGER,
    'date' TEXT,
	'description' TEXT,
	'client_id' INTEGER
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS 'contracts' (
	'id_contract' INTEGER PRIMARY KEY AUTOINCREMENT,
	'number' TEXT,
	'date' TEXT,
	'deal_status' BLOB,
	'price' INTEGER,
	'event_id' INTEGER,
	'client_id' INTEGER,
	'employee_id' INTEGER
)""")
cur.execute("""CREATE TABLE IF NOT EXISTS 'reports' (
	'id_report' INTEGER PRIMARY KEY AUTOINCREMENT,
	'number' TEXT,
	'date' TEXT,
	'report_type' TEXT,
	'description' TEXT,
	'employee_id' INTEGER
)""")

cur.execute("INSERT INTO 'employees' ('name', 'email', 'phone_number', 'position', 'department', 'chief_id')  VALUES (?, ?, ?, ?, ?, ?)",
            ('Дерябенко Николай Викторович', 'fiffa@gmail.ru', '89998324352', 'Старший manager', 'Отдел работы с клиентами', 0))
cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number', 'passport')  VALUES (?, ?, ?, ?)",
            ('Иванов Антон Алексеевич', 'mirodmirgs@gmail.ru', '81275938503', '4050 123456'))
cur.execute("INSERT INTO 'events' ('address', 'people', 'date', 'description', 'client_id')  VALUES (?, ?, ?, ?, ?)",
            ('Тверская область, город Воскресенск, шоссе Бухарестская, 87', 7,'01.01.2025', ' ', 1))
cur.execute("INSERT INTO 'contracts' ('number', 'date', 'deal_status', 'price', 'event_id', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('01.01.2025', '01.01.2025', True, 1000, 1, 1, 1))

cur.execute("INSERT INTO 'clients' ('name', 'email', 'phone_number', 'passport')  VALUES (?, ?, ?, ?)",
            ('Жмышенко Евгений Антонович', 'shinima3@ya.ru', '80936738518', '4050 001002'))
cur.execute("INSERT INTO 'events' ('address', 'people', 'date', 'description', 'client_id')  VALUES (?, ?, ?, ?, ?)",
            ('Самарская область, город Можайск, шоссе Балканская, 42', 1, '01.02.2025', ' ', 2))
cur.execute("INSERT INTO 'contracts' ('number', 'date', 'deal_status', 'price', 'event_id', 'client_id', 'employee_id')  VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('01.02.2025', '01.02.2025', True, 1200, 2, 2, 1))
connection.commit()
connection.close()