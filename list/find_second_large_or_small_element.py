def find_nth_ordered_element(input_list,nth_occurnace,tag):
    '''

    :param input_list: Driver code will have complete list
    :param nth_occurnace: Integer like 2 then 2nd largest etc
    :param tag: large or small
    :return:  If tag is Large then find nth largest , if tag is small then find nth smallest
    '''
    input_list=list(set(input_list)) # This code is added to remmove duplicate & to apply sort changed to list
    if tag == 'large':
        input_list.sort(reverse=True)
        try:
            return input_list[nth_occurnace-1]
        except:
            return f"{nth_occurnace} {tag}est not present in input list"
    elif tag == 'small':
        input_list.sort(reverse=False)
        try:
            return input_list[nth_occurnace-1]
        except:
            return f"{nth_occurnace} {tag}est not present in input list"
    else:
        return "Check the input parametrs in doc string !!!"

#Driver code

print(find_nth_ordered_element([-1,-1,-1,-1,1,1,0,3,4,5,6,7,-1],7,'large'))