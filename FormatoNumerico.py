
valor = 1234.56789

# Casas decimais fixas
print(f"{valor:.2f}")                # 1234.57

# Largura mínima + alinhamento
print(f"{valor:>12.2f}")             # "     1234.57" (direita, largura 12)
print(f"{valor:<12.2f}")             # "1234.57     " (esquerda)
print(f"{valor:^12.2f}")             # "   1234.57   " (centralizado)

# Notação científica
print(f"{valor:.3e}")                # 1.235e+03

# Preenchimento com zeros
numero = 42
print(f"{numero:05d}")               # 00042

# Sinal sempre visível
saldo = -15.5
credito = 15.5
print(f"{saldo:+.2f}")               # -15.50
print(f"{credito:+.2f}")             # +15.50

# Percentual (multiplica por 100 e adiciona %)
taxa = 0.0765
print(f"{taxa:.2%}")                 # 7.65%
