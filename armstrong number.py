# Program to check if a number is an Armstrong number
num = 153
sum = 0

# Temporarily store the original number
temp = num 

# Extract digits and calculate the sum of cubes
while temp > 0:
    digit = temp % 10
    sum += digit ** 3          # Add the cube of the digit to the sum
    temp //= 10                # Remove the last digit

# Check if the sum matches the original number
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num,"is not a Armstrong number")
