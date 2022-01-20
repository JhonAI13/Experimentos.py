import matplotlib.pyplot as plt
import numpy as np

# Valores do Gráfico #
valores = np.array([35, 25, 25, 15])

# Itens do Gráfico #
itens = ['Maçãs', 'Bananas', 'Laranjas', 'Melancias']

# Espaço entre as "fatias" do gráfico #
expaço = [0.2, 0, 0, 0]

# Monta o Gráfico e depois o mostra na tela #
plt.pie(valores, labels=itens, explode=expaço, shadow=True)
plt.show()
