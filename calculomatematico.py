#MENU

print('Escolha entre as operações abaixo, qual deseja realizar!')
print('Para adição digite: (+)')
print('Para subtração digite: (-)')
print('Para multiplicação digite: (*)')
print('Para divisão digite: (/)')
print('Para sair da calculadora digite: (s)')

#Laço de Repetição

while True:
    op = input('Qual operação você deseja realizar? ')
    if ((op != '+') and (op != '-') and (op != '*') and (op != '/') and (op != 's')):
        print('Escolha uma das opções: (+) ou (-) ou (*) ou (/) ou (s)!')
        continue
    elif (op == 's'):
        print('Você decidiu encerrar o programa!')
        break

    num = float(input('Digite o primeiro número para realizar sua operação desejada: '))
    num2 = float(input('Digite o segundo número para realizar sua operação desejada: '))

    if (op == '+'):
        print('Você escolheu adição. A soma é de {} + {} = {}'.format(num, num2, num+num2))

    elif (op == '-'):
        print('Você escolheu subtração. A subtração é de {} - {} = {}'.format(num, num2, num-num2))

    elif (op == '*'):
        print('Você escolheu multiplicação. A multiplicação  é de {} * {} = {}'.format(num, num2, num*num2))

    elif (op == '/'):
        print('Você escolheu divisão. A divisão é de {} / {} = {}'.format(num, num2, num/num2))

print('Encerrrando o programa...')

