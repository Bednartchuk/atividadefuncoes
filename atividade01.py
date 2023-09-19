## Continuação do código de slide

import os  
 lista = [] 
 os.system("cls") 
  
 while True: 
     print("Selecione uma opção") 
     opcao = input(" [i]nseir [a]pagar [l]istar [e]ditar [s]air: ") 
  
     if opcao == "i": 
         os.system("cls") 
         valor = input("Digite o valor: ") 
         lista.append(valor) 
         print("Valor inserido com sucesso!") 
         print("--------------------------------") 
  
     elif opcao == "a": 
         os.system("cls") 
         apagar = input("Qual valor deseja apagar: ") 
  
         try: 
             lista.remove(apagar) 
             print("Valor apagado com sucesso!") 
             print("--------------------------------") 
         except ValueError: 
             print("Valor não encontrado!!!") 
             print("--------------------------------") 
  
     elif opcao == "l": 
         os.system("cls") 
         if len(lista) == 0: 
             print("Lista vazia") 
         else: 
             for i, listageral in enumerate(lista): 
                 print(f"{i}: {listageral}") 
         print("--------------------------------") 
  
     elif opcao == "e": 
         os.system("cls") 
         editar = int(input("Qual índice do valor deseja editar: ")) 
         if editar >= 0 and editar < len(lista): 
             novo_valor = input("Digite o novo valor: ") 
             lista[editar] = novo_valor 
             print("Valor editado com sucesso") 
         else: 
             print("Índice inválido!") 
         print("--------------------------------") 
  
     elif opcao == "s": 
         os.system("cls") 
         break 
  
     else: 
         os.system("cls") 
         print("Opção inválida!") 
         print("--------------------------------") 
 
## código das funções

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