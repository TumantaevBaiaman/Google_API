import pandas as pd
from config import db_func, parser


def add_db():
    excel_data = pd.read_excel('file/test.xlsx', usecols=['№', 'заказ №', 'стоимость,$', 'срок поставки'])
    # f = open('../test.xlsx')
    usd = parser.parser()
    data_file = excel_data.to_dict(orient='record')
    for i in data_file:
        info = {}
        info['id_order'] = i['заказ №']
        info['usd'] = i['стоимость,$']
        info['pub'] = i['стоимость,$'] * usd
        info['time'] = str(i['срок поставки'])
        db_func.add(info)