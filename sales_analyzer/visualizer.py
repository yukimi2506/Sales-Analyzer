import plotly.express as px

def grafico_vendas_por_produto(df):
    df_agrupado = df.groupby('Produto', as_index=False)['Valor Total'].sum()
    fig = px.bar(
        df_agrupado,
        x='Produto',
        y='Valor Total',
        title='Vendas por Produto',
        text='Valor Total',
        color='Produto',
        labels={'Valor Total': 'Faturamento (R$)', 'Produto': 'Produto'}
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.show()

def grafico_lucro_por_produto(df):
    df_agrupado = df.groupby('Produto', as_index=False)['Lucro'].sum()
    fig = px.bar(
        df_agrupado,
        x='Produto',
        y='Lucro',
        title='Lucro por Produto',
        text='Lucro',
        color='Produto',
        labels={'Lucro': 'Lucro (R$)', 'Produto': 'Produto'}
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.show()
