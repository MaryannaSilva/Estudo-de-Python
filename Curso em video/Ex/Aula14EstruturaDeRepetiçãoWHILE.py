'''c = 1
while c < 10:
    print(c)
    c = c + 1

print('Fim')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 ==0:
        par += 1
    else:
        impar += 1

print('Voce digitou {} número pares e {} numeros impares'.format(par , impar))
