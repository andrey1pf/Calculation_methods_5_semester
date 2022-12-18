import math
import matplotlib.pyplot as plt
import numpy as np

import fourth_part


def find_x_i_list(alpha_i, h, n):
    x_i_list = []
    for i in range(0, n + 1):
        x_i_list.append(alpha_i + i * h)

    return x_i_list


def function(alpha_i, x):
    return alpha_i * pow(math.e, x) + (1 - alpha_i) * math.sin(x)


def find_f_i_list(alpha_i, x_i_list, n):
    f_i_list = []
    for i in range(0, n + 1):
        x = x_i_list[i]
        f_i_list.append(function(alpha_i, x))

    return f_i_list


def get_x1(x_i_list, h):
    return x_i_list[0] + (2 / 3) * h


def get_x2(x_i_list, h, n):
    return x_i_list[int(n / 2)] + 0.5 * h


def get_x3(x_i_list, h, n):
    return x_i_list[n] - (1 / 3) * h


def interpolate_lagrange_polynomial(x, x_i_list, f_i_list, size):
    lagrange_pol = 0

    for i in range(0, size):
        basics_pol = 1
        for j in range(0, size):
            if j != i:
                basics_pol *= (x - x_i_list[j]) / (x_i_list[i] - x_i_list[j])
        lagrange_pol += basics_pol * f_i_list[i]

    return lagrange_pol


def x_point_list():
    a = np.arange(0.4, 1.4, 0.005)
    return a


def y_point_list(x_i_list, f_i_list, size):
    a = []
    x_point = x_point_list()
    for i in x_point:
        a.append(interpolate_lagrange_polynomial(i, x_i_list, f_i_list, size))

    return a, x_point


def graph_interpolate(x_i_list, f_i_list, size):
    y, x = y_point_list(x_i_list, f_i_list, size)
    plt.plot(x, y)
    plt.show()


def comparison_values_3(alpha_i, x_i_list, h, n, list_xk, list_fk):
    a11 = get_x1(x_i_list, h)
    b11 = function(alpha_i, a11)
    x_i_list_x11 = list_xk
    f_i_list_x11 = list_fk
    x_i_list_x11.append(a11)
    f_i_list_x11.append(b11)
    inter_x1 = interpolate_lagrange_polynomial(a11, x_i_list_x11, f_i_list_x11, n+1)
    a22 = get_x2(x_i_list, h, n)
    b22 = function(alpha_i, a22)
    x_i_list_x22 = list_xk
    f_i_list_x22 = list_fk
    x_i_list_x22.pop(-1)
    f_i_list_x22.pop(-1)
    x_i_list_x22.append(a22)
    f_i_list_x22.append(b22)
    inter_x2 = interpolate_lagrange_polynomial(a22, x_i_list_x22, f_i_list_x22, n+1)
    a33 = get_x3(x_i_list, h, n)
    b33 = function(alpha_i, a33)
    x_i_list_x33 = list_xk
    f_i_list_x33 = list_fk
    x_i_list_x33.pop(-1)
    f_i_list_x33.pop(-1)
    x_i_list_x33.append(a33)
    f_i_list_x33.append(b33)
    inter_x3 = interpolate_lagrange_polynomial(a33, x_i_list_x33, f_i_list_x33, n+1)
    real_x1 = function(alpha_i, get_x1(x_i_list, h))
    real_x2 = function(alpha_i, get_x2(x_i_list, h, n))
    real_x3 = function(alpha_i, get_x3(x_i_list, h, n))
    print("True error x*: ", abs(inter_x1 - real_x1))
    print("True error x**: ", abs(inter_x2 - real_x2))
    print("True error x***: ", abs(inter_x3 - real_x3))
    print()


def comparison_values4(alpha_i, x_i_list, f_i_list, h, n, x, m):
    a11 = get_x1(x_i_list, h)
    b11 = function(alpha_i, a11)
    x_i_list_x11 = x_i_list
    f_i_list_x11 = f_i_list
    x_i_list_x11.append(a11)
    f_i_list_x11.append(b11)
    inter_x1 = fourth_part.phi(x, m, a11)
    a22 = get_x2(x_i_list, h, n)
    b22 = function(alpha_i, a22)
    x_i_list_x22 = x_i_list
    f_i_list_x22 = f_i_list
    x_i_list_x22.pop(-1)
    f_i_list_x22.pop(-1)
    x_i_list_x22.append(a22)
    f_i_list_x22.append(b22)
    inter_x2 = fourth_part.phi(x, m, a22)
    a33 = get_x3(x_i_list, h, n)
    b33 = function(alpha_i, a33)
    x_i_list_x33 = x_i_list
    f_i_list_x33 = f_i_list
    x_i_list_x33.pop(-1)
    f_i_list_x33.pop(-1)
    x_i_list_x33.append(a33)
    f_i_list_x33.append(b33)
    inter_x3 = fourth_part.phi(x, m, a33)
    real_x1 = function(alpha_i, get_x1(x_i_list, h))
    real_x2 = function(alpha_i, get_x2(x_i_list, h, n))
    real_x3 = function(alpha_i, get_x3(x_i_list, h, n))
    print("True error x*: ", abs(inter_x1 - real_x1))
    print("True error x**: ", abs(inter_x2 - real_x2))
    print("True error x***: ", abs(inter_x3 - real_x3))
    print()


