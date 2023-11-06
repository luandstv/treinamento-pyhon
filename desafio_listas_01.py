lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# Maior número
maiorElemento = max(lista)
print(maiorElemento)

#menor número
menorElemento = min(lista)
print(menorElemento)

# números pares da lista
for numero in lista:
    if numero % 2 == 0:
        print(numero)

# imprima o número de ocorrências do primeiro elemento da lista
primeiro_elemento = lista[0]

numero_ocorrencias = lista.count(primeiro_elemento)
print("O primeiro elemento da lista é {primeiro_elemento} e ocorre {numero_ocorrencias} vezes na lista.")

#media dos elementos

soma = sum(lista)
numero_de_elementos = len(lista)

media = soma / numero_de_elementos

print(f"A média dos elementos na lista é {media}")

# soma dos numeros negativos
soma_negativos = sum(numero for numero in lista if numero < 0)

print(f"A soma dos números negativos é {soma_negativos}")
