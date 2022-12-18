import math

import first_part
import second_part


def tk(n):
    restk = []
    for i in range(0, n+1):
        a = ((2*i+1)/(2*n+1)) * math.pi
        restk.append(math.cos(a))

    return restk


def xk(a, b, tk, n):
    resxk = []
    for i in range(n+1):
        x = (a+b)/2 + ((b-a)/2)*tk[i]
        resxk.append(x)
    return resxk


def fault_m(n, a, b):
    m = 0.3465957706175
    x = m/(second_part.factorial(n+1))
    y = (math.pow(b-a, n+1))/(math.pow(2, 2*n+1))
    return x*y


def start_third_part(alpha_i, h, n, a, b):
    print("THIRD PART! THIRD PART! THIRD PART! THIRD PART! THIRD PART! THIRD PART! THIRD PART! THIRD PART! \n")
    list_tk = tk(n)
    list_xk = xk(a, b, list_tk, n)
    function_list_xk = first_part.find_f_i_list(alpha_i, list_xk, n)
    print(list_tk)
    print(list_xk)
    print(function_list_xk)

    x1 = first_part.get_x1(first_part.find_x_i_list(alpha_i, h, n), h)
    x2 = first_part.get_x2(first_part.find_x_i_list(alpha_i, h, n), h, n)
    x3 = first_part.get_x3(first_part.find_x_i_list(alpha_i, h, n), h, n)
    lagrange_x1 = first_part.interpolate_lagrange_polynomial(x1, list_xk, function_list_xk, n + 1)
    lagrange_x2 = first_part.interpolate_lagrange_polynomial(x2, list_xk, function_list_xk, n + 1)
    lagrange_x3 = first_part.interpolate_lagrange_polynomial(x3, list_xk, function_list_xk, n + 1)
    print(lagrange_x1)
    print(lagrange_x2)
    print(lagrange_x3)

    r_n = fault_m(n, a, b)
    print(r_n)
    print(list_xk)
    print(function_list_xk)

    x_i_list_x1 = list_xk
    f_i_list_x1 = function_list_xk
    x_i_list_x2 = list_xk
    f_i_list_x2 = function_list_xk
    x_i_list_x3 = list_xk
    f_i_list_x3 = function_list_xk
    b1 = first_part.function(alpha_i, x1)
    b2 = first_part.function(alpha_i, x2)
    b3 = first_part.function(alpha_i, x3)
    x_i_list_x1.append(x1)
    f_i_list_x1.append(b1)
    print("R_n(x*) = ", first_part.fault(x_i_list_x1, f_i_list_x1, x1))
    x_i_list_x2.pop(-1)
    f_i_list_x2.pop(-1)
    x_i_list_x2.append(x2)
    f_i_list_x2.append(b2)
    print("R_n(x**) = ", first_part.fault(x_i_list_x2, f_i_list_x2, x2))
    x_i_list_x3.pop(-1)
    f_i_list_x3.pop(-1)
    x_i_list_x3.append(x3)
    f_i_list_x3.append(b3)
    print("R_n(x***) = ", first_part.fault(x_i_list_x3, f_i_list_x3, x3))
    print()
    x_i_list = first_part.find_x_i_list(alpha_i, h, n)
    first_part.comparison_values_3(alpha_i, x_i_list, h, n, list_xk, function_list_xk)
    #fault_x1 = first_part.fault(list_xk, function_list_xk, x1)
    #fault_x2 = first_part.fault(list_xk, function_list_xk, x2)
    #fault_x3 = first_part.fault(list_xk, function_list_xk, x3)
    #print(fault_x1)
    #print(fault_x2)
    #print(fault_x3)
