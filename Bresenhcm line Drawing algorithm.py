import matplotlib.pyplot as plt
x1=int(input("inter your input:"))
y1=int(input("inter your input:"))
x2=int(input("inter your input:"))
y2=int(input("inter your input:"))
dx=x2-x1
dy=y2-y1
pk=2*dy-dx

if abs(dx)>abs(dy):
  steps=abs(dx)
else:
  steps=abs(dy)

x_score=[]
y_score=[]

i=0
while steps>i:
  i=i+1
  if pk>=0:
    x1=x1+1
    y1=y1+1
    pk=pk+2*dy-2*dx
  elif pk<0:
    x1=x1+1
    y1=y1
    pk=pk+2*dy

  x_score.append(x1)
  y_score.append(y1)
  print("x1,y1:","(",x1,",",y1,")")

plt.plot(x_score, y_score, color="red", marker="o")
plt.xlabel("X-axis") # এখানে xlevel এর বদলে xlabel হবে04
plt.ylabel("Y-axis")
plt.title("Bresenham Line Drawing Algorithm")
plt.grid(True)
plt.show()

