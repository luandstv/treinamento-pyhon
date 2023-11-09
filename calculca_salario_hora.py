def calculaSalario(qtdHorasMensal, valorHora):
    if qtdHorasMensal > 176:
        excedente = qtdHorasMensal - 176
        valorExcedente = excedente * (valorHora * 1.5)
        salario = (176 * valorHora) + valorExcedente
        print(f"Salario com hora extra: {salario}")
        print(f"valor excedente: {valorExcedente}")
        return salario
    else:
        salario = qtdHorasMensal * valorHora
        print(f"Salario sem hora extra: {salario}")
        return salario
