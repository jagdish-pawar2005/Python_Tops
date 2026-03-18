l = ["Python","java","c++","c#","javascript","html","css"]


def filter_demo(a):
    if a.startswith("j"):
        print("contains :j", a)
        return a
    

for i in range(len(l )):
    filter_demo(l[i])
