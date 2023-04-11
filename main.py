"""
Faça um algoritmo que utilize o menu abaixo:

MENU
======
1- Ler arquivo de jogadores
2- Escalar time
3- Realizar Substiuição
4- Expulsão
5- Imprimir escalação
Escolha: 


Opção 1: Ler de um arquivo texto todos os jogadores
        escalados para a copa e armazenar em uma
        lista (lst_jogadores)
        Cada Elemento da lista será uma instância
            da classe Jogador.

Opção 2: Você deverá escalar 11 dos jogadores para
        iniciar a partida.
        Os Jogadores escalados para a partida ficam
            em uma lista (lst_escalados)
            Alterar o atributo 'participou_partida'
                para True
        Os jogadores que não forem escalados para
            iniciar a partida ficam em uma outra
            lista (lst_reserva)
Opção 3: Você poderá realizar a substituição de um
        jogador por outro.
        Quando isso acontecer o jogador vai para
            a lista de Reserva e o outro para a
            lista Escalados.

Opção 4: Caso haja alguma expulsão, o jogador sai
        da lista de Escalados e vai para a lista
        Reserva.

Opção 5: Mostrar a escalação de todos jogadores que
        participaram do jogo, inclusive as substituições
        e expulsões. 
        Salve esses dados em um arquivo (todosjogadores.txt)


class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False # ou Truelst_jogadores = []"""


lst_escalados = []
lst_reserva = []


class Jogador:
    def __init__(self, nome, numero, posicao):
        self.__numero = numero
        self.__nome_jogador = nome
        self.__posicao = posicao  # GOLEIRO ou DEFESA ou MEIO-CAMPO ou ATECANTE
        self.__situacao = "NORMAL"  # ou "EXPULSO"
        self.__participou_partida = False  # ou True

    def get_numero(self):
        return self.__numero

    def get_nome_jogador(self):
        return self.__nome_jogador

    def get_posicao(self):
        return self.__posicao

    def get_situacao(self):
        return self.__situacao

    def get_participou_partida(self):
        return self.__participou_partida

    def set_participou_partida(self, sim):
        self.__participou_partida = sim

    def set_situacao(self, legal):
        self.__situacao = legal

    def __str__(self):
        return f"{self.__numero}-{self.__nome_jogador} -Posição:{self.__posicao}"


'''---------------------------------------------------------------------------------------'''
'''--------------------------------------OPÇÃO1-------------------------------------------'''
'''---------------------------------------------------------------------------------------'''


def abrir_arquivo():
    arquivo = open("convocados.txt", "r", encoding="utf-8")
    for i in arquivo:
        if i == '26:Gabriel Martinelli:ATACANTE':
            numero, nome, posicao = i[:].split(':')
            jogador = (Jogador(nome, numero, posicao))
            lst_jogadores.append(jogador)
        else:
            numero, nome, posicao = i[:].split(':')
            posicao = posicao[:-1]
            jogador = (Jogador(nome, numero, posicao))
            lst_jogadores.append(jogador)
    for i in (lst_jogadores):
        print(i)

    arquivo.close()


def lerArquivo():
    arquivo = open("convocados.txt", "r", encoding="utf-8")
    for i in arquivo:
        if i == '26:Gabriel Martinelli:ATACANTE':
            numero, nome, posicao = i[:].split(':')
            jogador = (Jogador(nome, numero, posicao))
            lst_jogadores.append(jogador)
        else:
            numero, nome, posicao = i[:].split(':')
            posicao = posicao[:-1]
            jogador = (Jogador(nome, numero, posicao))
            lst_jogadores.append(jogador)


'''---------------------------------------------------------------------------------------'''
'''--------------------------------------OPÇÃO2-------------------------------------------'''
'''---------------------------------------------------------------------------------------'''


def escalar():
    lerArquivo()

    duplicado = False
    print("-----------------------------------------------------------")
    print("A ESCALAÇÃO FUNCIONA PELO NÚMERO DO JOGADOR")
    print("-----------------------------------------------------------")
    while len(lst_escalados) <= 10:

        jogador = input("Escolha os Jogadores Titulares pelos Numeros: ")
        for i, titulares in enumerate(lst_jogadores):
            if titulares.get_numero() == jogador:
                for linha in lst_escalados:
                    duplicado = False
                    if linha.get_numero() == jogador:
                        duplicado = True
                        print("Jogador já escalado")
                        break
                if not duplicado:
                    titulares.set_participou_partida(True)
                    lst_escalados.append(titulares)
                    lst_jogadores[i] = titulares
                    break
    print("-------------------------------------------------------------------------------------------------------")
    print("TODOS JOGADORES ESCALADOS COM SUCESSO")
    print("APITA O ÁRBITRO, VAI COMEÇAR A PARTIDA!!")


