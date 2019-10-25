        *  
        * *  
        * * *  
        * * * *  
        * * * * *  
        * * * * 
        * * * 
        * *  
        * 
        
        
#2.Create the below pattern using nested for loop in Python.

number = int(input("enter the values: "))
for i in range(1,number+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for k in range(number-2,-1,-1):
    for m in range(k,-1,-1):
        print("*",end="")
    print()
        
