import delorean
from datetime import datetime, timezone


def time():
    now = datetime.now()
    dt = ''
    # dt = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    if len(str(now.day))==2:
        dt += str(now.day)+'/'
    if len(str(now.day))==1:
        dt += '0' + str(now.day) + '/'
    if len(str(now.month))==2:
        dt += str(now.month)+'/'
    if len(str(now.month))==1:
        dt += '0' + str(now.month) + '/'
    dt += str(now.year)
    return dt
