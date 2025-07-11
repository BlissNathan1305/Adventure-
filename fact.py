def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
