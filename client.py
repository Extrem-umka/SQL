import psycopg2

conn = psycopg2.connect(database='client', user='postgres', password='Klizma1234')
with conn.cursor() as cur:

        #создание бд клиентов
    def create_cl(conn):
        cur.execute("""CREATE TABLE client(id serial primary key, first_name VARCHAR(50) not null, last_name VARCHAR(50) not null, email VARCHAR(100) not null);""")
        conn.commit()

        # создание бд телефонов
    def create_ph(conn):
        cur.execute("""CREATE TABLE phone(id serial primary key, phones BIGINT CHECK (phones is null or phones>5), client_id integer references client(id));""")
        conn.commit()

        #добавление нового клиента
    def add_client(conn, first_name, last_name, email):
        first_name = input('Введите имя клиента: ')
        last_name = input('Введите фамилию клиента: ')
        email = input('Введите электронную почту клиента: ')
        cur.execute("""INSERT INTO client(first_name, last_name, email) VALUES (%s, %s, %s);""",
                    (first_name, last_name, email))
        conn.commit()

        #добавление телефона для существующего клиента
    def add_phone(conn, phones, client_id):
        phones_num = input('Введите номер телефона клиента: ')
        find_id = input('Введите id клиента: ')
        cur.execute("""INSERT INTO phone(phones, client_id) VALUES (%s, %s);""", (phones_num, find_id))
        conn.commit()

        #изменение данных существующего клиента
    def change_client(conn, client_id):
        client_id = input('Введите id клиента: ')
        first_name = input('Введите имя клиента: ')
        last_name = input('Введите фамилию клиента: ')
        email = input('Введите электронную почту клиента: ')
        cur.execute("""UPDATE client SET first_name=%s, last_name=%s, email=%s;""",
                    (first_name, last_name, email))
        conn.commit()

        #удаление телефона существующего клиента
    def delete_phone(conn, client_id, phone):
        phones_num = int(input('Введите номер телефона для удаления: '))
        cur.execute("""DELETE FROM phone WHERE phones=%s;""", (phones_num,))
        conn.commit()

        # удаление существующего клиента
    def delete_client(conn, client_id):
        client_id = input('Введите id клиента: ')
        cur.execute("""DELETE FROM client WHERE client.id=%s;""", (client_id,))
        conn.commit()

        # поиск клиента по его данным
    def find_client(conn, first_name=None, last_name=None, email=None):
        first_name = input('Введите имя клиента: ')
        last_name = input('Введите фамилию клиента: ')
        email = input('Введите электронную почту клиента: ')
        cur.execute("""SELECT id FROM client WHERE first_name=%s or last_name=%s or email=%s;""",
                    (first_name, last_name, email))
        return cur.fetchone()[0]




    def main():
        print('''Для уточнения команд введите "help"''')
        description = input()
        if description == "help":
            print('''
            create_cl - создание таблицы клиентов
            create_ph - создание таблицы телефонов клиентов
            add_client - добавление клиента в бд
            add_phone - добавление телефона клиента в бд
            change_client - корректировка клиента
            delete_phone - удаление телефона с бд
            delete_client - удаление клиента с бд
            find_client  - поиск id клиента по имени, фамилии, эл.почте
            ''')
        while True:
            command = input('Введите команду: ')
            if command == 'create_cl':
                create_cl(conn)
            elif command == 'create_ph':
                create_ph(conn)
            elif command == 'add_client':
                first_name = input('Введите имя клиента: ')
                last_name = input('Введите фамилию клиента: ')
                email = input('Введите электронную почту клиента: ')
                cur.execute("""INSERT INTO client(first_name, last_name, email) VALUES (%s, %s, %s);""",
                            (first_name, last_name, email))
                conn.commit()
                print(f'Новый клиент {first_name} {last_name} c эл.почтой {email} добавлен')
            elif command == 'add_phone':
                phones_num = input('Введите номер телефона клиента: ')
                find_id = input('Введите id клиента: ')
                cur.execute("""INSERT INTO phone(phones, client_id) VALUES (%s, %s);""", (phones_num, find_id))
                conn.commit()
                print(f'Номер телефона {phones_num} для существующего клиента {find_id} добавлен')
            elif command == 'change_client':
                client_id = input('Введите id клиента: ')
                first_name = input('Введите имя клиента: ')
                last_name = input('Введите фамилию клиента: ')
                email = input('Введите электронную почту клиента: ')
                cur.execute("""UPDATE client SET client_id=%s, first_name=%s, last_name=%s, email=%s;""",
                            (client_id, first_name, last_name, email))
                conn.commit()
                print(f'Данные клиента {first_name} {last_name} изменены')
            elif command == 'delete_phone':
                phones_num = int(input('Введите номер телефона для удаления: '))
                cur.execute("""DELETE FROM phone WHERE phones=%d;""", (phones_num,))
                conn.commit()
                print(f'Номер телефона{phones_num} удален')
            elif command == 'delete_client':
                client_id = input('Введите id клиента: ')
                cur.execute("""DELETE FROM client WHERE client.id=%s;""", (client_id,))
                conn.commit()
                print(f'Клиент с id={client_id} удален')
            elif command == 'find_client':
                find_cl = find_client(conn, first_name=None, last_name=None, email=None)
                print(f'client_id {find_cl}')
            elif command == 'exit':
                return

    print(main())



conn.close()
