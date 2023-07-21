temp_str = "kim    ,   park ,   choi,,,,,,"

temp_list = [value.strip() for value in temp_str.split(",") if value.strip()]

print(f"temp_str: {temp_str}")
print(f"temp_list: {temp_list}")