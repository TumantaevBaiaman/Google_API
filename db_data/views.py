import pandas as pd

import file.file_read
from file import file_read
from django.shortcuts import render
from config import time, parser, db_func


def add_database(request):
    print(file_read.add_db())
    file.file_read.add_db()
    date = time.time()
    price = parser.parser()
    data = db_func.read()
    s = sum([int(i[2]) for i in data])
    r = sum([int(i[3]) for i in data])
    k = len(data)
    d = [[i[-1].split(' ')[0], i[2]] for i in data]
    print(d)
    context2 = {
        'districts': 50,
        'cities': 5
    }
    context = {'pub': price, 'data': data , 'date': date, 's': s, 'r': r, 'k': k, 'd': context2}
    return render(request, 'db_data/index.html', context=context)
