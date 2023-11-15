import json


filename = 'input.json'
# TODO решите задачу
def task() -> float:
    with open(filename) as f:
        data = json.load(f)

    sum_data = sum([i["score"] * i["weight"] for i in data])
    return round(sum_data, 3)


print(task())
