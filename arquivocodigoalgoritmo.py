# -*- coding: utf-8 -*-
"""Cópia de Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wFhelqBz46aDKn1DuH5TUGgRDAADU-8B
"""

num = int(input('Digite um número: '))

print('O número informado foi:', num)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

soma = n1+n2
print(n1, '+', n2, '=', soma)

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print (f"A média das notas é {media}")

valorHora = int(input("Quanto custa sua hora trabalhada? "))
qtdHoraMes = int(input("Quantas horas você trabalha por mês?"))
salario = valorHora * qtdHoraMes
print(f"O total do seu salário é de: {salario}")

"DESAFIO"

peso = int(input("Quantos kg pescados hoje: "))
excesso = peso - 50
multa = excesso * 4
print("\nO valor da multa é R$ ", multa)
print("P.S.: Caso o resultado seja negativo, desconsidere a multa.")