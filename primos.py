#Este es un programa para crear numeros primos 
# esta es la version mejorada
#creando una version que permita obtener los numeros primos hasta el
#numero dado.
def prime_number(n):
    numbers = list(((filter(lambda x:n%x==0, range(1,n+1)))));
    if len(numbers)==2:
        return f'{n} es primo';
    else:
        return f'{n} no es primo';
        
print(prime_number(13));


    

