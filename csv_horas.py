import csv
# from calculca_salario_hora import calculaSalario


def calculaSalario(qtdHorasMensal, valorHora):
    if qtdHorasMensal > 176:
        excedente = qtdHorasMensal - 176
        valorExcedente = excedente * (valorHora * 1.5)
        salario = (176 * valorHora) + valorExcedente
        return salario
    else:
        salario = qtdHorasMensal * valorHora
        return salario


with open('horas.csv', 'r', newline='') as horas_csv, open('salario.csv', 'w') as salario_csv:
    leitor = csv.reader(horas_csv, delimiter=';')

    escritor = csv.writer(
        salario_csv, delimiter=';')
    escritor.writerow(['ID', 'Salario'])

    for i, linha in enumerate(leitor):
        if i != 0:
            horas = linha[2]
            valor_hora = linha[3]
            salario = calculaSalario(int(horas), float(valor_hora))
            escritor.writerow([linha[0], salario])
        else:
            print(f"Cabecalho: {linha}")
