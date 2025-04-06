import os #Limpa o terminal
import random #Gera a aleatoriedade
import time #Possibilita a utilização do sleep (Espera)
from views import criar_conta
from models import Conta


# Limpar o terminal
os.system('cls' if os.name == 'nt' else 'clear')

#Lista de jogadores (Pré definida)
lista_jogadores = ["Ajala", "Ale", "Arthur", "Bernardin", "Bernardo", "Gouveia", "Guguin", "Gustavo", "Leonardo", "Lucas", "Malks", "Mikael", "Nicolas"]
jogadores_escolhidos = []   #Guarda os 10 jogadores escolhidos para em seguida realizar o sorteio


def adicionar_jogadores():#Adiciona novos jogadores à lista de jogadores
    while True:
        try:
            jogador = input("Nome ou Apelido do jogador: ").strip()
            if not jogador:
                raise ValueError("O campo deve ser preenchido!\n")
            criar_conta(Conta(nome_real = None, nick = jogador, hashtag = "BR1"))
            print(jogador + " foi adicionado\n")
            
            novo_jogador = input("Deseja adicionar outro jogador (S / N): ").upper()
            if novo_jogador == 'S':
                adicionar_jogadores()
            else:
                print("Jogadores Adicionados\n")
                break
            break
        except ValueError as erro:
            print(erro)



def excluir_jogadores():#Exclui jogadores da lista de jogadores (O nome de exclusão deve ser igual)
    while True:
        try:
            player = input("Nome ou Apelido do jogador: ").strip()
            if not player:
                raise ValueError("O campo deve ser preenchido!\n")
            if player in lista_jogadores:
                for jogador in lista_jogadores:
                    if jogador == player:
                        lista_jogadores.remove(jogador)
                        print(jogador + " foi removido\n")
                        
                        novo_jogador = input("Deseja excluir outro jogador (S / N): ").upper()
                        if novo_jogador == 'S':
                            excluir_jogadores()
                        else:
                            print("Jogadores Excluídos\n")
                        break
                break
            else:
                print("Jogador não existe!\n")
                excluir_jogadores()
                break
        except ValueError as erro:
            print(erro)



def visualizar_jogadores():#Visualiza a lista de jogadores cadastrados
    for jogador in lista_jogadores:
        print(jogador)
    print()



def escolher_jogadores():#Exibe a lista de jogadores cadastrados e solicita a escolha de 10 para montar as equipes
    print("Escolha de jogadores\n------------------------")
    visualizar_jogadores()
    print("Atenção: Devem ser escolhidos 10 jogadores por partida!\n\n")
    
    print("Jogadores para Partida\n------------------------")
    contador = 1

    while True:
        for contador in range(1,11):
            while True:
                jogador = input(f"{contador}. ").strip()
                
                if jogador in lista_jogadores:
                    if jogador not in jogadores_escolhidos:
                        jogadores_escolhidos.append(jogador)
                        break
                    else:
                        print(" Jogador já foi escolhido!")
                else:
                    print(" Jogador não existe! Tente novamente")    
        break
    
    print("\nResumo de jogadores\n----------------------------")
    
    contador = 1
    for jogador in jogadores_escolhidos:
            print(f"{contador}. {jogador}")
            contador += 1



def alterar_escolhas():#Altera jogadores na escolha, caso queira trocar algum jogador de última hora e em seguida executa o sorteio de equipes
    alterar_jogador = input("\nDeseja realizar alteração de jogadores? (S / N): ").upper()
    if alterar_jogador == 'S':
        while True:
            id_jogador = int(input("Numero do jogador: "))
            if id_jogador > 10 or id_jogador < 1:
                print("Número inválido. Tente novamente!\n")
            else:
                break
            
        while True:
            novo_jogador = input("Novo jogador: ")
            print()
            if novo_jogador in lista_jogadores:
                if novo_jogador not in jogadores_escolhidos:
                    jogadores_escolhidos[id_jogador - 1] = novo_jogador
                    contador = 1
                    for jogador in jogadores_escolhidos:
                        print(f"{contador}. {jogador}")
                        contador += 1
                        
                    nova_alteração = input("\nDeseja realizar outra alteração? (S / N): ").upper()
                    if nova_alteração == 'S':
                        alterar_escolhas()
                    else:
                        print("\n\nEscolhas feitas!")
                        print("Aguarde... Estamos balanceando as equipes!\n\n")
                        pause()
                        sortear_equipes(jogadores_escolhidos)
                        break
                    break
                else:
                    print("Jogador já escolhido")
            else:
                print("Jogador não existe. Tente novamente!")
    else:
        print("\n\nEscolhas feitas!")
        print("Aguarde... Estamos balanceando as equipes!\n\n")
        pause()
        sortear_equipes(jogadores_escolhidos)



def sortear_equipes(jogadores_escolhidos): #Sorteia os times baseado nos jogadores escolhidos (Sorteio aleatório e sem peso)
    jogadores_escolhidos = random.sample(jogadores_escolhidos,10)
    print("\n\n\tCRIAÇÃO DE EQUIPES")
    print("-" * (18 + 20))
    
    print("EQUIPE 1".ljust(15) + "|\tEQUIPE 2".ljust(15))
    print("-" * (18 + 20))
    
    for i in range(0, len(jogadores_escolhidos), 2):
        jogador1 = jogadores_escolhidos[i].ljust(15)
        jogador2 = jogadores_escolhidos[i + 1].ljust(15) if i + 1 < len(jogadores_escolhidos) else "".ljust(15)
        print(f"{jogador1}|\t{jogador2}")
        
    print("\n" * 10)



def pause():#Efeito de pausa tempo (simula tela de carregamento)
    time.sleep(3)
    input("Equipes criadas! Pressione ENTER para continuar...")


adicionar_jogadores()

#Para executar o código chame as funçoes
