# Aqui iremos importar o modulo que criamos
import operacoes

# Abaixo, conforme estudamos lá no início, usando o método center, multiplicar strings e escape para criar um título
print('\n')
print('\t','#' * 30)
print('\t','CALCULADORA'.center(30, '*'))
print('\t','#' * 30)
print('')

# Abaixo, usamos o while True, para que peça infinita vezes ao usuário qual a operação desejada
while True:
    # Abaixo, criamos as opções de menu:
    print('\t','-' * 30)
    print('\t  1. Soma')
    print('\t  2. Subtração')
    print('\t  3. Multiplicação')
    print('\t  4. Divisão')
    print('\t  5. Sair da Calculadora...')
    print('\t','-' * 30, '\n')
    # Recebendo a escolha do usuário:
    op= int(input('\t  Escolha a operação desejada: '))

    # Condicionais conforme escolha do usuário
    if op==1:
        print('\n\t  Somando...')
        print(f'\n\t  -> Soma = {operacoes.soma():.2f}\n')
    elif op==2:
        print('\n\t  Subtraindo...')
        print(f'\n\t  -> Subtração = {operacoes.subtracao():.2f}\n')
    elif op==3:
        print('\n\t  Multiplicando...')
        print(f'\n\t  -> Multiplicação = {operacoes.multiplicacao():.2f}\n')
    elif op==4:
        print('\n\t  Dividindo...')
        print(f'\n\t  -> Divisão = {operacoes.divisao():.2f}\n')
    elif op==5:
        # Aqui, iremos utilizar o break para sair do código conforme estudamos no notebook_04
        print('\n\t  Saindo da calculadora! Até mais ;)\n')
        print('\t','-' * 30)
        break
    else:
        print('\n\t  Opção inválida,selecione de 1 a 5:\n')
        