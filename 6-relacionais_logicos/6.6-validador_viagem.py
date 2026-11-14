#Solicitando dados do veículo

combustivel = float(input("Quantidade de combustivel: "))
pneus_calibrado = input("Os pneus estão calibrados? (sim/não): ").lower().strip()
documento_ok = input("A documentação está em dia (sim/não): ").lower().strip()

#Checagem individual 
combustivel_suficiente = combustivel >= 10.0
pneus_ok = pneus_calibrado == "sim"
documento_regular = documento_ok == "sim"

# Combinação lógica para liberação de viagem
viagem_liberada =  combustivel_suficiente and pneus_ok and documento_regular
                     
# Apresentando o status e liberação da viagem
print("\n------STATUS DE SEGURANÇA PARA A VIAGEM-----")
print(f"1. Combustivel Suficiente (>=10L): {combustivel_suficiente}")
print(f"2. Pneus Calibrados: {pneus_ok}")
print(f"Documentação Regularizado: {documento_regular}")
print(f"\n VIAGEM LIBERADA: {viagem_liberada}")
