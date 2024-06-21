opcao = -1

while opcao != 0:
    opcao = int(input("1. Sacar \n2. Extrato \n0. Sair \nDigite: "))
    
    if opcao == 1:
        print("Saque realizado!")
    elif opcao == 2:
        print("Aqui seu extrato!")
else: 
    print("Fim")