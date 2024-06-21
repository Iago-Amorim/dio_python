import os

menu = """
========= MENU =========

    [d] Deposito
    [s] Saque
    [e] Extrato
    [a] Avançar o dia
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3
dia = 1

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        while True:
            try:
                deposito = float(input(f"""
======= DEPOSITO =======

    Saldo: R$ {saldo:.2f}
    
    [0] Sair
    
    Deposito: R$ """))
        
                if deposito == 0:
                    break
                elif deposito > 0:
                    extrato += f"""    R$ {deposito:.2f}, Dia {dia}.
"""
                    saldo += deposito
                    print(f"""
    -> Deposito aprovado! <-
                      
    Saldo Atual: R$ {saldo:.2f}
""")
                    os.system("pause")
                    break
                else: 
                    print("""
ERRO: Digite um valor positivo.""")
                    os.system("pause")
            except:
                print("""
ERRO: Digite somente números e com valor positivo.""")
                os.system("pause")
        
    elif opcao == "s":
        if numero_saque < LIMITE_SAQUES:
            numero_saque += 1
            while True:
                try:
                
                    saque = float(input(f"""
======== SAQUE =========

    Saldo: R$ {saldo:.2f}
    
    [0] Sair
    
    Saque: R$ """))
        
                    if saque == 0:
                        numero_saque -= 1
                        break
                    elif saque > saldo:
                        print("""
ERRO: Digite um valor menor que o saldo.""")
                        os.system("pause")
                    elif saque > 0:
                        extrato += f"""    R$ -{saque:.2f}, Dia {dia}.
"""
                        saldo -= saque
                        print(f"""
    -> Saque de R$ {saque:.2f} foi aprovado! <-
                      
    Saldo Atual: R$ {saldo:.2f}
""")
                        os.system("pause")  
                        break
                    else: 
                        print("""
ERRO: Digite um valor positivo.""")
                        os.system("pause")
                except:
                    print("""
ERRO: Digite somente números e com valor positivo.""")
                    os.system("pause")
        else:
            print("""
======== SAQUE =========

    Limite saque diário alcançado.
""")
            os.system("pause")
        
    elif opcao == "e":
        print(f"""
======= EXTRATO ========

{extrato}
    Saldo Atual: R$ {saldo:.2f}
""")
        os.system("pause")
        
    elif opcao == "a":
        dia += 1
        numero_saque = 0
        print(f"""
========================

Dia {dia}. 
""")
        os.system("pause")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")