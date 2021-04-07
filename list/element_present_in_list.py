def element_in_list(input_list,element):
    if element in input_list:
        input_list.clear()
        return "Present",input_list

    else:
        return "Not Present",input_list


#Driver Code

print(element_in_list([100,22,567,85,75],5667),end="")