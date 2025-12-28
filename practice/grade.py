# mark = 85
mark = int(input('Enter the mark:'))

if mark >=90 and mark <=100:
    grade='A'
elif mark >=70 and mark <90:
    grade='B'
elif mark >=50 and mark <70:
    grade='C'
elif mark >=35 and mark <50:
    grade='D'
elif mark >=0 and mark <35:
    grade='F'
else:
    grade='invalid markd'

print("Grade:", grade)