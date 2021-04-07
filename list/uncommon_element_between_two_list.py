def uncommon_element(first_list,second_list):
    uncommon_list=[]
    for first in first_list:
        if first in second_list:
            pass
        else:
            uncommon_list.append(first)
    for second in second_list:
        if second in first_list:
            pass
        else:
            uncommon_list.append(second)
    return uncommon_list

#driver code

print(uncommon_element([[1,2],[3,4],5],[[0],[1,2],[3,6],5]))