from pacoteExemplo.reajust import reajustInflation, reajustDeflation

p1 = 49.90
print('Preço do Produto: {} sem inflação'.format(p1))
print('Preço do Produto: {:.2f} com inflação de {:.2f}%'.format(reajustInflation(p1,8),8))
print('Preço do Produto: {:.2f} com deflação de {:.2f}%'.format(reajustDeflation(p1,-12),-12))
