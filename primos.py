#This program generates prime numbers from 2 up to the specified number. 
#If the number is not a prime, it won't be displayed
#For example: prime_numbers(15) = [2,3,5,7,11,13]

def prime_numbers(n):
    numbers = list(((filter(lambda x:n%x==0, range(2,n+1)))));
    return numbers;
        
print(prime_numbers(30));

#this is a probe
#changes 

    

