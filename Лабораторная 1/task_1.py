numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_1 = numbers[:4]
numbers_2 = numbers[5:]
new_numbers = numbers_1 + numbers_2
sum_ = sum(new_numbers)
result = sum_ / (len(numbers))
numbers[4] = result
print("Измененный список:", numbers)
