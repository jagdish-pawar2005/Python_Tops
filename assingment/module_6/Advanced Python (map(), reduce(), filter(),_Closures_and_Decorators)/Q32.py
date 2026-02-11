from functools import reduce
product=[1,2,3,4,5]
result=reduce(lambda x,y:x*y,product)
print(result)