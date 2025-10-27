list=["sudipto","kapil","kaushik","raihan","shojib"]
list1=[]

"""
for x in list:
    if "s" in x:
     list1.append(x)
print(list1)
"""
list1=[x for x in list if "s" in x]
print(list1)
list1=[x for x in list if x!="sudipto"]
print(list1)
list1=[x for x in list]
print(list1)
