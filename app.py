#testando comentario
import os
from tracemalloc import start

restaurantes = [{'nome': 'Praça1', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Praça2', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Praça3', 'categoria': 'Brasileira', 'ativo': True}]

def exibir_nome():
   '''Método para exibir o nome do sistema'''
   
   print("""
                  
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)

def exibir_opcoes():
    '''Método para exibir as opções do sistema'''
    
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')
    
def exibir_subtitulos(texto):
   '''Método para exibir subtítulos '''
   
   os.system('cls')
   linha = '*' * (len(texto) + 4)
   print(linha)
   print(f'* {texto} *')
   print(linha)
       
def voltar_menu_principal():
    '''Método para voltar ao menu principal'''
    
    input('Digite Enter para voltar ao menu principal... ')
    main()

def opcao_invalida():
    '''Método para exibir mensagem de opção inválida'''
    
    exibir_subtitulos('Opção inválida! Tente novamente.')
    voltar_menu_principal()
   
def cadadastrar_restaurante(): 
   '''Método para cadastrar um novo restaurante'''
   
   exibir_subtitulos('Cadastro de novos restaurantes')
   nome_restaurante = input('Digite o nome do restaurante: ')
   categoria = input('Digite a categoria do restaurante: ')
   dados_do_restaurante = {'nome': nome_restaurante, 'categoria':categoria, 'ativo': False}
   restaurantes.append(dados_do_restaurante) 
   print(f'\nRestaurante "{nome_restaurante}" cadastrado com sucesso!\n')
   voltar_menu_principal()
      
def listar_restaurante():
   '''Método para listar os restaurantes'''
   
   exibir_subtitulos('Listagem de Restaurantes')

   print(f'{"Nome do Restaurante".ljust(23)} | {"Categoria".ljust(31)} | {"Status"}')
   
   for restaurante in restaurantes:
      nome_restaurante = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = 'ativado' if restaurante['ativo'] else 'desativado'
      print(f' - {nome_restaurante.ljust(20)} | Categoria: {categoria.ljust(20)} | Ativo: {ativo}')
    
   voltar_menu_principal()
  
def fim_app():
    '''Método para finalizar o aplicativo'''
    exibir_subtitulos('Obrigado por usar o sistema de restaurantes!')        
 
def alterar_status_restaurante():
   '''Método para alterar o status do restaurante'''
   
   exibir_subtitulos('Ativar Restaurante')
   nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ') 
   
   restaurante_encontrado = False
   for restaurante in restaurantes:
      if nome_restaurante == restaurante['nome']:
         restaurante_encontrado = True         
         restaurante['ativo'] = not restaurante['ativo']
         # fazendo uso de ternário
         mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
         print(mensagem)
   if not restaurante_encontrado:
      print(f'Não foi encontrado um restaurante com o nome "{nome_restaurante}".')
      

def escolher_opcao_usando_if(): 
   '''Método para escolher a opção usando estrutura condicional if'''
    
   try:
      opcao_escolhida = input('Escolha uma opção: ')
      opcao_escolhida = int(opcao_escolhida)    

      if opcao_escolhida == 1:
         cadadastrar_restaurante()

      elif opcao_escolhida == 2:
         listar_restaurante()
         
      elif opcao_escolhida == 3:
         alterar_status_restaurante()

      elif opcao_escolhida == 4:
         fim_app()

      else:
         opcao_invalida()
   except ValueError:
      opcao_invalida()  
         
def main():
    '''Função principal do aplicativo'''
    
    exibir_nome() 
    exibir_opcoes()
    escolher_opcao_usando_if()        

if __name__ == '__main__':
   '''Limpar a tela antes de iniciar o aplicativo'''
   
   os.system('cls')  
   main()
    
    