import matplotlib.pyplot as plt

def draw_midpoint_circle(r):
    x = 0
    y = r
    p = 1 - r
    all_points = []

    while x <= y:

        if p < 0:
            x = x + 1
            p = p + 2 * x + 1
        else:
            x = x + 1
            y = y - 1
            p = p + 2 * x - 2 * y + 1

        all_points.append((x, y))
        all_points.append((y, x))
        all_points.append((x, -y))
        all_points.append((y, -x))
        all_points.append((-x, -y))
        all_points.append((-y, -x))
        all_points.append((-x, y))
        all_points.append((-y, x))

    plot_x, plot_y = zip(*all_points)

    plt.figure(figsize=(6,6))
    plt.scatter(plot_x, plot_y, color='green')
    plt.gca().set_aspect('equal')
    plt.show()

draw_midpoint_circle(20)