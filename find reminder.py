def find_remainder(number, Z):
    return number % Z

# Example usage:
num = int(input("Enter the number: "))
z = int(input("Enter the divisor (Z): "))
print(f"Remainder when {num} is divided by {z} is {find_remainder(num, z)}")