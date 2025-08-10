number=int(input("Enter your range number:"))
sum=0
"""
0+2+4+6+.......+n
for s in range(0,number+1,2):
    sum=sum+s
print(sum)
"""
#4+8+12+.......+n
for s in range(0,number+1,4):
    sum=sum+s
print(sum)
