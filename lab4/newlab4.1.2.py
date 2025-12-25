import datetime
def show_datetime():
    now = datetime.datetime.now()
    print(now.strftime("%d.%m.%Y %H:%M:%S"))

show_datetime()
