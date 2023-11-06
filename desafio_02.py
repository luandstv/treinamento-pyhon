# grauC = float(input("Digite a temperatura em graus Celsius: "))

# resultadoF = grauC * 1.8 + 32

# print("A temperatura em Fahrenheit é:", resultadoF)

# grauF = float(input("Digite a temperatura em graus Fahrenheit: "))

# resultadoC = (grauF - 32) / 1.8

# print("A temperatura em Celsius é:", resultadoC)

# quantidade_brl = float(input("Digite a quantidade em reais: "))

# cotacao_dolar = 0.20

# quantidade_usd = quantidade_brl * cotacao_dolar

# print("A quantidade em dólares é:", quantidade_usd)

frase = input("Digite uma frase: ")

while(frase != "*"): 
    primeiraLetra = frase[0].lower()
    tautograma = "Y"
    frase = frase.split()

    for palavra in frase:
        if primeiraLetra != palavra[0].lower():
            tautograma = "N"
            break
    
    print(tautograma)
    frase = input("Digite uma frase: ")