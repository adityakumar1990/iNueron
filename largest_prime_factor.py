def largest_prime_factor(input):
    prime_list=[]
    for e in range(1,input+1):
        if e in (1,2):
            flag=True
        for j in range(2,e):
            if e % j == 0:
                flag=False
                break
            else:
                flag=True
        if flag:
            if input % e ==0:
                prime_list.append(e)
            prime_list.sort(reverse=True)
    return prime_list[0]

# driver code

print(largest_prime_factor(600000),end="\n")