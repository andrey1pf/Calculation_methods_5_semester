import math

import first_part
import numpy as np


def factorial(n):
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def t_p(n, t):
    if n == 0:
        return 1

    result = 1
    for i in range(0, n):
        result *= t-i

    return result


def formula_newton(n, table, x, h, x0):
    result = 0
    t = (x - x0)/h
    for i in range(0, n):
        result += (table[0, i] / factorial(i)) * t_p(i, t)

    return result


def create_finite_difference_table(n, f_i_list):
    cf = np.zeros([n, n])
    cf[:, 0] = f_i_list[:4]

    for i in range(1, n):
        for j in range(0, n - i):
            cf[j, i] = cf[j + 1, i - 1] - cf[j, i - 1]

    return cf


def frac(t, n):
    result = 1
    for i in range(n+1):
        result *= t - i

    return result/factorial(n+1)


def r_n(h, n, x, x0):
    t = (x - x0) / h
    return math.pow(h, n+1) * frac(t, n) * 1.1920316953308


def start_second_part(alpha_i, h, n):
    print("SECOND PART! SECOND PART! SECOND PART! SECOND PART! SECOND PART! SECOND PART! SECOND PART! SECOND PART! \n")
    k = 3
    x_i_list = first_part.find_x_i_list(alpha_i, h, n)
    f_i_list = first_part.find_f_i_list(alpha_i, x_i_list, n)
    x = first_part.get_x1(x_i_list, h)
    table = create_finite_difference_table(k + 1, f_i_list)
    print(table)
    print(formula_newton(k + 1, table, x, h, x_i_list[0]))
    print(r_n(h, k, x, x_i_list[0]))
