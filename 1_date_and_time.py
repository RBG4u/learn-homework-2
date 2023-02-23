from datetime import datetime, timedelta

def print_days():
    dt_now = datetime.now().date()
    delta_1 = timedelta(days=1)
    delta_30 = timedelta(days=30)
    print(f"Сегодня: {dt_now.strftime('%d.%m.%Y')} \nВчера: {(dt_now - delta_1).strftime('%d.%m.%Y')} \n30 дней назад: {(dt_now - delta_30).strftime('%d.%m.%Y')}")

def str_2_datetime(str_date):
    date = datetime.strptime(str_date, "%d/%m/%y %H:%M:%S.%f")
    return date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
