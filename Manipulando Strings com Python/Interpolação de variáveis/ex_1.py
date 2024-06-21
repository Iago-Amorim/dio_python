nome = "Iago"
idade = 22
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem)) 

print()

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print()

print("Olá, me chamo {1}. Eu tenho {2} anos de idade, trabalho como {3} e estou matriculado no curso de {0}.".format(linguagem, nome, idade, profissao))

print()

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(linguagem=linguagem, nome=nome, idade=idade, profissao=profissao))

print()

pessoa = {
    "nome": "Iago",
    "idade": 22,
    "profissao": "Programador",
    "linguagem": "Python"
}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

print()

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")