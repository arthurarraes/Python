n1 = (input("Qual o seu nome?"))
print('Olá, {}'.format (n1))

operation = input('''
Por favor escreva qual operação você gostaria de realizar:
1 para adição
2 para subtrair
3 para dividir
4 para multiplicar
''')

n2 = int(input('Insira o primeiro número:'))
n3 = int(input('Insira o segundo número:'))

if operation == '1':
 print('{} + {} = '.format (n2, n3))
 print(n2+n3)
 
elif operation == '2':
 print('{} - {} = '.format (n2, n3))
 print(n2-n3)

elif operation == '3':
 print('{} / {} = '.format (n2, n3))
 print(n2/n3)

elif operation == '4':
 print('{} * {} = '.format (n2, n3))
 print(n2*n3)