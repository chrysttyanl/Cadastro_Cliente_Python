from json import dump, load
from os import stat

def caminho_arquivo(func):
    def retornando_caminho(nome = None):
        return func('C:\\Projetos\\projeto_python\\Cadastro\\cliente.json',nome)
    return retornando_caminho

def cadastrar_cliente(func):
    def cadastrando_cliente():   
        condicao = True
        while condicao:
            try:
                print('*'*10 + 'Cadastro de Cliente' + '*'*10)
                nome = input('Nome: ')
                sobrenome = input('Sobrenome: ')
                idade = int(input('Idade: '))
                altura = float(input('Altura: '))
                rua = input('Rua: ')
                numero = int(input('Número: '))
                setor = input('Setor: ')
                cliente = {
                        'nome' : nome,
                        'sobrenome' : sobrenome,
                        'idade' : idade,
                        'altura' : altura,
                        'endereco' : {
                            'rua' : rua,
                            'numero' : numero,
                            'setor' : setor
                        }
                    }  
                # clientes.append(cliente) 
                escolha = input('Deseja continuar(S/N)? ').lower()            
                if escolha != 's':
                    break
            except ValueError as e:
                print('Por favor digite um valor válido!')
            except Exception as e:
                print(f'Erro: {type(e).__name__}')
        return func(cliente)
    return cadastrando_cliente

@cadastrar_cliente
@caminho_arquivo
def salvar_cadastro(caminho,dados):
    if stat(caminho).st_size != 0:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            clientes = load(arquivo)
            clientes.append(dados)
        print(clientes)
        
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            dump(
                clientes,
                arquivo,
                indent=2
            )
    else:         
        with open(caminho, 'w', encoding='utf-8') as arquivo:  
            clientes = [dados]
            dump(
                clientes,
                arquivo,
                indent=2,
            )

@caminho_arquivo
def listar_clientes(caminho_arquivo, dados):
    try:
        if stat(caminho_arquivo).st_size == 0:
            raise FileNotFoundError
        if dados == None:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                clientes = load(arquivo)
                for cliente in clientes:
                    print(
                        f'Nome: {cliente['nome']}\n' +
                        f'Sobrenome: {cliente['sobrenome']}\n' +
                        f'Idade: {cliente['idade']}\n' +
                        f'Altura: {cliente['altura']}\n' +
                        f'Rua: {cliente['endereco']['rua']}\n' +
                        f'Numero: {cliente['endereco']['numero']}\n' +
                        f'Setor: {cliente['endereco']['setor']}\n'
                        )
                    print('#' * 20)
        else:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                clientes = load(arquivo)  
                cliente = next((cliente for cliente in clientes if cliente['nome'].lower() == dados.lower()), None)
                print(
                    f'Nome: {cliente['nome']}\n' +
                    f'Sobrenome: {cliente['sobrenome']}\n' +
                    f'Idade: {cliente['idade']}\n' +
                    f'Altura: {cliente['altura']}\n' +
                    f'Rua: {cliente['endereco']['rua']}\n' +
                    f'Numero: {cliente['endereco']['numero']}\n' +
                    f'Setor: {cliente['endereco']['setor']}\n'
                    )   
    except FileNotFoundError as e:
        print('Error: Arquivo não encontrado ou vazio!')

    except TypeError as e:
        print('Error: Cliente não encontrado!')
    except Exception as e:
        print(f'Erro: {type(e).__name__}') 

@caminho_arquivo              
def apagar_cliente(caminho_arquivo, dados):
    try:
        cliente_apagar = None
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                clientes = load(arquivo)
                for i,dicionario in enumerate(clientes):
                    if dicionario['nome'] == dados:
                        cliente_apagar = i
        if cliente_apagar is not None:
            clientes.pop(cliente_apagar)
        else:
            raise TypeError                 

        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            dump(
                clientes,
                arquivo,
                indent=2,
            )
    except TypeError as e:
        print('Cliente não encontrado!')
    except Exception as e:
        print(f'Error: {type(e).__name__}')

def atualizar_cliente(indice, valor_alterar, valor_alterado):
    try:
        caminho_arquivo = 'C:\\Projetos\\projeto_python\\Cadastro\\cliente.json'
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                clientes = load(arquivo)
                for i,cliente in enumerate(clientes):
                    if cliente[indice] == valor_alterar:
                        cliente[indice] = valor_alterado
                    else:
                        raise TypeError
            

        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            dump(
                clientes,
                arquivo,
                indent=2,
            )
    except FileNotFoundError as e:
        print('Error: Arquivo não encontrado ou vazio!')
    except TypeError as e:
        print('Error: Cliente não encontrado!')
    except Exception as e:
        print(f'Erro: {type(e).__name__}') 

def app():
    try:
        continuar = True
        while continuar:
            print('#'*11 + '_Cadastro de cliente_' + '#'*11)
            print('# 1 - Cadastrar cliente')
            print('# 2 - Atualizar cliente')
            print('# 3 - Pesquisar cliente(s)')
            print('# 4 - Apagar cliente')
            print('# 5 - Sair')
            escolha = int(input('# Escolha uma das opções: '))
            print('#'*43)
            if escolha == 1:
                salvar_cadastro()               
            elif escolha == 2:
                pesquisa = input('Digite o nome: ')
                novo_nome = input('Digite o novo nome: ')
                atualizar_cliente('nome', pesquisa, novo_nome)
            elif escolha == 3:
                pesquisa = input('Digite o nome ou deixa em branco: ')
                if pesquisa == '':
                    listar_clientes()
                else:
                    listar_clientes(pesquisa)
            elif escolha == 4:
                pesquisa = input('Digite o nome: ')
                apagar_cliente(pesquisa)
            elif escolha == 5:
                continuar = False
            else:
                raise ValueError
    except ValueError as e:
                print('Por favor digite um valor válido!')
    except Exception as e:
        print(f'Error: {type(e).__name__}')
########################################################################################
# app()