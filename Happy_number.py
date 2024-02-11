n = int(input("Enter Your Number : "))
x = n
while x >= 10:               # Happy Number :: A number which sum of its squared digits will eventually
    sum = 0                  #  be 1, after infinte number of iteration
    while x > 0:            
        r = x%10         
        sum = sum+(r**2)    
        x = x//10            
    x = sum                  
if x == 1:
    print(n, "is a Happy Number!")
else:
    print(n, "OPPs! its Not a Happy Number")