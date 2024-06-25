import sqlite3


def show_stores():
    conn = sqlite3.connect('stores.db')
    cursor = conn.cursor()

    cursor.execute('SELECT store_id, title FROM stores')
    stores = cursor.fetchall()

    print(
        "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")

    conn.close()


def show_products(store_id):
    conn = sqlite3.connect('stores.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name, category, price, quantity FROM products WHERE store_id = ?', (store_id,))
    products = cursor.fetchall()

    for product in products:
        print(f"\nНазвание продукта: {product[0]}")
        print(f"Категория: {product[1]}")
        print(f"Цена: {product[2]}")
        print(f"Количество на складе: {product[3]}")

    conn.close()


def main():
    while True:
        show_stores()
        try:
            store_id = int(input("Введите id магазина: "))
            if store_id == 0:
                print("Выход из программы.")
                break
            show_products(store_id)
        except ValueError:
            print("Пожалуйста, введите корректный id магазина.")


if __name__ == "__main__":
    main()
