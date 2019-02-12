# Problem ID: 487 Roots of quadratic equation
l = input().strip().split(' ')
a, b, c = (int(i) for i in l)
discriminant = (b*b) - 4*a*c
if(discriminant < 0):
  print(-1)
else:
    if(discriminant == 0):
        print(0)
    else:
        print(1)

    from math import sqrt
    discriminant = sqrt(discriminant)
    root1=round((-b+discriminant)/(2.0*a))
    root2=round((-b-discriminant)/(2.0*a))
    print(root1, root2, sep=' ')
