import math
import matplotlib.pyplot as plt


def function(x, y):
    result = y/x + x * (0.4*math.pow(math.e, x)+0.6*math.cos(x))
    return result


def find_y(x):
    y = [0.3321523537766793688]

    for i in range(10):
        ny = y[i] + 0.1*function(x[i], y[i])
        y.append(ny)

    return y


def euler(x):
    y = find_y(x)
    return y


def get_phi0(h, x, y):
    return h * function(x, y)


def get_phi1(h, x, y):
    a = 2/3
    b = 2/3
    return h * function(x + a*h, y + b*get_phi0(h, x, y))


def find_y_rk(x, a, h):
    y = [0.3321523537766793688]

    for i in range(10):
        ai = (1-a)*get_phi0(h, x[i], y[i]) + a*get_phi1(h, x[i], y[i])
        ny = y[i] + ai
        y.append(ny)

    return y


def runge_kutta(x):
    a = 3/4
    h = 0.1
    y = find_y_rk(x, a, h)
    return y


def real(x):
    y = []
    for i in range(11):
        a = x[i]*(0.4 * math.pow(math.e, x[i]) + 0.6*math.sin(x[i]) - 1.38778 * math.pow(10, -16))
        y.append(a)

    return y


def error_true_2(euler_y, rk_y, real_y):
    e1 = []
    r1 = []
    for i in range(len(euler_y)):
        e1.append(math.fabs(real_y[i] - euler_y[i]))
        r1.append(math.fabs(real_y[i] - rk_y[i]))

    return e1, r1


def start_first_part():
    x = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]
    euler_y = euler(x)
    rk_y = runge_kutta(x)
    real_y = real(x)

    e1, e2 = error_true_2(euler_y, rk_y, real_y)
    print(e1)
    print(e2)

    plt.plot(x, euler_y, 'r', label='Euler')
    plt.plot(x, rk_y, 'g', label='Runge-Kutta')
    plt.legend(loc='upper left')
    plt.show()

    plt.plot(x, real_y, 'b', label='Real')
    plt.legend(loc='upper left')
    plt.show()
