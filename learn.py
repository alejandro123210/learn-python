array_to_sort = [415124, 10, 5, 13, 12, 42, 52, 346, 486, 3, 52, 5743, 754, 86, 53, 46, 57, 96]
should_stop = False
while should_stop == False:
    should_stop = True
    for back_index in range(len(array_to_sort) -1):
        front_index = back_index + 1
        if array_to_sort[back_index] > array_to_sort[front_index]:
            print(array_to_sort)
            array_to_sort[front_index],array_to_sort[back_index] = array_to_sort[back_index], array_to_sort[front_index]
            should_stop = False
