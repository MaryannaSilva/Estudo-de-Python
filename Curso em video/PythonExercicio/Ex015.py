print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')

perc = int(input('Quantidade de Km percorrido:'))
dia = float(input('Quantidade de dias percorrido com o carro:'))

V =  (dia * 60) + (perc * 0.15)

print(' Valor a ser pago é de R${:.2f}.'.format(V))