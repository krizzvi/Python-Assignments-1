def generate_primes(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes
