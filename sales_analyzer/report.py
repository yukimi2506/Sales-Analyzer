from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def gerar_pdf(kpis, caminho_saida):
    c = canvas.Canvas(caminho_saida, pagesize=letter)
    c.drawString(100, 750, 'Relatório de Vendas')
    c.drawString(100, 700, f"Faturamento Total: R$ {kpis['faturamento']}")
    c.drawString(100, 680, f"Lucro Total: R$ {kpis['lucro']}")
    c.drawString(100, 660, f"Produto Mais Vendido: {kpis['produto_mais_vendido']}")
    c.save()
