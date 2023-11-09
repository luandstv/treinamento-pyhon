nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")


disc = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

print("Dados do usúario:")
for key, value in disc.items():
    print(f"{key}: {value}")
