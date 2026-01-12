
a, b = 7, 3

# Qualquer expressão dentro de {}
print(f"Soma: {a + b}, Média: {(a + b)/2:.2f}")

# Condicional inline (ternário)
valor = -5
print(f"{'Negativo' if valor < 0 else 'Não negativo'}")

# Compreensão de listas
nums = [1, 2, 3, 4]
print(f"Pares: {[n for n in nums if n % 2 == 0]}")  # Pares: [2, 4]