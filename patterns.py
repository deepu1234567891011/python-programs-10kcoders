num = int(input("Enter a number: "))
temp = num

# Find length of the number
length = len(str(num))

sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** length)
    temp = temp // 10

# Check condition
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
