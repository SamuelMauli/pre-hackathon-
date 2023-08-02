class Sinistro:
    def __init__(self, id, status, tipo, motorista, cidade, data, modelo_carro, placa_carro, valor_carro, obs_carro):
        self.id = id
        self.status = status
        self.tipo = tipo
        self.motorista = motorista
        self.cidade = cidade
        self.data = data
        self.modelo_carro = modelo_carro
        self.placa_carro = placa_carro
        self.valor_carro = valor_carro
        self.obs_carro = obs_carro


class SistemaSinistros:
    def __init__(self):
        self.sinistros = []

    def cadastrar_sinistro(self, id_sinistro, status_sinistro, tipo_sinistro, motorista, cidade, data_sinistro,
                           modelo_carro, placa_carro, valor_carro, obs_carro):
        novo_sinistro = Sinistro(id_sinistro, status_sinistro, tipo_sinistro, motorista, cidade, data_sinistro,
                                 modelo_carro, placa_carro, valor_carro, obs_carro)
        self.sinistros.append(novo_sinistro)
        print("Sinistro cadastrado com sucesso!")

    def listar_sinistros(self):
        if not self.sinistros:
            print("Nenhum sinistro cadastrado.")
        else:
            print("Lista de Sinistros:")
            for idx, sinistro in enumerate(self.sinistros, start=1):
                print(f"ID do Sinistro: {sinistro.id}")
                print(f"Status: {sinistro.status}")
                print(f"Tipo de Sinistro: {sinistro.tipo}")
                print(f"Motorista: {sinistro.motorista}")
                print(f"Cidade: {sinistro.cidade}")
                print(f"Data do Sinistro: {sinistro.data}")
                print(f"Modelo do Carro: {sinistro.modelo_carro}")
                print(f"Placa do Carro: {sinistro.placa_carro}")
                print(f"Valor do Carro: {sinistro.valor_carro}")
                print(f"Obs. do Carro: {sinistro.obs_carro}")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    def editar_sinistro(self, indice, id_sinistro, status_sinistro, tipo_sinistro, motorista, cidade, data_sinistro,
                        modelo_carro, placa_carro, valor_carro, obs_carro):
        if 0 <= indice < len(self.sinistros):
            sinistro = self.sinistros[indice]
            sinistro.id = id_sinistro
            sinistro.status = status_sinistro
            sinistro.tipo = tipo_sinistro
            sinistro.motorista = motorista
            sinistro.cidade = cidade
            sinistro.data = data_sinistro
            sinistro.modelo_carro = modelo_carro
            sinistro.placa_carro = placa_carro
            sinistro.valor_carro = valor_carro
            sinistro.obs_carro = obs_carro
            print("Sinistro editado com sucesso!")
        else:
            print("Índice de sinistro inválido.")

    def excluir_sinistro(self, indice):
        if 0 <= indice < len(self.sinistros):
            del self.sinistros[indice]
            print("Sinistro excluído com sucesso!")
        else:
            print("Índice de sinistro inválido.")


def main(estado=None, pais=None):
    sistema = SistemaSinistros()

    while True:
        print("\nMenu:")
        print("1. Cadastrar sinistro")
        print("2. Listar sinistros")
        print("3. Editar sinistro")
        print("4. Excluir sinistro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("Preencha os dados do sinistro:")
            id_sinistro = int(input("Id do Sinistro: "))
            print("=-=-=-=-=-=-=-=")
            print(
                "1. Registrado\n2. Em Análise\n3. Aguardando Documentação\n4. Em Avaliação\n5. Aprovado\n6. Reprovado\n7. Em Processamento\n8. Finalizado")
            status_sinistro = input("Status do Sinistro (Digite o número correspondente): ")
            print("=-=-=-=-=-=-=-=")
            tipo_sinistro = input("Tipo de Sinistro: ")
            print("=-=-=-=-=-=-=-=")
            motorista = input("Motorista: ")
            print("=-=-=-=-=-=-=-=")
            cidade = input("Cidade: ")
            print("=-=-=-=-=-=-=-=")
            data_sinistro = input("Data do Sinistro: ")
            print("=-=-=-=-=-=-=-=")
            modelo_carro = input("Modelo do Carro: ")
            print("=-=-=-=-=-=-=-=")
            placa_carro = input("Placa do Carro: ")
            print("=-=-=-=-=-=-=-=")
            valor_carro = input("Valor do Carro: ")
            print("=-=-=-=-=-=-=-=")
            obs_carro = input("Obs. do Carro: ")

            local = f"{cidade}, {estado}, {pais}"  # Certifique-se de ter estado e pais definidos

            sistema.cadastrar_sinistro(id_sinistro, status_sinistro, tipo_sinistro, motorista, cidade, data_sinistro,
                                       modelo_carro, placa_carro, valor_carro, obs_carro)
        elif escolha == "2":
            sistema.listar_sinistros()
        elif escolha == "3":
            sistema.listar_sinistros()
            indice = int(input("Digite o índice do sinistro que deseja editar: ")) - 1
            data = input("Nova Data do Sinistro: ")
            tipo = input("Novo Tipo de Sinistro: ")
            local = input("Novo Local do Sinistro: ")
            sistema.editar_sinistro(indice, id_sinistro, status_sinistro, tipo_sinistro, motorista, cidade, data_sinistro,
                                    modelo_carro, placa_carro, valor_carro, obs_carro)
        elif escolha == "4":
            sistema.listar_sinistros()
            indice = int(input("Digite o índice do sinistro que deseja excluir: ")) - 1
            sistema.excluir_sinistro(indice)
        elif escolha == "5":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
