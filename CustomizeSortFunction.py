def myfunction(n):
    return abs(n-50)
n=[100,10,20,30,50]
n.sort(key=myfunction)
print(n)