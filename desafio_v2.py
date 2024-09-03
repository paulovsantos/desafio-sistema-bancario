import textwrap


def menu():
        menu = """\n    
        ================ MENU ================

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    
    => """
        
        return input(textwrap.dedent(menu))
    
saldo = 0.0
extrato = ""

def depositar(valor_deposito, /):
    global saldo, extrato
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"  
        
def sacar(*, valor_saque):
    global saldo, extrato
    
    if valor_saque > 0:
        saldo -=valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"  
        

def main():
    global saldo, extrato
    
    while True:
         opcao = menu()

         if opcao == "d":
            valor_deposito = float(input("Digite um valor de depósito: "))
            depositar(valor_deposito)
            
         elif opcao =="s":
             valor_saque = float(input("Digite um valor de saque: "))
             sacar(valor_saque=valor_saque)
    
            
         elif opcao == "e":
             print("\n========Extrato========")
             print("Não foram realizadas movimentações." if not extrato else extrato)
             print(f"\nSaldo atual: R$ {saldo:.2f}")
             break
                        
if __name__ == "__main__":
            main()
