a = 1
b = 1
c = 0
d = 0
e = 1

n = 1
q =((n+3)+(n+1)+n) % 2
qz = ((d+1) + b + a ) % 2
#print(qz)

for i in range(40):
    q = ((i + 3) + (i + 1) + i) % 2
    print(q)





#
# def iterative_factorial(n):
#     result = 1
#     for i in range(2,n+1):
#         result *= i
#     return result
#
#
# for i in range(40):
#     print(i, iterative_factorial(i))