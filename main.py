# x = input("Please enter first number:\n")
# fx = float(x)
#
# y = input("Please enter second number:\n")
# fy = float(y)
#
# print(f'{x} % {y} = {fx % fy}')

# def exponentgetter(base4, pow2):
#     result = 1
#     for index in range(pow2):
#         result = result * base4
#     return result
# val6 = exponentgetter(a, b)
import math

import numpy as np
from scipy.optimize import fsolve

# Note that range(71) is not the values of 0 to 71, but the values 0 to 71.

# index = -1
# for c in range(71):
#     a = (pow(53, c) % 71)
#     index += 1
#     if a == 45:
#         print(index)
#
#
#
# base1 = 45
# exponent1 = 6
# value1 = pow(base1, exponent1)
# base2 = 53
# exponent2 = 5
# value2 = pow(base2, exponent2)
# value3 = 71
# calc = value1 / value2
# print(calc % 71)
#
# base3 = 45
# exponent3 = 5
# valueX = pow(base3, exponent3)
# base4 = 53
# exponent4 = 2
# valueY = pow(base4, exponent4)
# value9 = 71
# calc = valueX - valueY
#
# print((34*calc) % 71)
#
#
#
#
#
#
# index = -1
# for c in range(71):
#     q = ((41 * 45) + pow(53, 7)) % 71
#
#     a = (29 * c) % 71
#     index += 1
#     if a == q:
#         print(index)
#
#
#
#
#
# # print(((41*45) + pow(53,7) )% 71)
#
# y = pow(53, -5, 71)
# w = pow(45, 6)
# t = w % 71
#
# print(t * y % 71)

# v= range(100)
# for c in range(100):
#     #for d in range(100):
#     d=1
#     q=5*c + 3* d

# for x in range(0,17):
#  if (-11 + 7 * x) % 17 == 0:
#       print (x)

# y = pow (53,-1, 31)
# print (y)


from random import randrange


def MillerRabin(p):
    d = p - 1
    r = 0

    while d % 2 == 0:
        d //= 2
        r += 1
    a = randrange(2, p - 1)
    x = (a ** d) % p
    if x == 1 or x == p - 1:
        return True
    while r > 1:
        x = (x * x) % p
    if x == p - 1:
        return True
        r -= 1
    return False


print(MillerRabin(4))


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def coprime_check(x, y):
    return gcd(x, y) == 1


def calc_phi(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1, x) if coprime_check(x, y)]
        return len(n)


print(calc_phi(4304177))

print(pow(223, -1, 6336))

import math
import sympy


def pollard_calc(n):
    a = 2
    b_index = 2

    while True:

        a = (a ** b_index) % n
        print(f"b = {b_index}", f"a = {a}")

        d = math.gcd((a - 1), n)

        if d > 1:
            return d

            break

        b_index += 1


n = 4304177
num = n
ans = []

while True:
    d = pollard_calc(num)
    ans.append(d)
    r = int(num / d)
    if sympy.isprime(r):

        ans.append(r)

        break


    else:

        num = r

print("The prime factors of", n, "are", *ans)
y = 65537

prime_list = [5, 11, 13, 17, 19, 23]

qz_index = -1
for ix in prime_list:
    qz_index += 1
    print(f"{prime_list[qz_index]}", "has bit length:", math.floor((math.log2(ix)) + 1))


def hamming_weight(q):
    c = 0
    while q:
        q &= q - 1
        c += 1

    return c


print(hamming_weight(1000000))
