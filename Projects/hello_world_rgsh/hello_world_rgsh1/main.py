from datetime import date, datetime, timedelta


def close_birthday_users(users, start, end):
    now = date.today()
    result = []
    for user in users:
        birthday = user.get('birthday').replace(year=now.year)
        if start <= birthday <= end:
            result.append(user)
    return result


def get_birthdays_per_week(users):
    if not users:
        return {}
    new_users = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    today = date.today()
    year = today.year
    current_day_of_week = today.weekday()
    days_until_end_of_week = 6 - current_day_of_week
    days_until_next_week = days_until_end_of_week + 1
    first_day_of_next_week = today + timedelta(days=days_until_next_week)
    last_day_of_next_week = first_day_of_next_week + timedelta(days=6)
    first_day_of_next_week = first_day_of_next_week
    last_day_of_next_week = last_day_of_next_week
    for user in users:
        name = user['name']
        birthday_date = user['birthday']
        new_birthday_date = birthday_date.replace(year=year)
        birthday_date_day = new_birthday_date.weekday()
        if new_birthday_date >= first_day_of_next_week and new_birthday_date <= last_day_of_next_week:
            if birthday_date_day == 5 or birthday_date_day == 6 or birthday_date_day == 0:
                new_users['Monday'].append(name)
            elif birthday_date_day == 1:
                new_users['Tuesday'].append(name)
            elif birthday_date_day == 2:
                new_users['Wednesday'].append(name)
            elif birthday_date_day == 3:
                new_users['Thursday'].append(name)
            else:
                new_users['Friday'].append(name)
        else:
            continue
    if any(new_users[day] for day in new_users):
        return new_users
    else:
        return {}


if __name__ == "__main__":
    users = [
        {"name": "Bill", "birthday": datetime(year=2023, month=10, day=29).date()},
        {"name": "Andrew", "birthday": datetime(year=2023, month=11, day=2).date()},
        {"name": "Jill", "birthday": datetime(year=2023, month=11, day=4).date()},
        {"name": "Till", "birthday": datetime(year=2023, month=11, day=5).date()},
        {"name": "Jan", "birthday": datetime(year=2023, month=11, day=6).date()},
    ]
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
    result = get_birthdays_per_week(users)
    print(result)
