import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart(csv_file_path):
    portfolio_data = pd.read_csv(csv_file_path)
    
    portfolio_data['Valore in EUR'] = portfolio_data['Valore in EUR'].str.replace(',', '.').astype(float)

    plt.figure(figsize=(10, 7))
    plt.pie(portfolio_data['Valore in EUR'], labels=portfolio_data['Prodotto'], autopct='%1.1f%%', startangle=140)
    plt.title('Distribuzione del Portafoglio Investimenti')
    plt.axis('equal')

    pie_chart_path = 'portfolio_pie_chart.png'
    plt.savefig(pie_chart_path)

    plt.show()
    
    return pie_chart_path

csv_file_path = 'Portfolio.csv'

pie_chart_path = create_pie_chart(csv_file_path)
