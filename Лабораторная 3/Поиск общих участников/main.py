# Поиск общих участников
# Описание
# Вы организуете встречу для двух групп участников, и вам необходимо определить, кто является общими участниками для обеих групп.
# Для этого вам нужно написать функцию, которая будет принимать две строки с фамилиями участников, перечисленными без пробелов через разделитель.
# Чаще всего в качестве разделителя используется запятая.
#
# Задача
# Напишите функцию find_common_participants, принимающую две строки, в которых перечислены участники без пробелов, а также необязательный аргумент, отвечающий за разделитель по умолчанию равен запятой.
# Найдите общих участников среди двух групп.
# Верните полученный результат в виде списка общих участников отсортированных в алфавитном порядке.

# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, sep=","):
    first = set(participants_first_group.split(sep))
    second = set(participants_second_group.split(sep))
    tuple_ = tuple(sorted(first.intersection(second)))
    return print(tuple_)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, sep="|")
