import matplotlib.pyplot as plt

x1 = 5
y1 = 6
x2 = 8
y2 = 12

m = (y2 - y1) / (x2 - x1)

x_list = [x1]
y_list = [y1]

while x1 < x2 or y1 < y2:
    if m > 1:
        x1 = x1 + (1 / m)
        y1 = y1 + 1
    elif m < 1:
        x1 = x1 + 1
        y1 = y1 + m
    else:
        x1 = x1 + 1
        y1 = y1 + 1

    x_list.append(round(x1))
    y_list.append(round(y1))

   
    print("X =", x1, "Y =", y1, "Plot =", round(x1), round(y1))

plt.plot(x_list, y_list, marker="o")
plt.show()