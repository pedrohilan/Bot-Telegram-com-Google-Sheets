import pandas as pd
import matplotlib.pyplot as plt
import sys

args = sys.argv

if len(sys.argv) != 2:
	print("Use: python3 main.py 'dados.xlsx'")
	sys.exit(1)

data_file = args[1]

def chart1(data_file, title):

    x = pd.read_excel(data_file)
    plt.pie(x[x.columns[1]], autopct=lambda p:f'{p:.0f}% ( {p*sum(x[x.columns[1]])/100 :.0f} )')
    #plt.legend(title='Nomes')
    plt.title(title)
    plt.legend(x[x.columns[0]], loc='lower center')
    plt.savefig(title+'.png')

chart1(data_file, 'Buscas ativas por Tipo')