import tkinter as tk
import math

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
    sieve = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(i * 2, limit + 1, i):
            sieve[j] += i
    return [i for i in range(2, limit + 1) if sieve[i] > i]

# Function to find all Joshie pairs from a list of untouchable numbers
def find_joshie_pairs(untouchables):
    joshie_pairs = {}
    for n in untouchables:
        phi_n = phi(n)
        digit_sum = single_digit_sum(phi_n)
        mu = 2 if digit_sum >= 5 else 4
        j_n = (phi_n // mu) + 1
        
        if is_prime(j_n):
            key = (phi_n, digit_sum, j_n)
            if key not in joshie_pairs:
                joshie_pairs[key] = []
            joshie_pairs[key].append(n)
    
    return {k: v for k, v in joshie_pairs.items() if len(v) > 1}

# Function to calculate the magnitude of a vector
def vector_magnitude(vector):
    squares = [x ** 2 for x in vector]
    sum_of_squares = sum(squares)
    magnitude = math.sqrt(sum_of_squares)
    return round(magnitude), squares, sum_of_squares, magnitude

# Function to display results in the Text widget
def display_results(results):
    text_widget.delete(1.0, tk.END)  # Clear previous results
    magnitude_groups = {}

    # Group Joshie pairs by their rounded vector magnitude
    for key, values in results.items():
        vector = values  # Using the Joshie pair values as vector components
        rounded_result, squares, sum_of_squares, magnitude = vector_magnitude(vector)
        
        if rounded_result not in magnitude_groups:
            magnitude_groups[rounded_result] = []
        magnitude_groups[rounded_result].append((values, key, rounded_result, squares, sum_of_squares, magnitude))

    # Only display groups with more than one pair
    magnitude_count = 0  # Counter for magnitude sets
    for mag, pairs in magnitude_groups.items():
        if len(pairs) > 1:  # Only show if more than one pair shares the same magnitude
            text_widget.insert(tk.END, f"Magnitude {mag}:\n", 'highlight')  # Highlight
            for pair, key, rounded_result, squares, sum_of_squares, magnitude in pairs:
                text_widget.insert(tk.END, f"Vector: {pair} with properties: {key}\n")
                text_widget.insert(tk.END, (
                    f"  Vector components: {pair}\n"
                    f"  Squares of each component: {squares}\n"
                    f"  Sum of squares: {sum_of_squares}\n"
                    f"  Magnitude before rounding: {magnitude:.10f}\n"  # Full precision before rounding
                    f"  The rounded magnitude of the vector is: {rounded_result}\n"
                ))
                text_widget.insert(tk.END, "\n")
            magnitude_count += 1  # Increment count for each magnitude set

    # Display the total number of magnitude sets
    text_widget.insert(tk.END, f"Total number of magnitude sets: {magnitude_count}\n")

# GUI setup
def main():
    global text_widget

    root = tk.Tk()
    root.title("Vector Magnitude Sets")

    # Create a Text widget for displaying results
    text_widget = tk.Text(root, wrap=tk.WORD, height=30, width=80)
    text_widget.pack(pady=10)

    # Create a tag for highlighting
    text_widget.tag_config('highlight', foreground='blue')  # Change the color here

    # Input limits
    lower_limit = int(input("Enter lower limit for untouchable numbers: "))
    upper_limit = int(input("Enter upper limit for untouchable numbers: "))

    # Generate untouchable numbers
    untouchables = untouchable_numbers(upper_limit)
    filtered_untouchables = [n for n in untouchables if n >= lower_limit]

    # Find Joshie pairs
    joshie_pairs = find_joshie_pairs(filtered_untouchables)

    # Display results
    display_results(joshie_pairs)

    root.mainloop()

if __name__ == "__main__":
    main()
