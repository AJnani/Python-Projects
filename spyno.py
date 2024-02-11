n = int(input("Enter a Number : "))

sum = 0            # SpyNo. :: The product of number and sum of the number is equal
prod = 1
temp = n

while n>0:
    digit = n%10
    sum = sum + digit
    prod = prod * digit
    n = n // 10

if sum == prod:
    print(temp,"is a spy number")
else:
    print(temp, "is not a spy number")

########################################################################################################
#########################################################################################################



number = int(input("Enter a number: "))

# Convert the number to a list of digits
digits = [int(digit) for digit in str(number)]

# Calculate the sum and product of digits
digit_sum = sum(digits)
digit_product = 1
for digit in digits:
    digit_product *= digit

# Check if it's a spy number
if digit_sum == digit_product:
    print(number, "is a spy number.")
else:
    print(number, "is not a spy number.")
