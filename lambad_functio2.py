import functools
# def square(x):
#     print(x*x)
# square(5)

# square=lambda x:x*x
# # print(square(4))
# result=square(4)
# print(result)

# add=lambda a,b:a+b 
# print(add(5,6))

# ভুল: students=[('Rahim,60')] -> এটি একটি স্ট্রিং
# সঠিক: students=[('Rahim', 60)] -> এটি একটি টুপল

# students = [('Rahim', 65), ('karim', 60), ('Fahim', 70)]

# sort_student = sorted(students, key = lambda x: x[1])

# print(sort_student)

num=[1,2,3,4,5]
result=list(map(lambda x:x*x,num))
print(result)

even=list(filter(lambda x:x%2==0,num))
print(even)

sum=functools.reduce(lambda x,y:x+y,num)
print(sum)

