chamados = []

def listar_chamados(lista_chamados):
    if len(lista_chamados) == 0:
        print('Não existem chamados em aberto agora.')
        return # O return finaliza a função aqui e impede que o loop for rode à toa
        
    for i, chamado in enumerate(lista_chamados):
        # Quebrei o print em 3 linhas para o código não ficar gigante na horizontal (boa prática)
        print(f"{i + 1} - Problema: {chamado['problema']}")
        print(f"    Descrição: {chamado['descricao']}")
        print(f"    Técnico: {chamado['tecnico']}")

def abrir_chamado(lista_chamados):
    while True:
        problema = input('Qual o problema apresentado? ').strip()
        if problema == '':
            print('O problema não pode ser vazio. Tente novamente.')
        else:
            break
            
    while True:
        descricao = input('Qual o tipo de aparelho? ').strip()
        if descricao == '':
            print('A descrição não pode ser vazia. Tente novamente.')
        else:
            break
            
    novo_chamado = {
        'problema': problema,
        'descricao': descricao,
        'tecnico': 'Nenhum'
    }
    
    lista_chamados.append(novo_chamado)
    print('Seu chamado foi aberto com sucesso!')

def encaminhar_chamado(lista_chamados):
    # Early Return: Trava de segurança inicial
    if len(lista_chamados) == 0:
         print('Sem chamados para encaminhar.')
         return 

    listar_chamados(lista_chamados)
    
    while True:
        try:
            indice_chamado = int(input('Qual o índice do chamado? '))
            if indice_chamado <= 0 or indice_chamado > len(lista_chamados):
                print('Não existe esse chamado. Tente novamente.')
            else:
                break
        except ValueError:
            print('Inválido! Tem que ser um número.')
            
    while True:
        tecnico = input('Qual o nome do técnico? ').strip()
        if tecnico == '':
            print('O nome do técnico não pode ser vazio.')
        elif not tecnico.replace(' ','').isalpha():
            print('O nome não pode conter números ou símbolos!')
        else:
            break
            
    indice_real = indice_chamado - 1
    lista_chamados[indice_real]['tecnico'] = tecnico
    print(f"Chamado {indice_chamado} encaminhado para {tecnico} com sucesso!")

def finalizar_chamado(lista_chamados):
    if len(lista_chamados) == 0:
        print('Sem chamados para finalizar.')
        return

    listar_chamados(lista_chamados)
    
    while True:
        try:
            chamado_para_fechar = int(input('Qual o número do chamado que você quer fechar? '))
            if chamado_para_fechar <= 0 or chamado_para_fechar > len(lista_chamados):
                print('Não existe esse chamado!')
            else:
                break
        except ValueError:
            print('Opção inválida! Digite apenas números.')
            
    indice_fechar = chamado_para_fechar - 1
    lista_chamados.pop(indice_fechar)
    print(f'O chamado {chamado_para_fechar} foi fechado com sucesso.')

def menu():
    while True:
        print('\n' + '-' * 20) # O \n dá um respiro visual antes do menu aparecer de novo
        print('1 - Novo Chamado')
        print('2 - Listar Chamados')
        print('3 - Encaminhar Chamados')
        print('4 - Deletar Chamado')
        print('5 - Sair')
        print('-' * 20)
        
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                abrir_chamado(chamados)
            elif opcao == 2:
                listar_chamados(chamados)
            elif opcao == 3:
                encaminhar_chamado(chamados)
            elif opcao == 4:
                finalizar_chamado(chamados)
            elif opcao == 5:
                print('Fechando o programa...')
                break
            else:
                print('Tem que ser um número de 1 a 5!')
        except ValueError:
            print('Opção inválida! Apenas números.')

menu()