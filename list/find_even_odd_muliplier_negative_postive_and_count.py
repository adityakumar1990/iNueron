def find_count(input_list,tag):
    even_list=[]
    odd_list=[]
    multiplier_list=[]
    if tag=='even':
        for e in input_list:
            if e %2 ==0:
                even_list.append(e)
        return even_list,f"Total no of {tag} elements are :---",len(even_list)
    elif tag=="odd":
        for e in input_list:
            if e%2 !=0:
                odd_list.append(e)
        return odd_list, f"Total no of {tag} elements are :---", len(odd_list)
    elif "multplier_of_" in tag:
        multiplier=tag.split("multplier_of_")
        for e in input_list:
            if e % int(multiplier[1])==0:
                multiplier_list.append(e)
        return multiplier_list, f"Total no of {tag} elements are :---", len(multiplier_list)
    else:
        return "Check the parameters"

#Driver code
print(find_count([0,1,2,3,4,5,6,7,8,9,10],"multplier_of_3"))