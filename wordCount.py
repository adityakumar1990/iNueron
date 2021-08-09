""" We can add input/ file read function too """
mystring="I do not like it Sam I Am".split(" ")
print({ ele : mystring.count(ele)  for ele in set(mystring) })
