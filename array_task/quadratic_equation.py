import math

a = float(input("Insert coefficient a: "))
b = float(input("Insert coefficient b: "))
c = float(input("Insert coefficient c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / 2 * a
    root2 = (-b - math.sqrt(discriminant)) / 2 * a
else:
    root1 = complex((-b / (2 * a)), math.sqrt(-discriminant) / (2 * a))
    root2 = complex((-b / (2 * a)), -math.sqrt(-discriminant) / (2 * a))

if discriminant > 0:
    print("Roots are real and different: {} and {}".format(root1, root2))
elif discriminant == 0:
    print("Roots are real and same: ", root1)
else:
    print("Roots are complex: {}  and {}".format(root1, root2))
