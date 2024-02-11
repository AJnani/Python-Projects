n = int(input("Enter your number : "))

for i in range(1, n+1):         
    if n%i == 0:
        flag = 0                 
        for j in range(2, i):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            print(i, end=" ")

#########################################################################################################
########################################################################################################


n = int(input("Enter your number : "))

for i in range(1, n+1):
    if n%i == 0:
        is_prime = True
        for j in range(2, i):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")