class Item:
    def __init__(self, nome, preco, quantidade=1):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class CarrinhoCompras:
    def __init__(self, limite_itens=10):
        self.itens = []
        self.limite_itens = limite_itens
        self.total = 0

    def adicionar_item(self, nome, preco, quantidade=1):
        """Adiciona um item ao carrinho"""
        if len(self.itens) >= self.limite_itens:
            print(f"Aviso: Limite de {self.limite_itens} itens atingido!")
            print("Não é possível adicionar mais itens.")
            return False

        novo_item = Item(nome, preco, quantidade)
        self.itens.append(novo_item)
        self.total += preco * quantidade
        print(f"{quantidade}x '{nome}' adicionado ao carrinho!")
        return True

    def calcular_total(self):
        self.total = sum(item.preco * item.quantidade for item in self.itens)
        return self.total

    def mostrar_carrinho(self):
        if not self.itens:
            print("Carrinho vazio!")
            return

        print("\n" + "=" * 40)
        print("CARRINHO DE COMPRAS")
        print("=" * 40)

        for i, item in enumerate(self.itens, 1):
            print(f"{i}. {item.nome:20} R$ {item.preco:.2f} x{item.quantidade}")

        print("-" * 40)
        print(f"Total: R$ {self.calcular_total():.2f}")
        print(f"Itens no carrinho: {len(self.itens)}/{self.limite_itens}")
        print("=" * 40)


class SistemaMercado:
    def __init__(self):
        self.carrinho = CarrinhoCompras(limite_itens=10)
        self.executando = True
        # Lista de produtos disponíveis
        self.produtos = {
            1: ("Arroz", 11.50),
            2: ("Óleo", 8.12),
            3: ("Bolacha", 3.50),
            4: ("Cerveja", 5.50),
            5: ("Sabão", 8.99),
            6: ("Bolo", 15.99),
            7: ("Macarrão", 9.99),
            8: ("Detergente", 22.99),
            9: ("Presunto", 5.99),
            10: ("Alface", 3.99),
        }

    def mostrar_menu(self):
        print("\n" + "=" * 40)
        print("MERCADO DO ZÉ")
        print("=" * 40)
        print("1. Adicionar item ao carrinho")
        print("2. Ver carrinho")
        print("3. Remover item do carrinho")
        print("4. Ver total da compra")
        print("5. Finalizar compra")
        print("6. Sair")
        print("=" * 40)

    def mostrar_produtos(self):
        print("\n" + "=" * 40)
        print("LISTA DE PRODUTOS DISPONÍVEIS")
        print("=" * 40)
        for codigo, (nome, preco) in self.produtos.items():
            print(f"{codigo}. {nome:20} R$ {preco:.2f}")
        print("=" * 40)

    def executar(self):
        while self.executando:
            self.mostrar_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_item()
            elif opcao == "2":
                self.carrinho.mostrar_carrinho()
            elif opcao == "3":
                self.remover_item()
            elif opcao == "4":
                print(f"\nTotal da compra: R$ {self.carrinho.calcular_total():.2f}")
            elif opcao == "5":
                self.finalizar_compra()
            elif opcao == "6":
                self.sair()
            else:
                print("Opção inválida! Tente novamente.")

    def adicionar_item(self):
        self.mostrar_produtos()
        try:
            codigo = int(input("Digite o número do produto: "))
            if codigo not in self.produtos:
                print("Produto inválido!")
                return

            nome, preco = self.produtos[codigo]
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= 0:
                print("Quantidade inválida!")
                return

            self.carrinho.adicionar_item(nome, preco, quantidade)

        except ValueError:
            print("Entrada inválida! Use números.")

    def remover_item(self):
        if not self.carrinho.itens:
            print("Carrinho vazio! Não há itens para remover.")
            return

        self.carrinho.mostrar_carrinho()

        try:
            indice = int(input("Digite o número do item a remover: ")) - 1
            if 0 <= indice < len(self.carrinho.itens):
                self.carrinho.itens.pop(indice)
                print("Item removido com sucesso!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Número inválido!")

    def finalizar_compra(self):
        if not self.carrinho.itens:
            print("Carrinho vazio! Adicione itens antes de finalizar.")
            return

        self.carrinho.mostrar_carrinho()
        confirmacao = input("\nDeseja finalizar a compra? (S/N): ").upper()

        if confirmacao == "S":
            print("\n" + "=" * 40)
            print("COMPRA FINALIZADA COM SUCESSO!")
            print(f"Total pago: R$ {self.carrinho.total:.2f}")
            print("Obrigado pela preferência!")
            print("=" * 40)
            self.carrinho = CarrinhoCompras()

    def sair(self):
        if self.carrinho.itens:
            print("\nAtenção! Você tem itens no carrinho.")
            print("Deseja mesmo sair sem finalizar a compra?")
            confirmacao = input("Digite 'S' para confirmar: ").upper()

            if confirmacao != "S":
                return

        self.executando = False
        print("\nObrigado por usar o Mercado!")


if __name__ == "__main__":
    print("Bem-vindo ao Mercado!")
    print("=" * 40)

    mercado = SistemaMercado()
    mercado.executar()
