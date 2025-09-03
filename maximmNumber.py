a=int(input("inter your input a:"))
b=int(input("inter your input b:"))
c=int(input("inter your input c:"))

if a>b and a>c:
    print("maximum number is a:",a)
elif b>a and b>c:
    print("maximum number is b:",b)
elif c>a and c>b:
    print("maximum number is c:",c)
else:
    print("the given number is equal.")