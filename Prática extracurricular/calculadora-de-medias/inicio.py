print("-="*25)
print("CALCULADORA DE MÉDIAS DE HORAS EXTRAS EM FÉRIAS")
print("-="*25)

#pergunta qual o valor do salário do colaborador por hora
sal_hora = float(input("Qual o valor do salário do colaborador por hora? \n"))

#pergunta o total de horas extras feitas dentro do período aquisitivo
qt_horas = float(input("\nQuantidade de horas extras dentro do período aquisitivo: \n"))

#pergunta a porcentagem das horas extras
percen_he = float(input("Qual o percentual dessas horas extras? \n"))

#pergunta qual duração das férias
duracao_ferias = float(input("Quantos dias dse férias o colaborador vai gozar? \n"))

#pergunta qual o total de DSR dentro do período aquisitivo
dsr_opcao = float(input("Digite 1 para inserir o total de DSR em valor R$\n ou digite 2 para inserir o total em horas: \n"))

#pergunta a media de dsr vai ser calculada em valor ou hora
if dsr_opcao == 1:
    dsr_valor = float(input("Digite o total de DSR em valor dentro do período aquisitivo: \n"))
if dsr_opcao == 2:
    dsr_valor = float(input("Digite o total de DSR em horas dentro do período aquisitivo: \n"))
    
#Passa as horas extras para centesimal 
horas_int = (qt_horas) - (qt_horas % 1)
qt_horas_cen = (qt_horas % 1 * 100) / 60 + horas_int

#acrescenta a porcentagem da hora extra
qt_horas_acres = (percen_he / 100 + 1) * qt_horas_cen

#se escolheu o dsr em horas, ele soma o valor do dsr em horas + o valor de horas extras com acréscimo
if dsr_opcao == 2:
    dsr_int = (dsr_valor) - (dsr_valor % 1)
    dsr_valor = (dsr_valor % 1 * 100) / 60 + dsr_int
    qt_horas_acres = dsr_valor + qt_horas_acres
   

#Encontra a media das horas extras dentro do período aquisitivo
media_qt_horas = qt_horas_acres/ 12

#print("A média da quantidade de horas feitas dentro do período aquisitivo é {:.2f}".format(media_qt_horas))

#Multiplica a média de horas pelo valor do Salário hora
valor_hr_extra = media_qt_horas * sal_hora

#se escolheu o dsr em valor, ele soma a média do valor da hora extra com o valor da média do dsr
if dsr_opcao == 1: 
    valor_hr_extra = valor_hr_extra + (dsr_valor / 12)
    
#Divide por 30 e multiplica pela quantidade de dias de férias
valor_hr_extra_total = valor_hr_extra / 30 * duracao_ferias

print("\nO valor total da média das horas extras a {}% acrescidas do DSR é {:.2f}\n".format(percen_he,valor_hr_extra_total))
