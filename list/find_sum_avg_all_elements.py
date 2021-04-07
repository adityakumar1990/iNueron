def sum_avg_of_elements(input_list):
    counter=0
    sum_element=0
    for e in input_list:
        if type(e)==int or type(e)==float:
            sum_element=sum_element+e
            counter=counter+1
    return sum_element, sum_element/counter

#Driver Code

print(sum_avg_of_elements([1,2,3,4,5,6,7,8,9,10,'a','b','c',10.23]))