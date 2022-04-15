import numpy as np


def fn(x):
    return x

def integrate1(fn, xmin, xmax, N):
    dx = (xmax - xmin) / N
    eps = 0.01 * dx
    area = 0
    # area_trapezoid = base * (h1 + h2) / 2
    for x in np.arange(xmin, xmax - eps, dx):
        area += dx * (fn(x) + fn(x + dx)) / 2
    return area

def integrate2(fn, xmin, xmax, N):
    dx = (xmax - xmin) / N
    eps = 0.01 * dx
    area = 0
    # area_trapezoid = base * (h1 + h2) / 2
    for x in np.arange(xmin, xmax - eps, dx):
        area += (fn(x) + fn(x + dx))
    area = area * dx / 2
    return area

def integrate3(fn, xmin, xmax, N):
    dx = (xmax - xmin) / N
    eps = 0.01 * dx
    area = 0
    # area_trapezoid = base * (h1 + h2) / 2
    for x in np.arange(xmin, xmax + eps, dx):
        area += fn(x)
    area = area * 2 - fn(xmin) - fn(xmax)
    area = area * dx / 2
    return area

print(integrate1(fn, 1, 4, 3))
print(integrate2(fn, 1, 4, 3))
print(integrate3(fn, 1, 4, 3))