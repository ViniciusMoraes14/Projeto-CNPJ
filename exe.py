from Dados import *
import cnpj

print("Olá,Bem-Vindo!\n Aqui Podemos validar e gerar CNPJ's e\n Criar Clientes em nosso banco de dados!")
print("-"*60)
while True:
    menu = input("Menu:\nCaso deseja validar ou gerar um cnpj - Digite 1\nCaso queira ir para aba de Cadastro de Clientes - Digite 2\nPara fechar o programa - Digite 3\n...")
    if menu == "1":
        while True:
            res = input("Deseja validar um CNPJ? - Digite 1\nDeseja gerar CNPJ? - Digite 2\nPara voltar ao Menu - Digite 3\n... ").lower()
            if res == "1":
                cnpj1 = input("Digite o CNPJ: ")
                if cnpj.valida(cnpj1):
                    print(f'{cnpj1} é válido')
                else:
                    print(f'{cnpj1} é inválido')
            if res == "2":
                print("-"*60)
                for i in range(100):
                    novo_cnpj = cnpj.gera()
                    formatado = cnpj.formata(novo_cnpj)
                    print(formatado)
                    print("-"*60)
            if res == "3":
                break
    if menu == "2":
        while True:
            op = int(input(''' Digite uma Opção:

                1 - Listar CNPJ\'s cadastrados
                2 - Importar dados do CNPJ
                3 - Voltar para o menu
                :'''))
            if op == 3:
                break
            executar(op)
    if menu == "3":
        print("Tchau!")
        exit()