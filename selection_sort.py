array = [7, 5, 10, 2]

for i in range(len(array)):
    lowest_val_index = i
    
    for j in  range(i + 1, (len(array))):
        if array[j] < array[lowest_val_index]:
            lowest_val_index = j
    
    (array[i], array[lowest_val_index]) = (array[lowest_val_index], array[i])
print(array)