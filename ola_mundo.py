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


# valor = 0 

# try:
#     valor = int(input("Digite a sua idade: "))
# except ValueError as error:
# 		print("não foi possível ler a sua idade, use somente números:", error)
# else: 
# 	print("Sua idade é:", valor, "anos")

#  for
# for letra in "Iteris":
# 		print(letra)

# # While
# valor = input("Digite 'banana': ")

# while valor != "banana":
# 	valor = input("Digite 'banana': ")
# # else pode ser usado quando a condição não atende mais o while
# else:
# 	print("voce digitou:", valor)


# if/else/elif 

# valor = int(input("digite um número entre 0 e 9: "))

# if 0 <= valor and valor < 5:
# 	print("valor entre 0 e 4")
# elif 5 <= valor and valor < 10:
# 	print("valor entre 5 e 9")
# else:
# 	print("valor fora do intervalo")

valor = int(input("Escolha uma das opções. De 1 a 3: "))
mensagem = ""

match valor:
	case 1:
		mensagem = "opção 1 escolhida"
	case 2:
		mensagem = "opção 2 escolhida"
	case 3:
		mensagem = "opção 3 escolhida"
	# default statement
	case _:
		mensagem = "opção inválida"
print(mensagem)