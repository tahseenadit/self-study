list1 = [10, 20, 30]

reference_to_list_1 = list1

print(f"List1: {list1}")
print(f"Reference to list1: {reference_to_list_1}\n")

list1[:] = [100, 200, 300]

print(f"List1: {list1}")
print(f"Reference to list1 after modifying list1 in place: {reference_to_list_1}\n")

reference_to_list_1 = [5, 4, 6]

print(f"List1: {list1}")
print(f"Reference to list1 after modifying reference_to_list_1: {reference_to_list_1}\n")

print("----------------------------------------------------------------------------------")

list2 = [10, 20, 30]

reference_to_list_2 = list2

print(f"List2: {list2}")
print(f"Reference to list2: {reference_to_list_2}\n")

list2[:] = [100, 200, 300]

print(f"List2: {list2}")
print(f"Reference to list2 after modifying list2 in place: {reference_to_list_2}\n")

reference_to_list_2[:] = [5, 4, 6]

print(f"List1: {list2}")
print(f"Reference to list2 after modifying reference_to_list_2 in place: {reference_to_list_2}\n")

print("----------------------------------------------------------------------------------")

list3 = [10, 20, 30]

reference_to_list_3 = list3

print(f"List3: {list3}")
print(f"Reference to list3: {reference_to_list_3}\n")

list3 = [100, 200, 300]

print(f"List3: {list3}")
print(f"Reference to list3 after modifying list3: {reference_to_list_3}")