def reserva():
    for i in lst_jogadores:
        dentro = False
        for j in lst_escalados:
            if i.get_numero() == j.get_numero():
                dentro = True
                break
        if not dentro:
            lst_reserva.append(i)


'''---------------------------------------------------------------------------------------'''
'''--------------------------------------OPÇÃO3-------------------------------------------'''
'''---------------------------------------------------------------------------------------'''


def substituicao():
    for l in lst_escalados:
        print("Numero: ", l.get_numero(), " Nome: ", l.get_nome_jogador(), " Posição: ", l.get_posicao(), )
    entrou = False
    print("\n")
    print("-----SUBSTITUIÇÃO-----")
    sai = input("\n QUAL O NUMERO DO JOGADOR QUE ESTÁ SAINDO?")
    for j in lst_jogadores:
        try:
            if j.get_numero() == sai:
                lst_escalados.remove(j)
                lst_reserva.append(j)
                break
        except:
            print("Jogador já escalado")

            return menu()

    print("------------------------------")
    for l in lst_reserva:
        print("Numero: ", l.get_numero(), " Nome: ", l.get_nome_jogador(), " Posição: ", l.get_posicao(), )
    entra = input("\n QUAL O NUMERO DO JOGADOR QUE ESTÁ ENTRANDO? ")
    for ind, jogadores in enumerate(lst_jogadores):
        if jogadores.get_numero() == entra:
            lst_reserva.remove(jogadores)
            lst_escalados.append(jogadores)
            jogadores.set_participou_partida(True)
            lst_jogadores[ind] = jogadores
            entrou = True

    if entrou:
        print("Substituição realizada com sucesso!!!")


'''---------------------------------------------------------------------------------------'''
'''--------------------------------------OPÇÃO4-------------------------------------------'''
'''---------------------------------------------------------------------------------------'''


def expulsao():
    for l in lst_escalados:
        print("Numero: ", l.get_numero(), " Nome: ", l.get_nome_jogador(), " Posição: ", l.get_posicao(), )
    sai = input("\n QUAL O NUMERO DO JOGADOR EXPULSO? ")
    for i, jogadores in enumerate(lst_jogadores):
        if jogadores.get_numero() == sai:
            for escalado in lst_escalados:
                if escalado.get_numero() == sai:
                    lst_escalados.remove(jogadores)
                    lst_reserva.append(jogadores)
                    jogadores.set_situacao("EXPULSO")
                    lst_jogadores[i] = jogadores
                    break


'''---------------------------------------------------------------------------------------'''
'''--------------------------------------OPÇÃO5-------------------------------------------'''
'''---------------------------------------------------------------------------------------'''


def imprimir():
    print("\n Escalação: ")
    for l in lst_jogadores:
        if l.get_participou_partida():
            grava_arquivo(l.get_numero(), l.get_nome_jogador(), l.get_posicao(), l.get_situacao())
            print("Numero:", l.get_numero(), " Nome:", l.get_nome_jogador(), " Posição:", l.get_posicao(), "Situação: ",
                  l.get_situacao())


def grava_arquivo(numero, nome, posicao, situacao):
    try:
        arquivo = open("todosjogadores.txt", "a",encoding="utf-8")
    except:
        arquivo = open("todosjogadores.txt", "w",encoding="utf-8")

    arquivo.write(str(numero) + ":" + nome + ":" + posicao + ":" + situacao + "\n")
    arquivo.close()





def menu():
    while True:
        escolha = input(
            """
        =======================================
        MENU
        =======================================  
            1- Ler arquivo de jogadores
            2- Escalar time
            3- Realizar Substiuição
            4- Expulsão
            5- Imprimir escalação
        Escolha: """
        )

        if escolha == '1':
            abrir_arquivo()
        if escolha == '2':
            escalar()
            reserva()
        if escolha == '3': substituicao()
        if escolha == '4': expulsao()
        if escolha == '5': imprimir()


menu()
