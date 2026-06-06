def add_two_numbers() -> int:
    line = input()
    parts = line.split(",")
    int_list = []
    for s in parts:
        int_list.append(int(s))
    return int_list[0] + int_list[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
