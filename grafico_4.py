import matplotlib.pyplot as plt
import pandas as pd

    #  BOXPLOT DOS DADOS:

read = pd.read_csv("a2_MANCHAS.csv")

plt.title('Número de manchas solares de Wolfer;\n', color = 'Black')
plt.ylabel('Manchas(Wolfer)')
read.boxplot(column = 'manchas')
plt.grid(True)

plt.savefig('quarto_grafico.png')

plt.show()
