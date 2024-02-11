n = int(input("Enter your Sequence : "))

n1 = 0                            # Fabonnaci Series :: mathematical number starts with 0 and 1
n2 = 1                            #  with each subsequent number being the sum of two preceding numbers
count = 2

if n < 0:
    print("NO! +ve Numbers Only!")
elif n == 1:
    print(n1) 
else:
    print("n1 = ",n1,end=",")
    print(" n2 = ",n2, end=",")
    while count<n:
        n3 = n1 + n2
        print(" n3 = ",n3,end=",")
        count+=1
        n1=n2
        n2=n3

