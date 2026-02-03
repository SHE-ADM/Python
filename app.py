import os
from tracemalloc import start

restaurantes = [{'nome': 'Praça1', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Praça2', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Praça3', 'categoria': 'Brasileira', 'ativo': True}]

def exibir_nome():
   print("""
                  
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')
    
def exibir_subtitulos(texto):
   os.system('cls')
   print(texto)   
   print()
       
def voltar_menu_principal():
    input('Digite Enter para voltar ao menu principal... ')
    main()

def opcao_invalida():
    exibir_subtitulos('Opção inválida! Tente novamente.')
    voltar_menu_principal()
   
def cadadastrar_restaurante(): 
   exibir_subtitulos('Cadastro de novos restaurantes')
   nome_restaurante = input('Digite o nome do restaurante: ')
   dados_do_restaurante = {'nome': nome_restaurante, 'categoria': '', 'ativo': False}
   restaurantes.append(dados_do_restaurante) 
   restaurantes.append({'nome': nome_restaurante, 'categoria': '', 'ativo': False})
   print(f'\nRestaurante "{nome_restaurante}" cadastrado com sucesso!\n')
   voltar_menu_principal()
      
def listar_restaurante():
   exibir_subtitulos('Listagem de Restaurantes')

   for restaurante in restaurantes:
      nome_restaurante = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = restaurante['ativo']
      print(f' - {nome_restaurante} | Categoria: {categoria} | Ativo: {ativo}')
    
   voltar_menu_principal()
  
def fim_app():
    exibir_subtitulos('Obrigado por usar o sistema de restaurantes!')        
 
def escolher_opcao_usando_if():  
   try:
      opcao_escolhida = input('Escolha uma opção: ')
      opcao_escolhida = int(opcao_escolhida)    

      if opcao_escolhida == 1:
         cadadastrar_restaurante()

      elif opcao_escolhida == 2:
         listar_restaurante()
         
      elif opcao_escolhida == 3:
         print('Ativar Restaurante')

      elif opcao_escolhida == 4:
         fim_app()

      else:
         opcao_invalida()
   except ValueError:
      opcao_invalida()  
         
def main():
    exibir_nome() 
    exibir_opcoes()
    escolher_opcao_usando_if()        

if __name__ == '__main__':
   os.system('cls')  
   main()
    
    