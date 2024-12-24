import pandas as pd
import matplotlib.pyplot as plt
def mais_vendidos(Filmes):

    df = pd.DataFrame(Filmes)
    df.dropna(inplace=True)
    df.fillna(0, inplace=True)
    df.plot(x='nome_filme', y='quantidade',kind='bar')
    plt.title('Vendas de ingressos')
    plt.xlabel('nome_filme')
    plt.ylabel('quantidade')
    plt.show()
    return Filmes