from sales_analyzer.loader import carregar_dados

def test_carregar_dados():
    df = carregar_dados('data/exemplo_vendas.csv')
    assert not df.empty
