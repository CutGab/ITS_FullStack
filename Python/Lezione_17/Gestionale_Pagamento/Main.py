# DRIVER

from PagamentoContanti import PagamentoContanti
from PagamentoCartaDiCredito import PagamentoCartaDiCredito

# Pagamenti in contanti
p1 = PagamentoContanti(150.00)
p1.dettagliPagamento()
p1.inPezziDa()

print()

p2 = PagamentoContanti(95.25)
p2.dettagliPagamento()
p2.inPezziDa()

print("\n" + "-"*50 + "\n")

# Pagamenti con carta di credito
c1 = PagamentoCartaDiCredito(200.00, "Mario Rossi", "12/24", "1234567890123456")
c1.dettagliPagamento()

print()

c2 = PagamentoCartaDiCredito(500.00, "Luigi Bianchi", "01/25", "6543210987654321")
c2.dettagliPagamento()
