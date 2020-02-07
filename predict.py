def predict(theta0, theta1, mileage):
    return theta0 + theta1 * mileage


def get_thetas():
    try:
        fd = open('thetas', 'r')
        line = fd.readline()
        theta0, theta1 = (float(i) for i in line.split())
        return theta0, theta1
    except:
        return 0.0, 0.0


if __name__ == "__main__":
    try:
        print("Enter car mileage:", end=" ")
        mileage = float(input())
        if mileage < 0.0:
            raise
        theta0, theta1 = get_thetas()
        print("Predicted cost:", round(predict(theta0, theta1, mileage), 2))
    except:
        print('Error!')
