from sales_analyzer.analyzer import calcular_kpis
import pandas as pd

def test_calculo_kpis():
    data = {'Produto': ['A', 'A', 'B'], 'Valor Total': [100, 200, 300], 'Lucro': [10, 20, 30]}
    df = pd.DataFrame(data)
    kpis = calcular_kpis(df)
    assert kpis['faturamento'] == 600
    assert kpis['lucro'] == 60
    assert kpis['produto_mais_vendido'] == 'A'
