def max_min(input_list):
    max_element=input_list[0]
    min_element=input_list[0]
    for e in input_list:
        if e > max_element:
            max_element=e
        elif e < min_element:
            min_element=e
        else:
            pass
    return "Max element is :-- " ,max_element,"Min element is :- " ,min_element

print(max_min([0,10,200,389,46,-7,-9898,7,8,9]))