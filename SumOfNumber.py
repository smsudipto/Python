
number=int(input("Enter your range number:"))
sum=0
"""
1+2+3+4.......+n
for s in range(1,number+1,1):
    sum=sum+s
print(sum)
"""
#1^2+2^2+3^3+4^4.......+n
for s in range(1,number+1,1):
    sum=sum+s*s
print(sum)
