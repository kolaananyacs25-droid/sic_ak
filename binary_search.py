def binary_search(search_element, input_list):
    low = 0 
    high = len(input_list) - 1
    while low <= high:
        mid_index = (low + high) // 2
        if search_element == input_list[mid_index]:
            return mid_index
        elif search_element < input_list[mid_index]:
            high = mid_index - 1
        else:
            low = mid_index + 1 