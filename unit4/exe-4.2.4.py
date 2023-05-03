if __name__ == '__main__':
    import calendar

    date_str = input("Enter a date (dd/mm/yyyy): ")
    day, month, year = map(int, date_str.split('/'))
    day_of_week = calendar.weekday(year, month, day)
    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']

    print(days_of_week[day_of_week])