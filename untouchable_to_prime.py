def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def euler_totient(n):
    result = n  # Initialize result with n
    # Calculate Euler's totient function
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
def digit_sum_recursive(number):
    while number >= 10:
        number = sum(int(digit) for digit in str(number))
    return number
def process_number(number):
    totient = euler_totient(number)
    digit_sum = digit_sum_recursive(totient)
    # Continue until a single-digit sum
    while digit_sum >= 10:
        totient = euler_totient(digit_sum)
        digit_sum = digit_sum_recursive(totient)
    # Perform the specified division based on the single-digit sum
    result = (totient / 2) + 1 if digit_sum >= 5 else (totient / 4) + 1
    # Remove the zero if the result has a remainder of zero
    result = int(result) if result.is_integer() else result
    is_prime_result = is_prime(result)
    return number, totient, digit_sum, result, is_prime_result
# User input for a list of numbers
numbers = input("Enter a list of numbers separated by space: ").split()
# Convert input to integers
numbers = [int(num) for num in numbers]
# Create a table header
header = "+------------+------------+------------+------------+---------------+"
print(header)
print("|{:^12}|{:^12}|{:^12}|{:^12}|{:^15}|".format("Number", "Totient", "Digit Sum", "Result", "Is Prime"))
print(header)
# Process each number in the list and display the results
for num in numbers:
    n, totient, digit_sum, result, is_prime_result = process_number(num)
    row = "|{:^12}|{:^12}|{:^12}|{:^12}|{:^15}|".format(n, totient, digit_sum, result, is_prime_result)
    print(row)
    print("+------------+------------+------------+------------+---------------+")