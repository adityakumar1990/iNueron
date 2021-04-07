def replace_character(input_list,old_char,new_char):
    index=0
    for e in input_list:
        if old_char in e:
            input_list[index]=e.replace(old_char,new_char)
            index=index+1
        else:
            index=index+1
    return input_list


#driver code
print(replace_character(["123","aditya","kumar","wipro","tcs","integrichain","1233"],'a','A'))

