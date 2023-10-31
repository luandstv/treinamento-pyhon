# inteiro = 1
# texto = "string"
# boleano = True
# flutuante = 1.5

# print("exibindo tipos:")
# print(inteiro, type(inteiro))
# print(texto, type(texto))
# print(boleano, type(boleano))  
# print(flutuante, type(flutuante))


# resultado = 1 + 1.5

# print("exibindo resultado:", resultado, type(resultado))

# inteiro = 1
# flutuante = float(inteiro)

# print(flutuante, type(flutuante))

# valor = int(input("Digite a sua idade: "))
# print("Sua idade é:", valor, "'valor' é do tipo:", type(valor))


valor = 0 

try:
    valor = int(input("Digite a sua idade: "))
except ValueError as error:
		print("não foi possível ler a sua idade, use somente números:", error)
else: 
	print("Sua idade é:", valor, "anos")