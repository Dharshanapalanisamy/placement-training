n= int(input())
if n <= 1:
    print(f"{n} is not a prime number.")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} prime number.")
    else:
        print(f"{n}  not a prime number.")
