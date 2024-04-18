import math

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def single_digit_sum(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def untouchable_numbers(limit):
    sieve = [0] * (limit + 5)
    for i in range(1, limit + 1):
        for j in range(i * 2, limit + 1, i):
            sieve[j] += i
    untouchables = [i for i in range(2, limit + 1) if sieve[i] > i]
    return untouchables

def find_joshie_pairs(untouchables):
    joshie_pairs = {}
    for n in untouchables:
        phi_n = phi(n)
        digit_sum = single_digit_sum(phi_n)
        result = phi_n // 2 + 1
        if is_prime(result):
            key = (phi_n, digit_sum, result)
            if key not in joshie_pairs:
                joshie_pairs[key] = []
            joshie_pairs[key].append(n)
    return joshie_pairs

untouchable_numbers_list = untouchable_numbers(690)

joshie_pairs = find_joshie_pairs(untouchable_numbers_list)

for key, value in joshie_pairs.items():
    if len(value) > 1:
        print("Joshie Pair:", value)