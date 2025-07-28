def calcular_kpis(df):
    total_faturamento = df['Valor Total'].sum()
    total_lucro = df['Lucro'].sum()
    produto_mais_vendido = df['Produto'].value_counts().idxmax()
    return {
        "faturamento": total_faturamento,
        "lucro": total_lucro,
        "produto_mais_vendido": produto_mais_vendido
    }
