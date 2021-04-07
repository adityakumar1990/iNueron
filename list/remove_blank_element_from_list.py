"""
Issue with this code :- I am interating through  a list and removing the elements from the same
list & hence while iterating it escaping some indice and there are 2 ways to automate it by removing the
for loop since we cannot reset the index value to 0 and ask for loop to interate so while loop can be
used or else append only non-empty element into the new list

"""
def remove_blank_element(input_list):
    no_empty_element_list=[]
    for e in input_list:
        if type(e) == int or type(e) ==float:
            no_empty_element_list.append(e)
        elif len(e) !=0:
            no_empty_element_list.append(e)
        else:
            ...

    return no_empty_element_list

#Driver code
print(remove_blank_element([1,'',(),(),[],[1,2,3],{},(1),(2,),33.23]))