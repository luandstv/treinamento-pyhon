arquivo = open('arquivo.txt', 'a')

frases = list()
frases.append('Olá, mundo!\n')
frases.append('Este é um arquivo de texto.\n')
frases.append('Aqui temos três linhas.\n')
frases.append('iteris domina.\n')

arquivo.writelines(frases)
arquivo.close()
