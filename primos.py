#Este es un programa para crear numeros primos 
# esta es la version mejorada
#creando una version que permita obtener los numeros primos hasta el
#numero dado.
#se volvio al anterior programador
#nueva actualizacion
#nueva mejora

def prime_number(n):
    numbers = list(((filter(lambda x:n%x==0, range(1,n+1)))));
    return numbers;
        
print(prime_number(30));


    

