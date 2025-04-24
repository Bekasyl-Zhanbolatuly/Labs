import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="lab11",
        user="postgres",
        password="1234abcd"
    )

def search(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook2(%s);", (pattern,))
            results = cur.fetchall()
            for row in results:
                print(row)

def insert_or_update(username, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user2(%s::VARCHAR, %s::VARCHAR);", (username, phone))
            conn.commit()
            print("Inserted or updated.")

def insert_many(names, phones):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_users2(%s, %s);", (names, phones))
            conn.commit()
            print("Batch insert done.")

def get_paginated(limit, offset):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_paginated2(%s, %s);", (limit, offset))
            rows = cur.fetchall()
            for row in rows:
                print(row)

def delete_user(keyword):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_user2(%s::TEXT);", (keyword,))
            conn.commit()
            print("Deleted.")

def menu():
    while True:
        print("\nМеню:")
        print("1. Добавить или обновить пользователя")
        print("2. Добавить список пользователей")
        print("3. Поиск по шаблону")
        print("4. Постраничный вывод")
        print("5. Удалить пользователя")
        print("6. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            name = input("Имя: ")
            phone = input("Телефон: ")
            insert_or_update(name, phone)
        elif choice == "2":
            names = input("Введите имена через запятую: ").split(",")
            phones = input("Введите телефоны через запятую: ").split(",")
            names = [n.strip() for n in names]
            phones = [p.strip() for p in phones]
            insert_many(names, phones)
        elif choice == "3":
            pattern = input("Введите шаблон поиска: ")
            search(pattern)
        elif choice == "4":
            limit = int(input("Лимит: "))
            offset = int(input("Смещение: "))
            get_paginated(limit, offset)
        elif choice == "5":
            keyword = input("Имя или телефон для удаления: ")
            delete_user(keyword)
        elif choice == "6":
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()
