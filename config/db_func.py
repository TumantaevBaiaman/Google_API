from config import db_create


def read():
    with db_create.connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM google_api;""")
        info = [i for i in cursor.fetchall()]
        return info


def read_id():
    with db_create.connection.cursor() as cursor:
        cursor.execute("""SELECT id_order FROM google_api;""")
        id_data = [i[0] for i in cursor.fetchall()]
        return id_data


def add(data):
    id_order = data['id_order']
    usd_price = data['usd']
    pub_price = data['pub']
    delivery_time = data['time']
    if id_order not in read_id():
        with db_create.connection.cursor() as cursor:
            cursor.execute("INSERT INTO google_api(id_order, usd_price, pub_price, delivery_time) VALUES (%s, %s, %s, %s);", (id_order, usd_price, pub_price, delivery_time))
        print('Добавил')
    else:
        print('Уже есть')


def update(data):
    id = data['id']
    price = data['price']
    with db_create.connection.cursor() as cursor:
        cursor.execute("UPDATE google_api SET pub_price = (%s) id_order = (%s);", (price, id))