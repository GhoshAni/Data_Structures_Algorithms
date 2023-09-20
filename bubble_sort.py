import numpy as np
def bubble_sort(list):
    unsorted_untill_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        unsorted_untill_index = len(list) - 1
        for i in range(unsorted_untill_index):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i+1], list[i]
                sorted = False
        unsorted_untill_index -= 1
    return list 

print(bubble_sort([65, 45, 55, 36, 25, 15, 10]))      
       
