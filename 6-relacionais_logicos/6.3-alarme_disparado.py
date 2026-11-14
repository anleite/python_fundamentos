#Definindo os valores das variáveis
temperatura_critica = True
pressao_critica = False

#Realizando a checagem dos sensores
alarme_disparado = temperatura_critica or pressao_critica

#Apresentando disparo do alarme
print(f"Alarme Ativado: {alarme_disparado}")

