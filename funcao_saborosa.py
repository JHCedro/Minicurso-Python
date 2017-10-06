def funcao_saborosa(lista):
	'''Funcao que recebe uma lista de palavras e retorna uma tupla
		contendo a menor e a maior palavra da lista'''
	if lista == []:
		return tuple()
	else:
		lista.sort(key = len)
		return (lista[0], lista[-1])

palavras = ['ventilador', 'cafe', 'oculos', 'pneumoultramicroscopicossilicovulcaniconiose']

print(funcao_saborosa(palavras))
