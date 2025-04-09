usuarios = []
contas = []
AGENCIA = "0001"


def main():
    while True:
        print("\n=== MENU ===")
        print("1. Criar usuário")
        print("2. Criar conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            extrato()
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")


def criar_usuario():
    cpf = input("CPF (somente números): ")
    if any(u["cpf"] == cpf for u in usuarios):
        print("Usuário já existe!")
        return

    usuarios.append(
        {
            "nome": input("Nome: "),
            "cpf": cpf,
            "data_nascimento": input("Data nasc. (dd/mm/aaaa): "),
            "endereco": input("Endereço (logradouro, nro - bairro - cidade/UF): "),
        }
    )
    print("Usuário criado!")


def criar_conta():
    cpf = input("CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("Usuário não encontrado!")
        return

    contas.append(
        {
            "agencia": AGENCIA,
            "numero": len(contas) + 1,
            "usuario": usuario,
            "saldo": 0,
            "extrato": [],
            "saques_hoje": 0,
        }
    )
    print(f"Conta criada! Número: {len(contas)}")


def selecionar_conta():
    cpf = input("CPF do titular: ")
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            return conta
    print("Conta não encontrada!")
    return None


def depositar():
    conta = selecionar_conta()
    if not conta:
        return

    valor = float(input("Valor para depositar: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado!")
    else:
        print("Valor inválido!")


def sacar():
    conta = selecionar_conta()
    if not conta:
        return

    if conta["saques_hoje"] >= 3:
        print("Limite de saques atingido!")
        return

    valor = float(input("Valor para sacar: "))

    if valor > 500:
        print("Limite por saque: R$ 500")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente!")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        conta["saques_hoje"] += 1
        print("Saque realizado!")
    else:
        print("Valor inválido!")


def extrato():
    conta = selecionar_conta()
    if not conta:
        return

    print("\n=== EXTRATO ===")
    for mov in conta["extrato"]:
        print(mov)
    print(f"Saldo: R$ {conta['saldo']:.2f}")


if __name__ == "__main__":
    main()
