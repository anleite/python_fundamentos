#Criando o status dos sensores
grade_fechada=True
emergencia_desativada = False

# Ambas precisam ser True para liberar o sistema
sistema_pronto = grade_fechada and emergencia_desativada
print(f"SISTEMA LIBERADO: {sistema_pronto}")
