menu = """

[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
extrato_depositos = []
extrato_saques = []

while True:
    opcao = input(menu)

    if opcao == "d":
        saldo = float(input("Qual o valor a ser depositado?\n"))
        if saldo > 0:
          extrato_depositos.append(saldo)
        else:
           print("Operação inválida, insira um valor positivo.")
            
                 

    elif opcao == "s":
        saque = float(input("Qual o valor de saque?\n"))

        if numero_saques != LIMITE_SAQUES:
            if saque <= limite:
                if saque <= saldo: 
                  saldo -= saque
                  extrato_saques.append(saque)
                  numero_saques += 1
                else: 
                  print("Saldo insulficiente para saque.")
            else:
               print("Seu limite de saque é de R$500, por favor insira um valor igual ou abaixo do seu limite.")
        else: 
           print("Limite de saque diário excedido.")

    elif opcao == "e":
        
        titulo_depositos = " DEPOSITOS "
        string_extrato_depositos = []
        contador_deposito = 0

        for contador_deposito in range(len(extrato_depositos)):
           string_extrato_depositos.append(f"R$ {extrato_depositos[contador_deposito]}")
           contador_deposito += 1

        lista_depositos = '\n'.join(string_extrato_depositos)

        titulo_saques = " SAQUES "
        string_extrato_saques = []
        contador_saques = 0

        for contador_saques in range(len(extrato_saques)):
           string_extrato_saques.append(f"R$ -{extrato_saques[contador_saques]}")
           contador_saques += 1

        lista_saques = '\n'.join(string_extrato_saques)


        titulo_extrato = " EXTRATO "
        extrato = f"""
        {titulo_extrato}
                      
        {titulo_depositos}
        {lista_depositos}
                           
        {titulo_saques}
        {lista_saques}

        Saldo: R$ {sum(extrato_depositos) - sum(extrato_saques)}                   
        """
        print(extrato)

    elif opcao == "q":
      print("Obrigado por utilizar o nosso sistema.d")
      break

    else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")   
