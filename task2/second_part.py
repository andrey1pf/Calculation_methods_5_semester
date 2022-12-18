import math
import numpy as np


def function(x):
    alpha_i = 0.4
    return alpha_i * pow(math.e, x) + (1 - alpha_i) * math.sin(x)


def ck(x):
    p = (7 / 16) * (429 * math.pow(x, 6) - 495 * math.pow(x, 4) + 135 * math.pow(x, 2) - 5)
    c = 2 / ((1 - math.pow(x, 2)) * math.pow(p, 2))
    return c


def find_result():
    xi = [-0.949107912342758, -0.741531185599394, -0.405845151377397, 0.0, 0.405845151377397, 0.741531185599394,
          0.949107912342758]
    ckl = []
    for i in range(0, 7):
        ckl.append(ck(xi[i]))

    pre_res_sum = 0
    for i in range(0, 7):
        pre_res_sum += ckl[i] * function(0.9 + xi[i] / 2)

    return pre_res_sum / 2


def error(n):
    a = (math.pow(2, 2 * n + 3)) / ((2 * n + 3) * np.math.factorial(2 * n + 2))
    b = (math.pow(np.math.factorial(n + 1), 2)) / (np.math.factorial(2 * n + 2))
    c = 1.0308101487448

    result = a * math.pow(b, 2) * c
    return result


def start_second_part():
    v = 1.476006418342949
    my_integral = find_result()
    print(my_integral)
    print("Def: ", error(6))
    print("Real: ", math.fabs(my_integral - v))
