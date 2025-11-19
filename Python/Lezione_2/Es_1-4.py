# 1-4. Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga:

# 2
# 0
# 2
# 4

x: int = 2024

numero_str: str = str(x)

for i in numero_str:
    print(i)