number=int(input("Enter your range number:"))
sum=0
#1+3+5+7+9+.......+n
for s in range(1,number+1,2):
    sum=sum+s
print(sum)