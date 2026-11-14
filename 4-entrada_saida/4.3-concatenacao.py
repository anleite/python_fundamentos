#Criando as variáveis
numero1=float(input("Digite um número: "))    
numero2=float(input("Digite outro número: "))

#Realizando a soma do numero 1 com o numero 2
resultado=numero1+numero2

#Apresentando o resultado da soma ao usuário 
print("Resultado da soma: ",int(resultado))
print(f"Resultado da soma: {int(resultado)}")

#Testando o tipo de dado, durante a entrada do usuário
idade=input("Digite sua idade: ")
print(type(idade))