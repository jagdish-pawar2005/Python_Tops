# iterator is the concept of iterating over a collection of elements one by one.
# l=[10,20,30,40]

# k= iter(l)
# print(next(k))
# print(next(k))

# print("ajkbfbawkf")
# print("5453")

# print(next(k))
# print(next(k))



# A generator is a special type of iterator that is defined using a function and the 'yield' statement.
def test():
    yield "hello"
    yield "test"

k= test()
print(next(k))
print(next(k))