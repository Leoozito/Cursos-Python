import os
import time 

all_restaurants = []

def apresentation_of_program():
    print("""
    SEJA BEM VINDO AO -

    █▀▀ █░█ █░░ █░░   ▀█▀ █░█ █▀▄▀█ █▀▄▀█ █▄█
    █▀░ █▄█ █▄▄ █▄▄   ░█░ █▄█ █░▀░█ █░▀░█ ░█░   
               
""")
    
def apresentation_of_options():
    print("""
    ---------------------------------------------
    Opções:

    [ 1 ] - Cadastrar restaurante
    [ 2 ] - Listar restaurantes
    [ 3 ] - Ativar restaurante
    [ 4 ] - Sair do Programa 
    ---------------------------------------------    
""")
    
def choose_option():
    try:
        chosen_option = int(input("Digite o n° da opção desejada: "))
        
        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurant()
        elif chosen_option == 3:
            activate_restaurant()
        elif chosen_option == 4:
            exit_program()
        else:
            os.system("clear") 
            print("Opção invalida !  ✘")
            time.sleep(3)
            apresentation_of_options()
    except:
        os.system("clear")
        print("Digite apenas números !")
        time.sleep(3)
        os.system('clear')
        main()

def register_restaurant():
    os.system('clear')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Cadastro de restaurante\n")
    name_restaurant = input("Digite o nome do restaurante: ")
    all_restaurants.append(name_restaurant)
    os.system('clear')
    print(f"Restaurante {name_restaurant} cadastrado com sucesso !!\n\n")
    input("Clique qualquer tecla para voltar ao menu principal !")
    main()

def list_restaurant():
    os.system('clear')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Restaurantes cadastrados\n")
    for restaurants in all_restaurants:
        print(restaurants)

def activate_restaurant(): 
    print("Ativar restaurante")

def exit_program():
    os.system('clear')
    # os.system('cls') para macIOS
    print("Saindo do programa...")
    time.sleep(3)
    os.system('clear')
    print("Até breve! 😆")

def main():
    apresentation_of_program()
    apresentation_of_options()
    choose_option()

if __name__ == '__main__':
    main()