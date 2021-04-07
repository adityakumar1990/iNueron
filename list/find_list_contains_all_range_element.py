def find_range_inside_list(input_list):
    input_list.sort()
    min_element=input_list[0]
    input_list.sort(reverse=True)
    max_element=input_list[1]
    flag=True
    range_list=list(range(min_element,max_element+1))
    for e in range_list:
        if e in input_list:
            flag=True and flag
        else:
            flag=False
    return flag

#Driver code

if find_range_inside_list([4,5,6,11, 7, 3, 9]):
    print("All elements of range is present in input list")
else:
    print("All elements of range is not present in input list")

