#crear una funcion que al pasarle un numero cree numeros primos hasta llegar a ese numero

def primensos(numero):
    lista=list(range(numero))
    for i in lista:
        lista[i]=lista[i]+1
    divisores=list()

    for i in lista:
        divisores.append(tuple(filter(lambda x:i%x==0,lista)))

    divisores_primos=list(filter(lambda x:len(divisores[x-1])==2,lista))
    return(divisores_primos)

#respuesta=primensos(45)
#print(f'Los primos son los siguintes: {respuesta}')

