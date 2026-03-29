name=["sudipto","shojib","kaushik","kapil","raihan"]
def generator():
    yield("sudipto")
    print("Hum Ok!!")
    yield("shojib")
    print("Hum Ok!!")
    yield("kapil ")
    yield("raihan")

a=generator()
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print(type(a))