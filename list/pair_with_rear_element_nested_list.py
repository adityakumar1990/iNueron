def pairing_rear_element(input_list):
    pair_list=[]
    for e in input_list:
        for j in e[:-1]:
            pair_list.append([j,e[-1]])
    return pair_list


# driver code

print(pairing_rear_element([[4, 5, 6,7,0], [2, 4, 5], [6, 7, 5]]))
