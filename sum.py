def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
input_number = int(input("Enter a number: "))
result = is_even_or_odd(input_number)
print(f"{input_number} is {result}.")
