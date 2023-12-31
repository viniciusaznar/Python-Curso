'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é 'par' ou 'impar'. Caso o usuário não digite um
numero inteiro, informe que não é um número inteiro.
'''

# Primeira solução
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    entrada_int = int(numero)
    numero_impar = entrada_int % 2 != 0
    numero_par = entrada_int % 2 == 0
    if numero_par:
        print('O número que digitou é par')
    else:
        print('O número que digitou é impar')
else:
    print('O número digitado não é um número inteiro')


# Segunda solução
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número{entrada_int} é {par_impar_texto}')
# else:
#     print('O número digitado não é um número inteiro')