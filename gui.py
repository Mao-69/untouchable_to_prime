import tkinter as tk
import math
from tabulate import tabulate

# Function to calculate the Euler's totient function
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

# Function to compute the single digit sum of a number
def single_digit_sum(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a list of untouchable numbers from 2 to limit
def untouchable_numbers(limit):
    sieve = [0] * (limit + 5)
    for i in range(1, limit + 1):
        for j in range(i * 2, limit + 1, i):
            sieve[j] += i
    untouchables = [i for i in range(2, limit + 1) if sieve[i] > i]
    return untouchables

# Function to find all Joshie pairs from a list of untouchable numbers
def find_joshie_pairs(untouchables):
    joshie_pairs = {}
    for n in untouchables:
        phi_n = phi(n)
        digit_sum = single_digit_sum(phi_n)
        result = phi_n // 2 + 1  # Since μ = 2 in this case
        if is_prime(result):
            key = (phi_n, digit_sum, result)
            if key not in joshie_pairs:
                joshie_pairs[key] = []
            joshie_pairs[key].append(n)
    if joshie_pairs:  # Check if any Joshie pairs are found
        return joshie_pairs
    else:
        return {}  # Return an empty dictionary if no Joshie pairs are found

# Function to save the selected Joshie Set to a file
def save_selected_set():
    selected_set = selected_joshie_set.get(1.0, tk.END).strip()
    with open("numbers.txt", "w") as file:
        file.write(selected_set)
    set_count_box.delete(1.0, tk.END)
    set_count_box.insert(tk.END, f"Set count: {count_numbers('numbers.txt')}")

# Function to count numbers in the saved set file
def count_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            numbers = content.strip()[1:-1].split(', ')
            count = len(numbers)
            return count
    except FileNotFoundError:
        print("File not found.")
        return -1

# Function to display the selected Joshie Pair in the Selected Joshie Set box
def display_selected(event):
    selected_index = result_box.curselection()
    if selected_index:
        value = result_box.get(selected_index[0])
        selected_joshie_set.delete(1.0, tk.END)
        selected_joshie_set.insert(tk.END, value)

# Function to calculate Joshie Sets
def calculate_joshie_sets():
    x = int(input_x.get())
    y = int(input_y.get())
    untouchable_numbers_list = untouchable_numbers(y)
    joshie_pairs = find_joshie_pairs(untouchable_numbers_list)
    result_box.delete(0, tk.END)
    for key, value in joshie_pairs.items():
        if len(value) > 1:
            numerical_values = ", ".join(map(str, value))
            result_box.insert(tk.END, f"Joshie Pair: [{numerical_values}]\n")

# Function to calculate patterns
def calculate_patterns():
    numbers = []
    selected_set = selected_joshie_set.get(1.0, tk.END).strip()
    for num in selected_set.split(','):
        num = num.strip()
        if num.isdigit():
            numbers.append(int(num))
    patterns = check_patterns(numbers)
    pattern_results.delete(1.0, tk.END)
    for pattern, values in patterns.items():
        if values:
            pattern_results.insert(tk.END, f"\n{pattern}:\n")
            if isinstance(values[0], list):
                values = [item for sublist in values for item in sublist]
            for i, value in enumerate(values, start=1):
                pattern_results.insert(tk.END, f"{i}: {value}\n")
        else:
            pattern_results.insert(tk.END, f"\n{pattern}: No values found\n")
# Function to find factors and multiples of a number
def multiples_and_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
# Function to generate a list of consecutive integers around a given number
def consecutive_integers(n):
    return [n - 1, n, n + 1]
# Function to generate a geometric sequence starting from a given number
def geometric_sequence(n):
    sequence = [n]
    for i in range(1, 6):  # Check up to 5 terms
        sequence.append(n * (2 ** i))
    return sequence
# Function to check if a number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]
# Function to check if a number is a perfect square or a perfect cube
def perfect_squares_or_cubes(n):
    root = math.isqrt(n)
    if root * root == n:
        return "Perfect Square"
    elif round(n ** (1. / 3)) ** 3 == n:
        return "Perfect Cube"
    else:
        return None
import math

# Function to check if two numbers are coprime
def is_coprime(a, b):
    return math.gcd(a, b) == 1
# Function to check if a number is semiprime
def is_semiprime(n):
    factors = prime_factorization(n)
    return len(factors) == 2
# Function to calculate the prime factorization of a number
def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors
# Function to check if a number is a power of two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Function to check patterns
def check_patterns(numbers):
    patterns = {
        "Prime Factorizations": [],
        "Multiples and Factors": [],
        "Consecutive Integers": [],
        "Geometric Sequences": [],
        "Palindrome Numbers": [],
        "Perfect Squares or Cubes": [],
        "Coprime": [],
        "Semiprime": [],
        "Powers of Two": [],
        # Add other patterns here
    }

    total_patterns = len(patterns)
    current_pattern = 0

    for pattern, _ in patterns.items():
        current_pattern += 1
        print(f"Calculating {pattern}... ({current_pattern}/{total_patterns})", end='\r', flush=True)

        for num in numbers:
            if pattern == "Prime Factorizations":
                if is_prime(num):
                    patterns[pattern].append(prime_factorization(num))
            elif pattern == "Multiples and Factors":
                patterns[pattern].append(multiples_and_factors(num))
            elif pattern == "Consecutive Integers":
                patterns[pattern].append(consecutive_integers(num))
            elif pattern == "Geometric Sequences":
                patterns[pattern].append(geometric_sequence(num))
            elif pattern == "Palindrome Numbers":
                if is_palindrome(num):
                    patterns[pattern].append(num)
            elif pattern == "Perfect Squares or Cubes":
                perfect = perfect_squares_or_cubes(num)
                if perfect:
                    patterns[pattern].append((num, perfect))
            elif pattern == "Coprime":
                for other_num in numbers:
                    if num != other_num and is_coprime(num, other_num):
                        patterns[pattern].append((num, other_num))
            elif pattern == "Semiprime":
                if is_semiprime(num):
                    patterns[pattern].append(num)
            elif pattern == "Powers of Two":
                if is_power_of_two(num):
                    patterns[pattern].append(num)
            # Add more pattern checks similarly

    print("Pattern calculation complete.                                 ")  # Clear progress message
    return patterns if any(patterns.values()) else {}  # Return an empty dictionary if no patterns are found

# GUI setup
root = tk.Tk()
root.title("Joshie Sets Calculator")

# Left frame for user input and selected Joshie Set
left_frame = tk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10)

