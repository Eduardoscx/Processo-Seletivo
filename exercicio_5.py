string = input("Digite a string para inverter: ")

string_invertida = ''

n = len(string)-1
while n >= 0:
    string_invertida = string_invertida+ string[n]
    n-=1

print(string_invertida)