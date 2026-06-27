# Binary stored in nested list
binary = [[1, 0, 1, 1]]

decimal = 0
power = len(binary[0]) - 1

for bit in binary[0]:
    decimal = decimal + bit * (2 ** power)
    power = power - 1

print("Decimal:", decimal)
