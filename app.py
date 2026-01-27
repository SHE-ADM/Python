import os
from tracemalloc import start

restaurantes = []


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
    input('Digite Enter para voltar ao menu principal...')
    main()

def opcao_invalida():
    exibir_subtitulos('\nOpção inválida! Tente novamente.\n')
    voltar_menu_principal()


def fim_app():
    exibir_subtitulos('\nObrigado por usar o sistema de restaurantes!\n')        
   
def cadadastrar_restaurante(): 
   exibir_subtitulos('Cadastro de novos restaurantes')
   nome_restaurante = input('Digite o nome do restaurante: ')
   restaurantes.append(nome_restaurante)
   print(f'\nRestaurante "{nome_restaurante}" cadastrado com sucesso!\n')
   voltar_menu_principal()
   
   
def listar_restaurante():
   exibir_subtitulos('Listagem de Restaurantes')

   for restaurante in restaurantes:
      print(f'{restaurante}')
      print()  
      voltar_menu_principal()
   
   
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
         

def escolher_opcao_usando_match():   
   opcao_escolhida = input('Escolha uma opção: ')
   opcao_escolhida = int(opcao_escolhida)    

   match opcao_escolhida:
      case 1:
         print('Cadastrar Restaurante')

      case 2:
         print('Listar Restaurantes')
         
      case 3:
         print('Ativar Restaurante')

      case _:
         fim_app()      
        

def main():
    exibir_nome() 
    exibir_opcoes()
    escolher_opcao_usando_if()
           

if __name__ == '__main__':
   os.system('cls')  
   main()
    
    