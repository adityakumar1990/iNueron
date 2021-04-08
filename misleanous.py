def power_of_digit(input,power_digit):
    n=1
    while True:
        if input == power_digit **n:
            return f"Power of {power_digit}" , n
        elif input < power_digit ** n :
            return None
        else:
            n=n+1
#driver code

##print(power_of_digit(19683,3))

def perfect_square(input_num):
    import math
    squrt_root=math.sqrt(input_num)
    if input_num == squrt_root** 2:
        return "Perfect Square"
    else:
        return None

#driver code
#print(perfect_square(26))

#power of any number

def power_of_any_num(input_num):
    power_digit=[]
    for i in range(2,input_num):
        n=1

        while True:
            if input_num== i **n :
                power_digit.append(i)
                break
            elif input_num < i **n :
                break
            else:
                n=n+1
    return power_digit

#driver code
#print(power_of_any_num(16))

##find mssing number from the list

def find_missing(input_list):
    input_list.sort()
    missing_element=[]
    for e in range(input_list[0],input_list[-1]+1):
        if e not in input_list:
            missing_element.append(e)
        else:
            ...
    return missing_element

# driver code
#print(find_missing([0,1,2,4,5,8,9]))


#Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
# [-1,0,1,2,-1,-4]
def find_3_element_sum(input_list):
    m=0
    new_list=[]
    while m < len(input_list)-2:
        n=m+1
        while n < len(input_list)-1:
            p=n+1
            while p < len(input_list):
                new_list.append([input_list[m],input_list[n],input_list[p]])
                p=p+1
            n=n+1
        m=m+1
    print(new_list)

    zero_sum_list=[]
    for i in new_list:
        sum=0
        for j in i:
            sum=sum+j
        if sum ==0:
            zero_sum_list.append(i)

    return zero_sum_list

# driver code
print(find_3_element_sum([-1,0,1,2,-1,-4]))


    


