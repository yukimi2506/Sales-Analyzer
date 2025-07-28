from sales_analyzer.visualizer import grafico_vendas_por_produto
import pandas as pd

def test_grafico():
    data = {'Produto': ['A', 'A', 'B'], 'Valor Total': [100, 200, 300]}
    df = pd.DataFrame(data)
    grafico_vendas_por_produto(df)
