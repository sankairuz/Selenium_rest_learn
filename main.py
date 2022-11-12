def get_max_index(numbers):
    max_index = 0
    max_value = numbers[-1] 

    for index, value in enumerate(numbers, 1): 
        if index > max_index: 
            max_index = index
            max_value = value

    return max_value