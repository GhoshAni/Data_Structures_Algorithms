def find_largest_number(num_list):
    largest_num = num_list[0]
    for i in range(len(num_list)):
        if num_list[i] > largest_num:
            largest_num = num_list[i]
            i += 1
    return largest_num

print(find_largest_number([55, 34, 56, 78, 80, 12, 160]))

