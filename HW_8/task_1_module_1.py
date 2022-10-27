import math


def square1(a, b):
    square_rec = a * b
    return square_rec


def square2(h, a):
    square_tr = 0.5 * h * a
    return square_tr


def square3(r):
    square_cir = math.pi * math.pow(r, 2)
    return square_cir
