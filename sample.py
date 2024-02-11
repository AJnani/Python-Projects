for num in range(2, 100):

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            #print(num, "is not a prime number")
            break
    if is_prime:
       print(num, "is a Prime Number")


#######################################################################################################
#######################################################################################################
       
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()


