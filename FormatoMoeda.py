# Separador de milhar
print(f"{valor:,.2f}")               # 1,234.57 (padrão en_US)

br = f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(br)                            # R$ 1.999,90 (padrão brasileiro)

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print(locale.format_string("R$ %.2f", valor, grouping=True))  # R$ 1.234,57
