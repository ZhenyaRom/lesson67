import sqlite3


def initiate_db(title, description, price, photo):
    connection = sqlite3.connect('base_products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    photo TEXT
    );
    ''')

    cursor.execute("INSERT INTO Products(title, description, price, photo) VALUES(?, ?, ?, ?)",
                   (title, description, price, photo))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('base_products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products


if __name__ == '__main__':
    initiate_db('Напиток арбузный', 'Объем 300 мл., калорийность 50 ккал. ', 100, '1.jpg')
    initiate_db('Напиток грушевый', 'Объем 300 мл., калорийность 60 ккал. ', 110, '2.jpg')
    initiate_db('Напиток земляничный', 'Объем 300 мл., калорийность 70 ккал. ', 120, '3.jpg')
    initiate_db('Напиток яблочный', 'Объем 300 мл., калорийность 80 ккал. ', 130, '4.jpg')
