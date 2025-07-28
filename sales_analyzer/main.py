from sales_analyzer.loader import carregar_dados
from sales_analyzer.analyzer import calcular_kpis
from sales_analyzer.visualizer import grafico_vendas_por_produto, grafico_lucro_por_produto
from sales_analyzer.report import gerar_pdf
import sys

if __name__ == '__main__':
    caminho = sys.argv[1]
    df = carregar_dados(caminho)
    kpis = calcular_kpis(df)
    grafico_vendas_por_produto(df)
    grafico_lucro_por_produto(df)
    gerar_pdf(kpis, 'relatorio.pdf')
