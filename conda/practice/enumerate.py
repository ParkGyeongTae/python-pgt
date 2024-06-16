"""
ddd
"""

if __name__ == "__main__":

    names = ["kim", "park", "choi"]

    for value in names:
        print(f"value : {value}")

    for value in range(len(names)):
        print(f"value : {value}")

    for index, value in enumerate(names):
        print(f"index, value : {index, value}")

    for index, value in enumerate(names):
        if index == 1:
            value += " gyeongtae"
        print(f"index, value : {index, value}")
