d = {"Math": 90, "Science": 85, "English": 78, "History": 88}

def test(a):
    if a[1]>85:
        return a

k = filter(lambda x: x[1] > 85, d.items())

# k = map(test, [d])

print(list(k))
