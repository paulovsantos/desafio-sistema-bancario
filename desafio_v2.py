import textwrap

def menu():
        menu = """\n    
        ================ MENU ================

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    
    => """
        return input(textwrap.dedent(menu))
    
saldo = 0.0
extrato = ""
usuarios = []
contas = []
AGENCIA = "0001"

def depositar(valor_deposito, /):
    global saldo, extrato
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"  
        print(f"Depósito de R$ {valor_deposito:.2f}, efetuado com sucesso!")
    else:
        print("Valor informado não confere! Tente novamente.")
    return saldo, extrato
        
def sacar(*, valor_saque):
    global saldo, extrato
    
    if valor_saque > 0:
        saldo -=valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"  
        print(f"Saque de R$ {valor_saque:.2f}, efetuado com sucesso!")
        
def criar_usuario(usuarios):
    #global usuarios
    
    cpf = input("informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já existe um usuário com este CPF!")
        return
    
    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    
    usuarios.append({ "nome": nome, "data_nascimento": data_nascimento, "cpf": cpf })
    
    print("Usuário cadastrado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado!") 
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']} 
            Titular:\t{conta['usuario']['nome']}
        """
        
        print("=" * 100)
        print(textwrap.dedent(str(linha)))

              
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
             print(f"\nSaldo disponível: R$ {saldo:.2f}")
            
         
         elif opcao == "nu":
             criar_usuario(usuarios)
             
         elif opcao == "nc":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)
             
             if conta:
                 contas.append(conta)
                 
         elif opcao == "lc":
             listar_contas(contas)
             break  
                        
if __name__ == "__main__":
            main()
