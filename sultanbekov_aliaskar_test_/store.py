import sqlite3

# Создание базы данных и подключение к ней
conn = sqlite3.connect('stores.db')
cursor = conn.cursor()

# Создание таблицы магазинов
cursor.execute('''
CREATE TABLE IF NOT EXISTS stores (
    store_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
)
''')

# Создание таблицы продуктов
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    store_id INTEGER,
    FOREIGN KEY (store_id) REFERENCES stores (store_id)
)
''')

# Вставка данных в таблицу магазинов
stores = [
    (1, 'Asia'),
    (2, 'Globus'),
    (3, 'Spar')
]

cursor.executemany('INSERT INTO stores (store_id, title) VALUES (?, ?)', stores)

# Вставка данных в таблицу продуктов
products = [
    ('Chocolate', 'Food products', 10.5, 129, 1),
    ('Cola', 'Food products', 2.2, 120, 1),
    ('Rice', 'Food products', 1.5, 300, 1),
    ('meat', 'Food products', 5.5, 200, 2),
    ('Sandwich', 'Food products', 1.2, 150, 2),
    ('Lentils', 'Food products', 1.1, 200, 2),
    ('cucumbers', 'Food products', 1.1, 250, 3),
    ('Tomato', 'Food products', 1.5, 300, 3),
    ('sweet pepper', 'Food products', 1.3, 100, 3),
    ('Yogurt', 'Dairy products', 1.0, 50, 1),
    ('Cheese', 'Dairy products', 2.5, 123, 1),
    ('Custard', 'Dairy products', 1.5, 122, 1),
    ('Ice cream', 'Dairy products', 1.1, 200, 2),
    ('Kefir', 'Dairy products', 1.8, 133, 2),
    ('Ricotta', 'Dairy products', 1.3, 100, 2),
    ('Buttermilk', 'Dairy products', 2.2, 20, 3),
    ('Sour cream', 'Dairy products', 3.3, 300, 3),
    ('Milk', 'Dairy products', 1.2, 100, 3),
    ('Biscuit', 'Bakery products', 2.2, 150, 1),
    ('Bagel', 'Bakery products', 1.9, 100, 1),
    ('Brownie', 'Bakery products', 2.1, 56, 1),
    ('Cake', 'Bakery products', 1.4, 33, 2),
    ('Muffin', 'Bakery products', 1.1, 55, 2),
    ('Flatbread', 'Bakery products', 2.2, 46, 2),
    ('Cracker', 'Bakery products', 3.3, 67, 3),
    ('Pastry', 'Bakery products', 2.2, 55, 3),
    ('Bread', 'Bakery products', 0.8, 200, 3)
]

cursor.executemany('INSERT INTO products (name, category, price, quantity, store_id) VALUES (?, ?, ?, ?, ?)', products)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
