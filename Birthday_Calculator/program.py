import datetime

print('----------------------------')
print('----BIRTHDAY CALCULATOR-----')
print('----------------------------')
print()


def get_users_birthday():
    year_text = input('Year: ')
    year = int(year_text)

    month_text = input('Month: ')
    month = int(month_text)

    day_text = input('Day: ')
    day = int(day_text)

    birthday = datetime.date(year, month, day)

    return birthday


def compute_days_between_dates(date1, date2):
    this_years_birthday = datetime.date(date2.year, date1.month, date1.day)
    dt = this_years_birthday - date2
    return dt.days


def print_birthday_information(days):
    if days < 0:
        days = days * -1
        print('your birthday was {} days ago'.format(days))
    elif days > 0:
        print('your birthday is {} days from now'.format(days))
    else:
        print('Happy Birthday')


def main():
    birthday = get_users_birthday()
    days = compute_days_between_dates(birthday, datetime.date.today())
    print_birthday_information(days)


main()
