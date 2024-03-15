def calculaFibonacci(numero):
    if numero == 0 or numero == 1:
        return True
    fibonacci = [0,1]
    n = 1
    while numero>fibonacci[n]:
        n+=1
        fibonacci.append(fibonacci[n-1] + fibonacci[n-2])
        if fibonacci[n] == numero:
            return True
    return False


numero_desejado = int(input('Informe o número a ser procurado: '))
if calculaFibonacci(numero_desejado) == True:
    print("O número informado pertence a sequencia")
else:
    print("O número informado não pertence a sequencia")