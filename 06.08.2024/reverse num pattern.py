size = 5
for i in range(size):
    for j in range(i):
        print(" ", end="")
    for k in range(2 * (size - i) - 1):
        print(k+1, end="")
    print()
