def sort_nested_list(input_list):
    sorted_list=[]
    for e in input_list:

        if type(e) not in (str,int,float):

            ##print(e)
            #sorted_list.append(e.sort(reverse=True))
            ##This will not work because e.sort(reverse=True) return none and none will be appended
            e.sort(reverse=True)
            sorted_list.append(e)
            # this will work since sort in in-place-method
        else:
            sorted_list.append(e)
    return sorted_list

#driver code

print( sort_nested_list([[4, 1, 6], [7, 8], [4, 10, 8]]))