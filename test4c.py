dll_index = 0


for i in range(27):
  print(pow(i,547, 40633))

# Function to find the gcd of two
# integers using Euclidean algorithm
# def gcd(p, q):
#     if q == 0:
#         return p
#
#     return gcd(q, p % q)
#
#
# # Function to find the
# # lcm of two integers
# def lcm(p, q):
#     return p * q / gcd(p, q)
#
#
# # Function implementing extended
# # euclidean algorithm
# def egcd(e, phi):
#     if e == 0:
#         return (phi, 0, 1)
#     else:
#         g, y, x = egcd(phi % e, e)
#         return (g, x - (phi // e) * y, y)
#
#
# # Function to compute the modular inverse
# def modinv(e, phi):
#     g, x, y = egcd(e, phi)
#     return x % phi
#
#
# # Implementation of the Chinese Remainder Theorem
# def chineseremaindertheorem(dq, dp, p, q, c):
#     # Message part 1
#     m1 = pow(c, dp, p)
#
#     # Message part 2
#     m2 = pow(c, dq, q)
#
#     qinv = modinv(q, p)
#     h = (qinv * (m1 - m2)) % p
#     m = m2 + h * q
#     return m
#
#
# # Driver Code
# p = 9817
# q = 9907
# e = 65537
# c = 36076319
# d = modinv(e, lcm(p - 1, q - 1))
#
# dq = pow(d, 1, q - 1)
# dp = pow(d, 1, p - 1)
#
# chineseremaindertheorem(dq, dp, p, q, c)
