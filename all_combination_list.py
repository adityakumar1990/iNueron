def all_permutation_list(i,j,k,n):
    all_list=[]
    for x in range(i+1):
        for y in range(j+1):
            for z in range(k+1):
                if x+y+z== n:
                    pass
                else:
                    all_list.append([x,y,z])

    return all_list


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #driver code
    print(all_permutation_list(x,y,z,n))