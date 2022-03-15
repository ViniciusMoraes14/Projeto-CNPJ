import Dados as cnpj

while True:
    res = input("Deseja validar um CNPJ? - Digite 1\nDeseja gerar CNPJ? - Digite 2\n... ").lower()
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
        
            
