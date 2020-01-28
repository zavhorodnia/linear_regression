import csv
import matplotlib.pyplot as plt
#km, price
# x    y


theta0 = 0.0 # b
theta1 = 0.0 # a
learning_rate = 0.1


# y = ax + b
def estimate_price(miles):
    global theta0, theta1
    return theta0 + theta1 * miles


def cost_function():
    global normalized_data, m
    cost = 0.0
    for x, y in normalized_data:
        cost += (estimate_price(x) - y) ** 2
    return cost / m


def average_theta0():
    global normalized_data, m
    avg_sum = 0.0
    for row in normalized_data:
        avg_sum += estimate_price(row[0]) - row[1]
    return avg_sum / m


def average_theta1():
    global normalized_data, m
    avg_sum = 0.0
    for row in normalized_data:
        avg_sum += (estimate_price(row[0]) - row[1]) * row[0]
    return avg_sum / m


def train():
    global theta0, theta1, data
    cost = 0
    prev_cost = 1
    while abs(prev_cost - cost) > float(0.0003):
        prev_cost = cost
        theta0 -= learning_rate * average_theta0()
        theta1 -= learning_rate * average_theta1()
        cost = cost_function()
    print(prev_cost)


def denormalize():
    global delta, theta1
    theta1 /= delta


def normalize():
    global data, min_x, delta
    return list(map(lambda i: (((i[0] - min_x) / delta), i[1]), data))


if __name__ == "__main__":
    with open('data.csv', 'r') as fd:
        reader = csv.reader(fd)
        next(reader, None)
        data = list(map(lambda i: (float(i[0]), float(i[1])), map(tuple, reader)))
    m = len(data)
    max_x = max(data, key= lambda i : i[0])[0]
    min_x = min(data, key= lambda i : i[0])[0]
    delta = max_x - min_x
    normalized_data = normalize()
    train()
    print(theta0, theta1)
    denormalize()
    plt.scatter(list(map(lambda i: i[1], data)), list(map(lambda i: i[0], data)))
    xs = list(map(lambda i: i[0], data))
    plt.plot(list(map(lambda i: estimate_price(i), xs)), xs)
    plt.show()
    print(theta0, theta1)
    print(estimate_price(240000.0))
