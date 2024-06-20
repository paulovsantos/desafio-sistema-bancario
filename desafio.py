menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
numero_saques = 0


while True:  
    opcao = input(menu)
 
    if opcao == "d":
        valor_deposito = float(input("Digite o valor para depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                
    elif opcao == "s":
        valor_saque = float(input("Digite o valor para saque: "))
        
        if saldo == 0:
            print("Saldo insuficiente!")
        
        elif valor_saque > limite:
            print("Valor de saque não permitido")
            
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques excedido!")
            
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
                    
          
    elif opcao == "e":
        print("\n========Extrato========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=======================")
        
    elif opcao == "q":
        print("Sair")
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada!")
       