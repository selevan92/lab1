# TODO Найдите количество книг, которое можно разместить на дискете

memory = 1.44 #Информационный объем дискеты в Мб
page = 100
line = 50
simbol = 25
simbol_in_bait = 4 #Объем хранения одного символа

memory_in_bait = memory * 1024 * 1024
book = page * line * simbol * simbol_in_bait
all_book = int(memory_in_bait / book)

print("Количество книг, помещающихся на дискету:", all_book)
