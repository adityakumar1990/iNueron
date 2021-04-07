def convert_list_into_dict(key_list,value_list):
    index=0
    dict={}
    dict_list=[]

    for k in key_list:
        lst=value_list[index::len(key_list)]
        dict[k]=lst
        index=index+1

    ##creating seprate dict for each and every group
    index=0
    while index <  len(lst):
        indivial_dict = {}
        for k in key_list:
            print(dict[k][index])
            indivial_dict[k]=dict[k][index]
        dict_list.append(indivial_dict)
        index=index+1

    return dict,"~~~~~~~~~~~~~~~~~~~~~~~~~~",dict_list


#Driver code

print(convert_list_into_dict(['name','age','gender'],['aditya',28,'M','bhanu',25,'M','tintin',3,'F']))