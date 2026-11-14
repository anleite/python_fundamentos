# Definindo o valor das variáveis
total_sensores = int(input("DIGITE A QUANTIDADE DE SENSORES DISPONÍVEIS: "))
CAPACIDADE_CAIXA = 12

#Quanas caixas compltas podemos encher?
caixas_fechadas = total_sensores//CAPACIDADE_CAIXA

#Quantos sensores ficarão avulsos?
sobra_sensores =  total_sensores%CAPACIDADE_CAIXA

if sobra_sensores == 0:
    print("NÃO RESTA ITENS AVULSOS")
else:
    print(f"Preencher 1{caixas_fechadas} caixas e guardar {sobra_sensores} peças avulsas.")