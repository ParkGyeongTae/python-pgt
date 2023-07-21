temp_list = ["kim", "park", "choi"]

for _l1 in temp_list:
    print(_l1)

for _l1 in enumerate(temp_list):
    print(_l1)

for index, value in enumerate(temp_list):
    if index == 1:
        value += " gyeongtae"
    print(f"index: {index}, value: {value}")
