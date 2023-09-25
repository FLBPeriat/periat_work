"""
Date: 15.09.2023
Author: F. L.B. Périat
Description: Generation of primes
"""



def sieve_of_periat(included_limit: int) -> list[int]:
    """
    Get all prime numbers <= n = included_limit, by Périat method.

    Complexity:
                * O(n log n) in time
                * O(n / log n) in space

    :param included_limit: maximal value to check
    :return: list of ordered prime numbers
    """
    next_multiples: dict[int, int] = {}
    primes: list[int] = []
    for k in range(2, included_limit + 1):
        if k in next_multiples:
            prime = next_multiples.pop(k)
            multiple: int = k
            if prime == 2:
                multiple <<= 1
            else:
                multiple += prime
                while multiple <= included_limit and multiple in next_multiples:
                    multiple += prime
            if multiple <= included_limit:
                next_multiples[multiple] = prime
        else:
            primes.append(k)
            multiple = k << 1
            if multiple <= included_limit:
                next_multiples[multiple] = k
    return primes



def sieve_of_atkin(included_limit) -> list[int]:
    """
    Get all prime numbers <= n = included_limit, by (simple) Atkin method.

    Complexity:
                * O(n) in time
                * O(n) in space

    :param included_limit: maximal value to check
    :return: list of ordered prime numbers
    """
    sieve = [False] * (included_limit + 1)
    for i in [2, 3]:
        if i >= len(sieve):
            break
        sieve[i] = True
    x = 1
    while x * x <= included_limit:
        y = 1
        while y * y <= included_limit:
            n = 4 * x * x + y * y
            if n <= included_limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] ^= True
            n = 3 * x * x + y * y
            if n <= included_limit and n % 12 == 7:
                sieve[n] ^= True
            n = 3 * x * x - y * y
            if x > y and n <= included_limit and n % 12 == 11:
                sieve[n] ^= True
            y += 1
        x += 1
    root = 5
    while root * root <= included_limit:
        if sieve[root]:
            for i in range(root * root, included_limit + 1, root * root):
                sieve[i] = False
        root += 1
    primes: list[int] = []
    for k in range(2, included_limit + 1):
        if sieve[k]:
            primes.append(k)
    return primes


if __name__ == '__main__':

    import time

    limit = 1000000
    t0 = time.time()
    primes_0: list[int] = sieve_of_periat(limit)
    t1 = time.time()
    primes_1: list[int] = sieve_of_atkin(limit)
    t2 = time.time()
    
    print(f'Find prime numbers <= {limit}:')
    print(f'{len(primes_0)} primes found by Périat method\n'
          f'in time {t1 - t0}s')
    print(f'{len(primes_1)} primes found by (simple) Atkin method\n'
          f'in time {t2 - t1}s')
    print(f'Both method has same result: {primes_0 == primes_1}')
