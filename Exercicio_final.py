import matplotlib.pyplot as plt
import numpy as np

# GERANDO ARQUIVOS DE ENTRADA ---------------------
f = lambda x : x**3 - 13.0/5.0 * x + 0.95
x = np.linspace(-2, 2, 50)
# array de valores aleatorios
ruido = 0.8 * np.random.randn(50)
y = f(x) + ruido


# ESCRITA EM ARQUIVOS   --------------------------
arq = open('dados_coletados.txt', 'w')	# abrir para escrita ('w')
arq.write('X \t Y \n')
for i, j in zip(x, y):
    arq.write(str(i) + '\t' + str(j) + '\n')
arq.close()
#--------------------------------------------------


# LEITURA DE ARQUIVOS   ---------------------------
arq = open('dados_coletados.txt', 'r')	# abrir para escrita ('w')
linhas = arq.readlines()[1:]	# ignora a primeira linha
arq.close()
#--------------------------------------------------


# TRATANDO ENTRADA DE ARQUIVOS   ------------------
x, y = [], []
for linha in linhas:
    aux = linha.split()
    x.append( float(aux[0]) )
    y.append( float(aux[1]) )


# EXEMPLO DE REGRESSAO POLINOMIAL -----------------
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
	'''Funcao que dado um valor x e um array de coeficientes [c0, c1, c2, ...]
		retorna o valor da funcao P(x) = c0*x^0 + c1*x^1, c2*x^2 + ... 
		Exemplo: polinomio(2, [1, 2, 3]) --> 1*(2)^0 + 2*(x)^1 + 3*(x)^2 '''
	# Obs.: o texto entre aspas triplas (''') no inicio da funcao e' sua documentacao
	#	e pode ser acessada usando help(polinomio)

	y = 0
	for i, c in enumerate(coefs):
		y += c * x**i

	#----- Outra forma de fazer: -------
	# for i in range(len(coefs)):
	#	y += coefs[i] * x**i

	return y

# EXEMPLO DE PLOT DE GRAFICO ----------------------
plt.plot(x, y, 'x', label='Dados observados')
plt.plot(x, polinomio(x, coefs), label='Minimos quadrados')
plt.plot(x, f(x), '--', label='Modelo teorico')
plt.xlabel('Tempo (s)')
plt.ylabel('Fluxo Magnetico (Wb)')
plt.legend(loc='best')
plt.title('Regressao polinomial')
plt.grid()
plt.savefig('Analise.png', dpi=200)
plt.show()
