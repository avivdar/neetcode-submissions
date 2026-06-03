from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    new_list = []
    counter = 0

    for element in my_list:
        new_list.append(element)
        counter += 1

    for element in elements:
        new_list.append(element)
        counter += 1
    
    return new_list



# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
