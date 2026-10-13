pacientes = []

def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")

    nome = input("Nome: ").strip()

    if not nome:
        print("O nome não pode ficar vazio.")
        return

    try:
        idade = int(input("Idade: "))

        if idade < 0:
            print("A idade não pode ser negativa.")
            return

    except ValueError:
        print("Digite uma idade válida.")
        return

    telefone = input("Telefone: ").strip()

    if not telefone:
        print("O telefone não pode ficar vazio.")
        return

    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pacientes.append(paciente)

    print("Paciente cadastrado com sucesso!")


def mostrar_estatisticas():
    print("\n--- Estatísticas dos Pacientes ---")

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    quantidade = len(pacientes)
    media_idade = sum(p["idade"] for p in pacientes) / quantidade
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"Total de pacientes: {quantidade}")
    print(f"Idade média: {media_idade:.1f} anos")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")


def buscar_paciente():
    print("\n--- Buscar Paciente ---")

    nome_busca = input("Digite o nome ou parte do nome: ").strip().lower()

    if not nome_busca:
        print("Digite um nome para pesquisar.")
        return

    encontrados = [
        p for p in pacientes
        if nome_busca in p["nome"].lower()
    ]

    if encontrados:
        for paciente in encontrados:
            print("\nNome:", paciente["nome"])
            print("Idade:", paciente["idade"])
            print("Telefone:", paciente["telefone"])
    else:
        print("Nenhum paciente encontrado.")


def listar_pacientes():
    print("\n--- Lista de Pacientes ---")

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    for numero, paciente in enumerate(pacientes, start=1):
        print(f"\nPaciente {numero}")
        print("Nome:", paciente["nome"])
        print("Idade:", paciente["idade"])
        print("Telefone:", paciente["telefone"])


def menu():
    while True:
        print("\n===== CLÍNICA VIDA+ =====")
        print("1 - Cadastrar paciente")
        print("2 - Ver estatísticas")
        print("3 - Buscar paciente")
        print("4 - Listar pacientes")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            mostrar_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print("Sistema encerrado. Até logo!")
            break
        else:
            print("Opção inválida. Escolha de 1 a 5.")


if __name__ == "__main__":
    menu()