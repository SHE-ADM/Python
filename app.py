import os

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
    
def fim_app():
    os.system('cls')      
    print('\nObrigado por usar o sistema de restaurantes!\n')     

def escolher_opcao_usando_if():   
   opcao_escolhida = input('Escolha uma opção: ')
   opcao_escolhida = int(opcao_escolhida)    

   if opcao_escolhida == 1:
      print('Cadastrar Restaurante')

   elif opcao_escolhida == 2:
      print('Listar Restaurantes')
      
   elif opcao_escolhida == 3:
      print('Ativar Restaurante')

   else:
         fim_app()
         
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
    escolher_opcao_usando_match()
        
if __name__ == '__main__':
    main()
    
    