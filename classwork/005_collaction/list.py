# l =[1,2,3,4,5,5,6,6.50,"jack",True] 
# print(l)
# print(len(l))
# print(type(l)) #find which type of collaction

# k=list((12,547))
# print(k)

# access list
# l = ["python","java","php","c","java"]
# print(l[0])
# print(l[-1])
# print(l[1:3])
# print(l[::-1])
# print(l["java" in l])  #in is identity operator

#change list itme

# l[0] = "React"
# l[1:3] = [""]
# l.insert(2,"XYZ")
# l.append("XYZ")
# k = [10,20,30]
# l.extend(["A","B"])
# l.extend(k)

# remove list item
# l = ["python","java","php","c","java"]
# l.remove("java")
# l.pop()
# l.pop(2)
# l.clear()
# del l

# looping in list
l=[10,20,30,40,50]
# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i = 0 
# while i<len(l):
#     print(l[i])
#     i+=1

# -----------------------------------------------------------
# List1 = [1,2,3,4,5]
# print(List1)

# list2 = ["mango","banana","apple","orange"]
# print(list2)

# print(List1+list2)

# if 7 in List1 :
#     print("7 in List 1 :)")
# else:
#     print("7 is not in List1 );")

# if 'mango' in list2 :
#     print('mango is available in list2 ')
# else:
#     print('mango is not available list2 ')

# print('length of list1 :',len(List1))
# print('length of list2 :',len(list2))

# print('length of both list ',len(List1+list2))

# print([1,2,3]+[4.1,5.2,6.5])
# print(['hi']*4)

# # for x in list2:
# #     print(x)

# list2.pop(1)
# print(list2)

# -----------------------------------------------------------

# shopping_list = ["bread","butter","chees","panner"]

# len = 0

# for item in shopping_list:
#     len+=1

# # print(len)

# -----------------------------------------------------------

# add element in existing/created list

# l=[]

# l.append("mango")
# l.append("banana")
# l.append("orange")

# l.pop(0) #pop is deleted list element through indexed

# print(l)

# ------accept data from user -------
# l = []

# for i in range(1,3):
#     name = input("enter name : ")
#     l.append(name)

# print(l)

# ----------even/odd for uuser input----------------

# even_list = []
# odd_list = []

# for i in range(1,5):
#     num=int(input("enter the number: "))

#     if num % 2==0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# print("even numbers:",even_list)
# print("odd numbers :",odd_list)

# ------vowal program------

# vowal_list = []

# name = input("enter your name :").lower()

# for c in name:
#     if c in "aeiou":
#         vowal_list.append(c)
    
# print(f"{name} contains {len(vowal_list)} vowals")

l = [10,20,30]

# l.insert(0,10001) #adding the list
# print(l)

# print(l.count(10)) #count the list element index
