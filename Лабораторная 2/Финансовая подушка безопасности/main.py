money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0

while True:
    diff = spend - salary
    if diff > money_capital:
        break

    if month != 0:
        spend += spend * increase
        money_capital += salary - spend
        month += 1

    elif month == 0:
        money_capital += salary - spend
        month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
