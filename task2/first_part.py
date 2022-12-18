import math

import second_part


def find_integral(n):
    point = 0.4
    f_i = []
    sums = 0
    h = 1 / n
    while point <= 1.4:
        f_i.append(second_part.function(point))
        point += h

    for i in range(1, n+1):
        sums += f_i[i-1]

    return h * sums


def find_n():
    n = 1
    while True:
        m = 31.9764524 * 8
        r = m / (24*n*n)
        if r <= math.pow(10, -4):
            return n
        n += 1


def start_first_part():
    n = find_n()
    print("N = ", n)
    sums = find_integral(n)
    print(sums)
    print(1.4759983968592227 - 1.476006418342948)
