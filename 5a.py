index = 0
for i in range(1, 1001, 1):
    index += 1
    calc = pow(3, i, 17)
    if calc == 1:
        print(index)
        break


index_2 = 0
for qx in range(1, 16, 1):
    index_2 += 1
    calc = pow(3, qx, 17)
    if calc == 7:
        print(index_2)
        break
