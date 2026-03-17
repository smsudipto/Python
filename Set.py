list1={"sudipto","kapil","kaushik","hori"}
list2={"shojib","raihan","shisher","sudipto"}
list3={"dulal","sagorika","JOYA","paipa"}
list4={"sudipto","kapil",}
print(list1)
print(list2)
print(list1.union(list2))
print(list1.intersection(list2))
print(list1.difference(list2))
print(list2.difference(list1))
print(list1.symmetric_difference(list2))
print(list1 | list2)
print(list1.union(list2,list3))
print(list1.union(("krishana","bolai")))
print(list1 & list2)
print(list1.issubset(list4))
print(list1.isdisjoint(list3))
print(list1.issuperset(list4))