
produto = "Notebook"
preco = 3599.99

# Preenchimento com caracteres customizados
print(f"{produto:.<20}")             # "Notebook............"
print(f"{produto:.>20}")             # "............Notebook"
print(f"{produto:.^20}")             # ".....Notebook......"

# Coluna de preços alinhada
print(f"{'Preço:':<10} R$ {preco:>10.2f}")  # "Preço:     R$   3599.99"
print(f"{'Preço:':<10} R$ {preco:.^10.2f}")  # "Preço:     R$ ..3599.99.."