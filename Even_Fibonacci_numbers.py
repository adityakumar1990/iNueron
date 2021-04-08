## dispaly top 10 fibonacci sequence element
import datetime

print(datetime.datetime.now())
def counter(value):
    series=[0,1]
    output=[]
    for i in range(1,value+1):
        if i == 1:
            output.extend(series[0:1])
        elif i == 2:
            output.extend(series[1:2])
        else:
            series.extend([series[i-3]+ series[i-2]])
            output.append(series[i-2]+ series[i-1])
    return output

# driver code
print(counter(100))

print(datetime.datetime.now())

