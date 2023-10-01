import math

from sympy import Eq, symbols


def delta(first, last):
    return last - first


def k(x1, x2, y1, y2):
    return delta(y1, y2)/delta(x1, x2)


def m(k, x, y):
    return k*(x)-y


def linear(k, m):
    x = symbols('x')
    return Eq(k*x+m, 0)
    pass


def pq_form(p, q, div=1):
    p = p/div
    q = q/div
    formula = math.sqrt((p/2) ** 2-q)
    pos = -(p/2) + formula
    neg = -(p/2) - formula
    return pos, neg


def avvikelse(num_array, medelval):
    new_arr = []
    for num in num_array:
        new_arr.append(num - medelval)
    return new_arr


def standardavvikelse(num_array, medelval):
    standardavvikelsen = 0
    for i in range(0, len(num_array)):
        num_array[i] = (num_array[i] - medelval)**2
        standardavvikelsen += num_array[i]

    return math.sqrt(standardavvikelsen/len(num_array)), standardavvikelsen, num_array


vikt = [19, 28, 32, 69, 82]
medelval = 46

print(avvikelse(vikt, medelval))
print(standardavvikelse(vikt, medelval))
