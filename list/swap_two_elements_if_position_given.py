def swap_element(input_list,first_position,second_position):
    if type(input_list)==list:
        pass
    else:
        return "Input provided by user is not list"
    try:
        first_element=input_list[first_position]
    except:
        first_element = input_list[0]
        first_position=0
    try:
        second_element=input_list[second_position]
    except:
        second_element = input_list[-1]
        second_position=-1
    input_list[first_position]=second_element
    input_list[second_position]=first_element
    return input_list

#driver code
print(swap_element(123456,12,15))