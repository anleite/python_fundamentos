
componentes=int(input("Digite a quantidade de COMPONENTES: "))
OPERADORES = 4

#QUANTOS COMPONENTES INTEIROS CADA OPERADOR VAI PROCESSAR?
componentes_processados=componentes//OPERADORES

#QUANTOS COMPONENTES IRÃO SOBRAR?
sobra_componentes=componentes%OPERADORES

if sobra_componentes==0:
 print("TODOS COMPONENTES FORAM PROCESSADOS")
else:
 print(f' FORAM PROCESSADOS {componentes_processados} COMPONENTES E SOBRARAM {sobra_componentes}')