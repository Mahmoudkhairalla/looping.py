original_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
