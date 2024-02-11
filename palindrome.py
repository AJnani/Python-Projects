n = int(input("Enter Your Number : "))
x = n
rev = 0

while n > 0:                                           
    r = n % 10                 # here 123 % 10 = 1       # here 12 % 10 = 2        # here 1 % 10 = 1
    rev = rev * 10 + r         # here 0 * 10 + 1 = 1     # here 1 * 10 + 2 = 12    # here 0 * 10 + 1 = 1
    n = n // 10                # here 123 // 10 = 12     # here 12 // 10 = 1       # here 151 // 10 = 15
print(f"Reverse number for {x} is : ", rev)

if rev == x:
    print(f"{x} is a palindrome Number ")
else :
    print(f"{x} is not a palindrome Number ")