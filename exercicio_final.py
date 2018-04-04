import matplotlib.pyplot as plt
import numpy as np

# GERANDO DADOS DE ENTRADA -------------------------------------------------
# uma funcao qualquer
f = lambda x : x**3 - 13.0/5.0 * x + 0.95

# um eixo qualquer com 50 valores de -2 a 2
x = np.linspace(-2, 2, 50)					

# array de 50 valores aleatorios entre -0.8 e 0.8
ruido = 0.8 * np.random.randn(50)

# y tem valores proximos a f(x), 
# para simular dados coletados experimentalmente 
y = f(x) + ruido


# ESCRITA EM ARQUIVOS   ------------------------------------------------------
# abrir 'dados_coletados.txt' para escrita ('w')
arq = open('dados_coletados.txt', 'w')	

arq.write('X \t Y \n')
for i, j in zip(x, y):
    arq.write(str(i) + '\t' + str(j) + '\n')
arq.close()
#------------------------------------------------------------------------------


# LEITURA DE ARQUIVOS   -------------------------------------------------------
# abrir 'dados_coletados.txt' para leitura ('r')
arq = open('dados_coletados.txt', 'r')

# lista todas as linhas exceto a primeira
linhas = arq.readlines()[1:]	
arq.close()
#------------------------------------------------------------------------------


# TRATANDO ENTRADA DE ARQUIVOS   ----------------------------------------------
x, y = [], []
for linha in linhas:
    aux = linha.split()			# quebrando string por espacos
    x.append( float(aux[0]) )
    y.append( float(aux[1]) )


# EXEMPLO DE REGRESSAO POLINOMIAL ---------------------------------------------
# nump.array eh muito melhor para parte numerica
x = np.array(x)
y = np.array(y)

grau = 3
# np.polyfit faz regressao polinomial por minimos quadrados
coefs = np.polyfit(x, y, grau)

# coefs contem os coeficientes de [x^3, x^2, x^1, x^0]
coefs = coefs[::-1]		# invertendo vetor de coeficientes
# agora, coefs contem os coeficientes de [x^0, x^1, x^2, x^3]

# print(coefs)

def polinomio(x, coefs):
	"""
	Funcao em que, dado um valor x e uma lista de coeficientes [c0, c1, c2, ...],
	retorna o valor da funcao P(x) = c0*x^0 + c1*x^1, c2*x^2 + ... 
	
	Exemplo:
	>>> polinomio(2, [1, 2, 3])		# 1*(2)^0 + 2*(2)^1 + 3*(2)^2 
	17
	"""
	# Obs.: o texto entre aspas triplas (""") no inici o da funcao eh 
	# sua documentacao e pode ser acessada usando help(polinomio), tente!

	#----- Uma forma de fazer (sem enumerate): -------
	y = 0
	for i, c in enumerate(coefs):
		y += c * x**i

	#----- Outra forma de fazer (sem enumerate): -------
	# for i in range(len(coefs)):
	#	y += coefs[i] * x**i

	return y

# EXEMPLO DE PLOT DE GRAFICO --------------------------------------------------
# plotar os tres conjuntos de dados sobre o eixo x
plt.plot(x, y				   , 'x' , label='Dados observados' )
plt.plot(x, polinomio(x, coefs), '-' , label='Minimos quadrados')
plt.plot(x, f(x)			   , '--', label='Modelo teorico'   )

# demais detalhes graficos...
plt.xlabel('Tempo (s)')				# incluir etiqueta do eixo x
plt.ylabel('Fluxo Magnetico (Wb)')	# incluir etiqueta do eixo y
plt.legend(loc='best')				# incluir legenda (no 'melhor' local)
plt.title('Regressao polinomial')	# incluir titulo do Grafico
plt.grid()							# incluir linhas de grade no grafico

# salvar grafico atual em 'Analise.png'
plt.savefig('Analise.png', dpi=200)

# mostrar grafico atual
plt.show()
