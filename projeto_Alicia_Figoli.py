#Cadastro de dados pessoais/Salvar dados captados em csv
import csv
import os

#Lista de cadastros
cadastros = []

#Função para exibir o menu
def exibir_menu():
    print("Menu:")
    print("1. Criar novo cadastro:")
    print("2. Listar cadastros salvos:")
    print("3. Atualizar cadastro:")
    print("4. Deletar cadastro:")
    print("5. Sair")

#Função criar um novo cadastro
def criar_cadastro():
    print("Dados cadastrais")
    nome = input("Digite o nome do cadastro: ")
    idade = input(" Digitte a idade: ")
    genero = input("Digite o gênero:")
    cpf = input("Digite o CPF(apenas o número): ")
    email = input("Digite o e-mail: ")
    telefone = input("Digite o telefone com o DDD: ")
    cadastro = {'Nome': nome, 'Idade': idade, 'Gênero': genero, 'CPF': cpf, 'Email': email, 'Telefone': telefone}
    cadastros.append(cadastro)
    print("Cadastro criado com sucesso!")

#Função para listar os cadastros
def listar_cadastros():
    if not cadastros:
      print("Nenhum cadastro em sistema.")
    else:
          for cadastro in cadastros:
              print(cadastro)

#Função para alterar um cadastro
def alterar_cadastro():
  nome = input("Digite o nome do cadastro que deseja alterar: ")
  for cadastro in cadastros:
    if cadastro['Nome'] == nome:
        cadastro['Nome'] = input("Novo nome de cadastro: ")
        cadastro['Idade'] = input("Nova idade do cadastro: ")
        cadastro['Genero'] = input("Novo gênero do cadastro: ")
        cadastro['CPF'] = input("Novo CPF do cadastro: ")
        cadastro['Email'] = input("Novo email do cadastro:")
        cadastro['Telefone'] = input("Novo telefone de cadastro: ")
        return
    print("Cadastro não encontrado.")

#Função deletar um cadastro
def deletar_cadastro():
    nome = input("Digite o nome do cadastro que deseja deletar: ")
    for cadastro in cadastros:
        if cadastro['Nome'] == nome:
          cadastros.remove(cadastro)
          print("Cadastro delerado com sucesso!")
          return
          print("Cadastro não encontrado. ")

# Nome do arquivo CSV
nome_arquivo = 'cadastros.csv'

# Diretório atual do notebook
diretorio_atual =os.getcwd()

#Caminho completo para o arquivo CSV
caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)


#Função salvar, criar escritor e escrever cabeçalhos os dados em arquivo CSV
def salvar_dados():
    nome_arquivo = input("Digite o nome do arquivo: ")
    nome_arquivo += 'cadastro.csv'
    with open(nome_arquivo, 'w', newline='') as csvfile:
      cabecalhos = ['Nome','Idade','Gênero','CPF','Email','Telefone']
      escritor_csv = csv.DictWriter(arquivo_csv,fieldnames=cabecalhos)
      escritor_csv.writerheader()
      for cadastro in cadastros.csv: 
          escritor_csv.writerow(linha)

    print(f'Arquivo CSV"{cadastros.csv}" criado com sucesso em: {caminho_arquivo}')

#Loop principal
while True:
    exibir_menu
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        criar_cadastro()
    elif opcao == '2':
        listar_cadastros()
    elif opcao == '3':
        alterar_cadastro()
    elif opcao == '4':
        deletar_cadastro()
    elif opcao == '5':
      print("Sair")
      break
    else:
      print("Opção inválida. Tente novamente.")






