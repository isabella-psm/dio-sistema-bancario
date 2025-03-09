def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R${valor:.2f} reaizado com sucesso.")
    else:
        print("Valor inválido. O valor deve ser positivo.")
    return saldo, extrato


def sacar(saldo, extrato, saques_realizados):
    LIMITE_SAQUE = 3
    LIMITE_VALOR_SAQUE = 500

    if saques_realizados >= LIMITE_SAQUE:
        print("Limite de saque diário atingido.")
        return saldo, extrato, saques_realizados

    saldo = float(input("Informe o valor do saque: "))
    if saldo <= 0:
        print("Valor inválido. O valor deve ser positivo.")
        
    elif saldo > LIMITE_VALOR_SAQUE:
        print(f"Valor máximo por saque é R${LIMITE_VALOR_SAQUE}.")
        
    elif saldo > saldo:
        print("Saldo insuficiente.")
        
    else:
        saldo -= saldo
        extrato.append(f"Saque: R$ {saldo:.2f}")
        saques_realizados += 1
        print(f"Saque de R${saldo:.2f} reaizado com sucesso.")
    return saldo, extrato, saques_realizados


def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não houve movimentações na conta.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"Saldo atual: R${saldo:.2f}")


def main():
    saldo = 0
    extrato = []
    LIMITE_SAQUES = 3
    saques_realizados = 0

    while True:
        print("\n========== MENU ==========")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, saques_realizados = sacar(saldo, extrato, saques_realizados)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


main()
