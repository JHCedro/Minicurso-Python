def funcao_saborosa(lista):
	"""Funcao que recebe uma lista de palavras e retorna uma tupla
		contendo a menor e a maior palavra da lista"""
	if lista == []:
		# se a lista eh vazia, retorna uma tupĺa vazia
		return tuple()
	else:
		# uma forma de fazer
		return max(lista, key=len), min(lista, key=len)
		
		# # outra forma de fazer (ordenando)
		# l_ordenada = sorted(lista, key = len)
		# # obs.: ordenar todos os itens eh mais custoso do que
		# # apenas buscar o maior e o menor
		# return l_ordenada[0], l_ordenada[-1]

palavras = ['ventilador', 'cafe', 'oculos', 'pneumoultramicroscopicossilicovulcaniconiose']

print(funcao_saborosa(palavras))
