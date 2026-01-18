from subprocess import list2cmdline

lis1=["sudipto","shojib","raihan"]
list2=[6,7,8,9,10]
list3=["A","B","C","D","E","F"]

list4=lis1+list2
print(list4)

list5=list4.copy()
print(list5)

list2.append(list3)
list6=list2
print(list6)

list3.extend(list2)
list7=list3
print(list7)

