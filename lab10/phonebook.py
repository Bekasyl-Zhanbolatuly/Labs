import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="postgres",
    password="1234abcd"  # ← новый пароль
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        phone VARCHAR(20)
    );
""")

conn.commit()
cur.close()
conn.close()

print("Таблица phonebook создана.")
import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="lab10",
        user="postgres",
        password="1234abcd"
    )

def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50),
                    phone VARCHAR(20)
                );
            """)
            conn.commit()
            print("Table 'phonebook' created.")

def insert_from_console():
    username = input("Enter name: ")
    phone = input("Enter phone number: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
            conn.commit()
            print("Data inserted.")

def insert_from_csv():
    file = input("Enter CSV filename (e.g., contacts.csv): ")
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        with connect() as conn:
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row['username'], row['phone']))
                conn.commit()
                print("CSV data inserted.")

def update_data():
    username = input("Enter the username to update: ")
    phone = input("Enter the new phone number: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (phone, username))
            conn.commit()
            print("Data updated.")

def filter_data():
    keyword = input("Enter a filter (name or phone): ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM phonebook
                WHERE username ILIKE %s OR phone LIKE %s
            """, (f"%{keyword}%", f"%{keyword}%"))
            rows = cur.fetchall()
            for row in rows:
                print(row)

def delete_data():
    keyword = input("Enter username or phone number to delete: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE username = %s OR phone = %s", (keyword, keyword))
            conn.commit()
            print("Data deleted.")

def menu():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Insert from console")
        print("2. Insert from CSV file")
        print("3. Update phone number")
        print("4. Query phonebook")
        print("5. Delete from phonebook")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            filter_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    menu()
