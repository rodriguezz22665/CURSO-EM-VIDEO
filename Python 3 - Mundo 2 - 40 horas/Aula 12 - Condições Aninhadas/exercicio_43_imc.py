#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

# IMC = peso/(altura x altura)

peso = float(input("Qual o seu peso? (kg) "))

altura = float(input("Qual a sua altura? (m) "))

imc = peso/(altura **2)

print("O IMC dessa pessoa é \033[32;45m{:.1f}\033[m kg/m.".format(imc))

if imc < 18.5:
    print("Atenção! Você está na faixa abaixo do peso.")
elif 18.5 <= imc < 25:
    print("PARABÉNS! Você está na faixa de peso normal.")
elif 25 <= imc < 30:
    print("Atenção! Você está na faixa de sobrepeso.")
elif 30 <= imc < 40:
    print("CUIDADO! Você está na faixa da obesidade.")
elif imc >= 40:
    print("CUIDADO!! Você está na faixa de obesidade mórbida.")           