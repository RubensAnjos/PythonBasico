# Esse módulo realiza as 4 operações matemáticas e alimenta o programa calculadora

# Recebe dois números e retorna a soma
def soma():
    numero_1=float(input('\n\t  -> Primeiro numero: '))
    numero_2=float(input('\t  -> Segundo  numero: '))
    return numero_1 + numero_2

# Recebe dois números e retorna a subtração
def subtracao():
    numero_1=float(input('\n\t  -> Primeiro numero: '))
    numero_2=float(input('\t  -> Segundo  numero: '))
    return numero_1-numero_2

# Recebe dois números e retorna a multiplicação
def multiplicacao():
    numero_1=float(input('\n\t  -> Primeiro numero: '))
    numero_2=float(input('\t  -> Segundo  numero: '))
    return numero_1*numero_2

# Recebe dois números e retorna a divisão do primeiro pelo segundo
def divisao():
    numero_1=float(input('\n\t  -> Primeiro numero: '))
    numero_2=float(input('\t  -> Segundo  numero: '))
    # Orientar o usuario quanto a divisao por zero
    if numero_2 == 0:
        print('\t  !Não é possível dividir por ZERO!')
        numero_2=float(input('\t  -> Segundo  numero: '))
        pass
    return numero_1/numero_2

# Após escape \n\t foram adicionados 2 espaços teclado