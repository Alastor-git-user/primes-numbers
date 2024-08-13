#This program generates prime numbers from 2 up to the specified number. 
#If the number is not a prime, it won't be displayed
#For example: prime_numbers(15) = [2,3,5,7,11,13]

def prime_numbers(n):
    return [num for num in range(2, n + 1) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
           
print(prime_numbers(30));


    

