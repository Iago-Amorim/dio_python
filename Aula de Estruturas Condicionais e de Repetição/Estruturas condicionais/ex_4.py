saldo = 200

saque = float(input("Digite o valor: "))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")