# Equation label
equation_label = tk.Label(left_frame, text="let (n) be an integer > 2\nin the untouchable numbers set (2,5,52,88,96, . . . , 498)\nsuch that\nthe totient number Φ(n) = n∏(1-1/p)\nis the positive integers up to a given integer (n)\nthat are relatively prime to (n)\nnow let\nF₁₀Φ(n) be the single digit sum of the totient number\nthen let\nμ = { 2, if F₁₀Φ(n) ≥ 5 or 4, if F₁₀Φ(n) < 5\nsuch that\nJ(n) = ( Φ(n) / μ ) +1 is a prime number\nand\n(n₁, n₂, nₖ) : Φ(n₁) = Φ(n₂) =...= Φ(nₖ) ∧\n F₁₀Φ(n₁) = F₁₀Φ(n₂) =...= F₁₀Φ(nₖ) ∧\n J(n₁) = J(n₂) =...= J(nₖ)\n")
equation_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

input_x_label = tk.Label(left_frame, text="Untouchable Number\nLower Limit:")
input_x_label.grid(row=1, column=0, sticky="w", pady=(0, 100))
input_x = tk.Entry(left_frame)
input_x.grid(row=1, column=1, pady=(0, 100))


input_y_label = tk.Label(left_frame, text="Untouchable Number\nUpper Limit:")
input_y_label.grid(row=1, column=0, sticky="w")
input_y = tk.Entry(left_frame)
input_y.grid(row=1, column=1)

calculate_button = tk.Button(left_frame, text="Calculate Joshie Sets", command=calculate_joshie_sets)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

selected_joshie_label = tk.Label(left_frame, text="Selected Joshie Set:")
selected_joshie_label.grid(row=3, column=0, sticky="w")

selected_joshie_set = tk.Text(left_frame, width=30, height=4)
selected_joshie_set.grid(row=4, column=0, columnspan=2)

save_set_button = tk.Button(left_frame, text="Save Set", command=save_selected_set)
save_set_button.grid(row=5, column=0, columnspan=2, pady=5)

# Right frame for displaying results and set count
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10)

result_label = tk.Label(right_frame, text="Joshie Pairs:\n (n₁, n₂, nₖ) : Φ(n₁) = Φ(n₂) =...= Φ(nₖ) ∧ F₁₀Φ(n₁) = F₁₀Φ(n₂) =...= F₁₀Φ(nₖ) ∧ J(n₁) = J(n₂) =...= J(nₖ)")
result_label.grid(row=0, column=0, sticky="w")

result_scrollbar = tk.Scrollbar(right_frame, orient=tk.VERTICAL)
result_box = tk.Listbox(right_frame, width=40, height=20, yscrollcommand=result_scrollbar.set)
result_scrollbar.config(command=result_box.yview)
result_box.grid(row=1, column=0, sticky="nsew")
result_scrollbar.grid(row=1, column=1, sticky="ns")
result_box.bind("<<ListboxSelect>>", display_selected)

set_count_box = tk.Text(right_frame, width=30, height=4)
set_count_box.grid(row=2, column=0, sticky="nsew")

count_button = tk.Button(right_frame, text="Count Numbers in the Set", command=lambda: set_count_box.insert(tk.END, f"Set count: {count_numbers('numbers.txt')}"))
count_button.grid(row=3, column=0, sticky="nsew")

# Pattern Results box and button
pattern_results_label = tk.Label(right_frame, text="Pattern Results:")
pattern_results_label.grid(row=4, column=0, sticky="w")

pattern_results_scrollbar = tk.Scrollbar(right_frame, orient=tk.VERTICAL)
pattern_results = tk.Text(right_frame, width=40, height=20, yscrollcommand=pattern_results_scrollbar.set)
pattern_results_scrollbar.config(command=pattern_results.yview)
pattern_results.grid(row=5, column=0, sticky="nsew")
pattern_results_scrollbar.grid(row=5, column=1, sticky="ns")

calculate_patterns_button = tk.Button(right_frame, text="Calculate Patterns", command=calculate_patterns)
calculate_patterns_button.grid(row=6, column=0, sticky="nsew")

# Make the display results box responsive to the GUI
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
right_frame.grid_rowconfigure(1, weight=1)

root.mainloop()
