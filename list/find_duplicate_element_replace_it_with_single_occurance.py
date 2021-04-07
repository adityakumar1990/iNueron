def find_dup_keep_single_occurance(input_list):
    distinct_list=[]

    for e in input_list:
        if e in distinct_list:
            continue
        distinct_list.append(e)
    return distinct_list


#Driver Code :-

print(find_dup_keep_single_occurance([1,1,8,2,3,2,1,4,5,8,6,7,3]))



