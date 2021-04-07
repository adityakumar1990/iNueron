def swap_first_last_element(lst):
    first_element=lst[0]
    last_element=lst[-1]
    lst[0]=last_element
    lst[-1]=first_element
    return lst

#driver code
print(swap_first_last_element([1,2,3,4,5,6,7,8,9,0]))