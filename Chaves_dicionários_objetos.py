
dados = {"nome": "Maria", "idade": 30, "saldo": 1234.5}

# Acesso direto a dict
print(f"{dados['nome']} tem {dados['idade']} anos e saldo {dados['saldo']:.2f}")

# Objetos (atributos e métodos)
class Cliente:
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos
    def nivel(self):
        return "Gold" if self.pontos >= 1000 else "Silver"

c = Cliente("João", 1200)
print(f"{c.nome} é nível {c.nivel()} com {c.pontos} pontos.")
# Aninhamento de formatações