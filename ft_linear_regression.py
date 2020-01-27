import csv
#km, price

theta0 = 0.0
theta1 = 0.0
learning_rate = 0.01


def estimate_price(miles):
    return theta0 + theta1 * miles


def average_theta0():
    global data, m
    sum = 0
    for item in data:
        sum += estimate_price(item[0]) - item[1]
    return sum / m


def average_theta1():
    global data, m
    sum = 0
    for item in data:
        sum += (estimate_price(item[0]) - item[1]) * item[0]
    return sum / m


def train():
    tt0 = learning_rate * average_theta0()
    tt1 = learning_rate * average_theta1()


def denormalize(x):
    global min_x, delta
    return x * delta + min_x


def normalize():
    global data, min_x, delta
    data = list(map(lambda i: (((i[0] - min_x) / delta), i[1]), data))


if __name__ == "__main__":
    with open('data.csv', 'r') as fd:
        reader = csv.reader(fd)
        next(reader, None)
        data = list(map(lambda i: (float(i[0]), float(i[1])), map(tuple, reader)))
    m = len(data)
    max_x = max(data, key= lambda i : i[0])[0]
    min_x = min(data, key= lambda i : i[0])[0]
    delta = max_x - min_x
    normalize()
    train()
    # print(data)
    # print(denormalize(data[0][0]))
