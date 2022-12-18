import math

import numpy as np

import first_part


def sum_m(x_i_list, a, b, m):
    result = 0
    for i in range(m):
        result += math.pow(x_i_list[i], a) * math.pow(x_i_list[i], b)

    return result


def create_matrix(n, x_i_list, m):
    cf = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            elem = sum_m(x_i_list, i, j, m + 1)
            cf[i, j] = elem

    return cf


def f_res(n, m, x_i_list, f_i_list):
    vec = []
    for i in range(n + 1):
        sum_f = 0
        for j in range(m + 1):
            sum_f += math.pow(x_i_list[j], i) * f_i_list[j]
        vec.append(sum_f)

    return vec


def phi(x, n, x1):
    res_phi = 0
    for i in range(n + 1):
        res_phi += x[i] * math.pow(x1, i)

    return res_phi


def fault(m, x, n, x_i_list, f_i_list):
    sum_fault = 0
    for i in range(m+1):
        sum_f = phi(x, n, x_i_list[i]) - f_i_list[i]
        sum_fault += math.pow(sum_f, 2)

    return math.sqrt(sum_fault)


def start_fourth_part(alpha_i, h, m):
    print("FOURTH PART! FOURTH PART! FOURTH PART! FOURTH PART! FOURTH PART! FOURTH PART! FOURTH PART! FOURTH PART! \n")
    n = 5
    x_i_list = first_part.find_x_i_list(alpha_i, h, m)
    f_i_list = first_part.find_f_i_list(alpha_i, x_i_list, m)
    print(x_i_list)
    a = create_matrix(n+1, x_i_list, m)
    print(a)
    vector = f_res(n, m, x_i_list, f_i_list)
    b = np.array(vector).reshape(6, 1)

    print(b)

    x = np.linalg.lstsq(a, b, rcond=None)[0]

    print(x)

    x1 = first_part.get_x1(x_i_list, h)
    x2 = first_part.get_x2(x_i_list, h, m)
    x3 = first_part.get_x3(x_i_list, h, m)

    print("phi1 = ", phi(x, n, x1))
    print("phi2 = ", phi(x, n, x2))
    print("phi3 = ", phi(x, n, x3))

    fault_f = fault(m, x, n, x_i_list, f_i_list)
    print("fault = ", fault_f)

    first_part.comparison_values4(alpha_i, x_i_list, f_i_list, h, m, x, n)
