nams_list=["sudipto","kapil","kaushik","raihan","shojib"]
new_list=[]
"""
found=False
for i in nams_list:
    if "a" in i:
        print(i)
        found=True
if not found:
        print("a is not in list")
"""
for i in nams_list:
    if "a" in i:
        new_list.append(i)

print(new_list)
