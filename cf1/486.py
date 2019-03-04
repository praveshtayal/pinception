# Problem ID: 486 Total Salary
l = input().strip().split(' ')
basic=int(l[0])
grade=l[1]
if(grade=='A'):
    allow = 1700
elif(grade == 'B'):
    allow = 1500
else:
    allow = 1300
salary=round(1.59*basic + allow)
print(salary)
