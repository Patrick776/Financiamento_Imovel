import pandas as pd

def calcular_financiamento():

    #solicitar informações do usuário
    valor_casa = float(input("Digite o valor da casa: R$ "))
    salario = float(input("Digite o seu salário: R$ "))
    prazo_anos = int(input("Digite o prazo em anos para pagamento: "))

    #Cálculo da prestação mensal
    prestacao = valor_casa / (prazo_anos * 12)
    if prestacao <= 0.3 * salario:
        print("Financiamento aprovado! Prestação mensal: R$", prestacao)
    else:
        print("Financiamento negado. A prestação excede 30% do salário.")

    #Opções de data de vencimento
    datas_vencimento = [1, 10, 15, 20, 30]
    print("Opções de data de vencimento:", datas_vencimento)

    #Opção de desconto por pagamento antecipado
    desconto_antecipado = 0.03
    print(f"Desconto por pagamento antecipado: {desconto_antecipado * 100:.2f}%")

    #Opção de quitação com desconto
    desconto_quitacao = 0.10
    print(f"Desconto por quitação antecipada: {desconto_quitacao * 100:.2f}%")

    #Coleta dos dados do cliente
    nome = input("Nome: ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    emprego = input("Empregado ou Desempregado: ")
    renda = float(input("Renda do cliente: R$ "))

    #verificação da renda
    if renda >= 4500:
        print("Renda aprovada!")
    else:
        print("Renda insuficiente. Financiamento não aprovado.")

    #Criar tabela no Excel
    dados_cliente = {
        "Nome": [nome],
        "CPF": [cpf],
        "RG": [rg],
        "Data de Nascimento": [data_nascimento],
        "Emprego": [emprego],
        "Renda": [renda]
    }
    df = pd.DataFrame(dados_cliente)
    df.to_excel("cadastro_cliente.xlsx", index=False)
    print("Cadastro salvo em cadastro_cliente.xlsx")

    #Mensagem de agradecimento
    print("Obrigado por utilizar a simulação de financiamento!")

#Executar o programa
calcular_financiamento()