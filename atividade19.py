# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

numero = int(input("Digite um numero: "))
fatorial = 1 

while numero > 1:
    fatorial *= numero
    numero -= 1 
print(f"Fatorial: {fatorial}")


