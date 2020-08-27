def prime (x):
    j=0
    for i in range(1,x+1,+1):
        if x%i==0 :
           j+=1
    if j==2 :
        print("The number is prime")
    else:
        print("The number is not prime")
        
        
