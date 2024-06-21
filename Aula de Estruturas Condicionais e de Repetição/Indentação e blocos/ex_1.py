def sacar (valor):
    saldo = 500
    
    if valor <= saldo:
        print("Valor sacado!")
        print("Pode retirar o dinheiro.")
        
    print("Obrigado por ser nosso Cliente!")
        
sacar(100)
sacar(600)

def deposito (valor):
    saldo = 500
    if valor > 0:
        saldo += valor
        print(saldo)

deposito(1000)