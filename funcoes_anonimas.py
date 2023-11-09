def lambda_cubo(y): return y*y*y


print(lambda_cubo(5))


lista = [[4, 3, 2], [16, 64, 1, 4], [9, 12, 6, 3]]

# Ordena cada sublista
# X: é o parâmetro que a função recebe


def listaOrdenada(x): return (sorted(i) for i in x)

# busca o segundo maior elemento
# x, f: são os parâmetros ue a função recebe


def segundoMaior(x, f): return [y[len(y)-2] for y in f(x)]


res = segundoMaior(lista, listaOrdenada)
print(res)