def comparison_values(alpha_i, x_i_list, f_i_list, h, n):
    a11 = get_x1(x_i_list, h)
    b11 = function(alpha_i, a11)
    x_i_list_x11 = x_i_list
    f_i_list_x11 = f_i_list
    x_i_list_x11.append(a11)
    f_i_list_x11.append(b11)
    inter_x1 = interpolate_lagrange_polynomial(a11, x_i_list_x11, f_i_list_x11, n+1)
    a22 = get_x2(x_i_list, h, n)
    b22 = function(alpha_i, a22)
    x_i_list_x22 = x_i_list
    f_i_list_x22 = f_i_list
    x_i_list_x22.pop(-1)
    f_i_list_x22.pop(-1)
    x_i_list_x22.append(a22)
    f_i_list_x22.append(b22)
    inter_x2 = interpolate_lagrange_polynomial(a22, x_i_list_x22, f_i_list_x22, n+1)
    a33 = get_x3(x_i_list, h, n)
    b33 = function(alpha_i, a33)
    x_i_list_x33 = x_i_list
    f_i_list_x33 = f_i_list
    x_i_list_x33.pop(-1)
    f_i_list_x33.pop(-1)
    x_i_list_x33.append(a33)
    f_i_list_x33.append(b33)
    inter_x3 = interpolate_lagrange_polynomial(a33, x_i_list_x33, f_i_list_x33, n+1)
    real_x1 = function(alpha_i, get_x1(x_i_list, h))
    real_x2 = function(alpha_i, get_x2(x_i_list, h, n))
    real_x3 = function(alpha_i, get_x3(x_i_list, h, n))
    print("True error x*: ", abs(inter_x1 - real_x1))
    print("True error x**: ", abs(inter_x2 - real_x2))
    print("True error x***: ", abs(inter_x3 - real_x3))
    print()


def split_difference_table(x_i_list, f_i_list):
    n = len(f_i_list)
    cf = np.zeros([n, n])
    cf[:, 0] = f_i_list

    for j in range(1, n):
        for i in range(n - j):
            cf[i][j] = (cf[i + 1][j - 1] - cf[i][j - 1]) / (x_i_list[i + j] - x_i_list[i])

    return cf


def fault(x_i_list, f_i_list, x):
    pr = 1
    for i in range(0, len(x_i_list) - 1):
        pr *= x - x_i_list[i]

    return pr * split_difference_table(x_i_list, f_i_list)[0][-1]


def start_first_part(alpha_i, h, n):
    x_i_list = find_x_i_list(alpha_i, h, n)
    f_i_list = find_f_i_list(alpha_i, x_i_list, n)
    print("FIRST PART! FIRST PART! FIRST PART! FIRST PART! FIRST PART! FIRST PART! FIRST PART! FIRST PART! \n")
    print()
    print("X list: ", x_i_list)
    print("F list: ", f_i_list)
    print()
    print("-----------------------------------------------")
    print()
    print("Interpolate Lagrange polynomial for x* =", get_x1(x_i_list, h), ": ",
          interpolate_lagrange_polynomial(get_x1(x_i_list, h), x_i_list, f_i_list, n))
    print("Interpolate Lagrange polynomial for x** =", get_x2(x_i_list, h, n), ": ",
          interpolate_lagrange_polynomial(get_x2(x_i_list, h, n), x_i_list, f_i_list, n))
    print("Interpolate Lagrange polynomial for x*** =", get_x3(x_i_list, h, n), ": ",
          interpolate_lagrange_polynomial(get_x3(x_i_list, h, n), x_i_list, f_i_list, n))

    #graph_interpolate(x_i_list, f_i_list, n)
    print()
    print("-----------------------------------------------")
    print()
    #print(divided_diff(x_i_list, f_i_list))
    x_i_list_x1 = x_i_list
    f_i_list_x1 = f_i_list
    x_i_list_x2 = x_i_list
    f_i_list_x2 = f_i_list
    x_i_list_x3 = x_i_list
    f_i_list_x3 = f_i_list
    a1 = get_x1(x_i_list, h)
    b1 = function(alpha_i, a1)
    a2 = get_x2(x_i_list, h, n)
    b2 = function(alpha_i, a2)
    a3 = get_x3(x_i_list, h, n)
    b3 = function(alpha_i, a3)
    x_i_list_x1.append(a1)
    f_i_list_x1.append(b1)
    print("R_n(x*) = ", fault(x_i_list_x1, f_i_list_x1, a1))
    x_i_list_x2.pop(-1)
    f_i_list_x2.pop(-1)
    x_i_list_x2.append(a2)
    f_i_list_x2.append(b2)
    print("R_n(x**) = ", fault(x_i_list_x2, f_i_list_x2, a2))
    x_i_list_x3.pop(-1)
    f_i_list_x3.pop(-1)
    x_i_list_x3.append(a3)
    f_i_list_x3.append(b3)
    print("R_n(x***) = ", fault(x_i_list_x3, f_i_list_x3, a3))
    comparison_values(alpha_i, x_i_list, f_i_list, h, n)
    print()
