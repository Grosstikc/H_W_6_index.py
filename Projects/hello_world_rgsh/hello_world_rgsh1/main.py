from datetime import date, timedelta


users = [
    {"name": "Bill", "birthday": date(2023, 10, 29)},
    {"name": "Andrew", "birthday": date(2023, 11, 2)},
    {"name": "Jill", "birthday": date(2023, 11, 4)},
    {"name": "Till", "birthday": date(2023, 11, 5)},
    {"name": "Jan", "birthday": date(2023, 11, 6)},
]

def get_birthdays_per_week(users):
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    birthdays_per_week = {}

    for user in users:
        name = user["name"]
        birthday = user["birthday"].replace(year=today.year)  # Встановити рік на поточний рік

        # Якщо день народження раніше, ніж сьогодні, враховуйте його на наступний рік
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        # Перевірте, чи день народження припадає на поточний тиждень чи на наступний
        if start_of_week <= birthday <= end_of_week:
            day_of_week = birthday.strftime("%A")
            if day_of_week not in birthdays_per_week:
                birthdays_per_week[day_of_week] = []
            birthdays_per_week[day_of_week].append(name)

    # Перенесіть дні народження у вихідні (субота та неділя) на понеділок
    if "Sunday" in birthdays_per_week:
        birthdays_per_week["Monday"] = birthdays_per_week.get("Monday", []) + birthdays_per_week["Sunday"]
        del birthdays_per_week["Sunday"]
    if "Saturday" in birthdays_per_week:
        birthdays_per_week["Monday"] = birthdays_per_week.get("Monday", []) + birthdays_per_week["Saturday"]
        del birthdays_per_week["Saturday"]

    return birthdays_per_week


result = get_birthdays_per_week(users)
print(result)


if __name__ == "__main__":
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
    result = get_birthdays_per_week(users)
    print(result)
