from sys import argv
import argparse
import csv
import numpy as np
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
    global standartized_xs, prices, m
    cost = 0.0
    for miles, price in zip(standartized_xs, prices):
        cost += (estimate_price(miles) - price) ** 2
    return cost / m


def average_theta0():
    global standartized_xs, prices, m
    avg_sum = 0.0
    for miles, price in zip(standartized_xs, prices):
        avg_sum += estimate_price(miles) - price
    return avg_sum / m


def average_theta1():
    global standartized_xs, prices, m
    avg_sum = 0.0
    for miles, price in zip(standartized_xs, prices):
        avg_sum += (estimate_price(miles) - price) * miles
    return avg_sum / m


def train(args):
    global theta0, theta1
    cost = 0
    prev_cost = 1
    while abs(prev_cost - cost) > float(0.0003):
        prev_cost = cost
        theta0 -= learning_rate * average_theta0()
        theta1 -= learning_rate * average_theta1()
        cost = cost_function()
    if args.mse:
        print("Mean squared error:", cost)



def restore_thetas(avg, std):
    global theta0, theta1
    theta0 -= (theta1 * avg / std)
    theta1 /= std


def standartize(xs):
    avg = np.average(xs)
    std = np.std(xs)
    return avg, std, list(map(lambda x: (x - avg) / std, xs))


def read_csv(filename):
    try:
        with open(filename, 'r') as fd:
            reader = csv.reader(fd)
            next(reader, None)
            mileages = []
            prices = []
            for row in reader:
                mileages.append(float(row[0]))
                prices.append(float(row[1]))
        return np.array(mileages), np.array(prices), len(mileages)
    except:
        print("Error reading data file")
        exit(0)


def write_thetas():
    global theta0, theta1
    try:
        with open ('thetas', 'w') as fd:
            fd.write(' '.join(map(str, [theta0, theta1])))
    except:
        print("Error writing thetas")
        exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', action='store', help='csv file with data for training')
    parser.add_argument('-m', '--mse', help='mean squared error', default='False', action='store_true')
    parser.add_argument('-d', '--display-graph', help='algorithm visualization', default='False', action='store_true')
    args = parser.parse_args()
    mileages, prices, m = read_csv(args.file)
    avg, std, standartized_xs = standartize(mileages)
    train(args)
    restore_thetas(avg, std)
    write_thetas()
    if args.display_graph:
        plt.scatter(mileages, prices)
        plt.plot(mileages, list(map(lambda i: estimate_price(i), mileages)), color='r')
        plt.xlabel('mileage')
        plt.ylabel('price')
        plt.show()