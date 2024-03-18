from database import despesas, contas
import pprint  # biblioteca para imprimir dados de forma mais amigável

def menu():
    while True:
        print("""
        Projeto de software Crud
        ========================
        [1] Adicionar uma despesa
        [2] Ver despesas 
        [3] Alterar despesas
        [4] Apagar despesas
        --------------------
        [5]Adicionar Conta
        [6]Ver conta
        [7]Alterar Conta
        [8]Apagar Conta
        --------------------
        [0] Sair
    """)
        try:
            user_select = int(input("O que deseja fazer: "))
            if user_select == 1:
                funcao_adicionar_despesa()
            elif user_select == 2:
                funcao_ver_despesas()
            elif user_select == 3:
                funcao_alterar_despesas()
            elif user_select == 4:
                funcao_apagar_despesas()


            elif user_select == 5:
                funcao_adicionar_conta()
            elif user_select == 6:
                funcao_ver_conta()
            elif user_select == 7:
                funcao_alterar_conta()
            elif user_select == 8:
                funcao_apagar_conta()
            elif user_select == 0:
                break
            else:
                print("Alternativa incorreta")
        except ValueError:
            print("Por favor, insira um número válido.")

def funcao_adicionar_despesa():
    try:
        id_despesa = int(input("ID da despesa: "))
        data = input("Data da despesa (XX/XX/XXXX): ")
        descricao = input("Descrição da despesa: ")
        conta = input("Conta da despesa: ")
        valor = float(input("Valor da despesa: "))
        pago = input("A despesa foi paga? [S/N]: ").upper()

        despesa = {"id": id_despesa, "data": data, "descricao": descricao, "conta": conta, "valor": valor, "pago": pago}
        despesas.append(despesa)
        print("Despesa adicionada com sucesso.")
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número para o ID da despesa e o valor.")

def funcao_ver_despesas():
    pprint.pprint(despesas)

def funcao_alterar_despesas():
    try:
        id_despesa = int(input("Digite o ID da despesa que deseja alterar: "))
        for despesa in despesas:
            if despesa["id"] == id_despesa:
                print("""
                O que deseja alterar?
                [1] Data
                [2] Descrição
                [3] Conta
                [4] Valor
                [5] Pago/Não pago""")
                user_select = int(input("Digite o número da opção desejada: "))
                if user_select == 1:
                    despesa["data"] = input("Nova data da despesa (XX/XX/XXXX): ")
                elif user_select == 2:
                    despesa["descricao"] = input("Nova descrição da despesa: ")
                elif user_select == 3:
                    despesa["conta"] = input("Nova conta da despesa: ")
                elif user_select == 4:
                    despesa["valor"] = float(input("Novo valor da despesa: "))
                elif user_select == 5:
                    despesa["pago"] = input("A despesa foi paga? [S/N]: ").upper()
                else:
                    print("Opção inválida.")
                print("Despesa alterada com sucesso.")
                break
        else:
            print("Despesa não encontrada.")
    except ValueError:
        print("Por favor, insira um número válido.")

def funcao_apagar_despesas():
    try:
        id_despesa = int(input("Digite o ID que deseja apagar: "))
        for despesa in despesas:
            if despesa['id'] == id_despesa:
                despesas.remove(despesa)
                print("Despesa apagada com sucesso.")
                break
        else:
            print("Despesa não encontrada.")
    except ValueError:
        print("Por favor, insira um número válido.")



# a partir desse ponto do código está apenas as funções de contas
    
def funcao_adicionar_conta():
    try:
        id_conta = int(input("ID da despesa: "))
        nome = input("Nome da conta: ")
        valor = float(input("Valor da despesa: "))
        conta = {"id": id_conta, "nome":nome,  "valor": valor}
        contas.append(conta)
        print("Conta adicionada com sucesso!")
    except ValueError:
        print("error")

def funcao_ver_conta():
    try:
        pprint.pprint(contas)
    except ValueError:
        print("error")

def funcao_alterar_conta():
    try:
        id_conta = int(input("Digite o ID da despesa que deseja alterar: "))
        for conta in contas:
            if conta["id"] == id_conta:
                print("""
                O que deseja alterar?
                [1] Nome
                [2] Valor""")
                user_select = int(input("Digite o número da opção desejada: "))
                if user_select == 1:
                    conta["nome"] = input("Digite o novo nome: ")
                elif user_select == 2:
                    conta["valor"] = input("Digite o novo valor: ")
                else:
                    print("Opção inválida.")
                print("Conta alterada com sucesso.")
                break
        else:
            print("Conta não encontrada.")
    except ValueError:
        print("Por favor, insira um número válido.")

def funcao_apagar_conta():
    try:
        id_conta = int(input("Digite o ID que deseja apagar: "))
        for conta in contas:
            if conta['id'] == id_conta:
                contas.remove(conta)
                print("Conta apagada com sucesso.")
                break
        else:
            print("Conta não encontrada.")
    except ValueError:
        print("Por favor, insira um número válido.")