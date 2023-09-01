def BemVindo():
    print("Bem Vindo a turma de Analise")

BemVindo()

def BemVindoDiferenciado(nome):
    print(f"Bem Vindo! {nome} Já estudou hoje?")

nome_da_pessoa = "Gustavo"
BemVindoDiferenciado(nome_da_pessoa)

def calculo_retangulo(largura, altura):
    area = largura * altura
    return area

largura_do_retangulo = 5
altura_do_retangulo = 3
area_calculada = calculo_retangulo(largura_do_retangulo, altura_do_retangulo)
print(f"A área do retângulo é: {area_calculada} unidades quadradas.")