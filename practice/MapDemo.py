# map is a function which takes two arguments
# function and iterable(list,tuple,dict,set)

# syntax: map(function, iterable)

# Q1
# l=[1,2,3,4,5,6]
# result= map(lambda x : x+2,l)
# print(list(result))

# Q2
# l=[1,2,3,4]
# square = map(lambda x : x*x,l)
# print(list(square))

# Q3
# a=[1,5,4,7]
# b=[4,5,8,2]
# add = map(lambda x,y:x+y, a,b)
# print(list(add))

# Q4 convert the upper case

l=["jagdish","chetan","aashish"]
word= map(lambda x:x.upper(),l)
print(list(word))
