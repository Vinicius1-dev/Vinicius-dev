

import pandas as pd
import numpy as np

dados_vendas = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam'],
    'Vendas_Jan': [150, 320, 280, 95, 180],
    'Vendas_Fev': [180, 340, 250, 110, 200],
    'Vendas_Mar': [200, 380, 290, 130, 220]
}

df = pd.DataFrame(dados_vendas)

df['Total_Vendas'] = df['Vendas_Jan'] + df['Vendas_Fev'] + df['Vendas_Mar']

df['Media_Mensal'] = df['Total_Vendas'] / 3

df_ordenado = df.sort_values('Total_Vendas', ascending=False)

print("=" * 60)
print("ANÁLISE DE VENDAS - PRIMEIRO TRIMESTRE 2025")
print("=" * 60)
print("\n📊 Dados Completos:")
print(df_ordenado.to_string(index=False))

print("\n\n🏆 Produto Mais Vendido:")
print(f"{df_ordenado.iloc[0]['Produto']} - {df_ordenado.iloc[0]['Total_Vendas']:.0f} unidades")

print("\n📈 Produto com Maior Crescimento:")
crescimento = ((df['Vendas_Mar'] - df['Vendas_Jan']) / df['Vendas_Jan'] * 100)
idx_maior_crescimento = crescimento.idxmax()
print(f"{df.loc[idx_maior_crescimento, 'Produto']} - {crescimento[idx_maior_crescimento]:.1f}% de crescimento")

print("\n💰 Total Geral de Vendas:", df['Total_Vendas'].sum(), "unidades")
print("=" * 60)
