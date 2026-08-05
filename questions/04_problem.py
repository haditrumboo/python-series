def is_prime(n):
    for i in range(1,n):
        if i % 2 == 0:
            print(i)
        else:
            print(f"odd {i}")


is_prime(100)