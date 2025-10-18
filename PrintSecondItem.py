list=["sudipto","kapil","kaushik","nemai","raihan","shojib"]
print(list)
print("second number is:",list[2])
print("Last number is:",list[-1])
print("Last second number is:",list[-2])
print(" number is:",list[:3])#Starting number is "sudipto" and end number is "kaushik"
print(" number is:",list[4:])#print starting shojib and end the last value
print(" number is:",list[2:5])#starting index 2 and end index 4
print("number is:",list[-5:-2])#[-2:-5] is not possible .always print left to right

if "sudipto" in list:
     print("yes sudipto is present inside in this list ")