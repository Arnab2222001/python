def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

prime_list = prime_numbers(50)
print(prime_list)