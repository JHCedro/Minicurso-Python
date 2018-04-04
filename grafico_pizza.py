import numpy as np
import matplotlib.pyplot as plt

c = [0.2, 0.5, 0.6, 4.0]	# proporcoes
nomes = ['feijao', 'arroz', 'carne', 'batata']
cores = ['maroon', 'floralwhite', 'lightcoral', 'goldenrod']
# DICA: https://matplotlib.org/examples/color/named_colors.html
destaque = (0, 0.3, 0, 0.1)

plt.pie(c, labels=nomes, colors = cores, explode = destaque)

plt.axis('equal')
plt.show()
