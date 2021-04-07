def random(input_list):
    import random
    extended_list=[]
    for e in input_list:
        if type(e) not in (int,str,float):
            extended_list.extend(e)
        else:
            extended_list.append(e)
    random_index=random.randrange(0,len(extended_list)-1)
    return extended_list[random_index]

#driver code

print(random([[1,2,3],[10,20,30],[100,200,300],[1000,2000,3000,4000],[-1,-2,-3]]))