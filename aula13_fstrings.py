nome = 'Jhonatan Sousa'
altura = 1.78
peso = 70
imc = peso / (altura * altura) 
# imc = peso / (altura ** 2) 

linha_1 = f'{nome} tem {altura} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)