'''
Jogo que jogadores propõem inicialmente um número de peças 
serão dispostos em um tabuleiro e um limite de peças 
que podem ser tiradas do tabuleiro por cada jogador. 
Vencerá quem retirar a ultima peça do tabuleiro.
O jogo tem os modos usuário versus computador ou usuário versus usuário.
'''
import random

__author__ = "Leonardo FSS"
__copyright__ = "Copyright 2018, by FSS"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "Leonardo FSS"
__email__ = "leonnferreira@gmail.com"
__status__ = "Prototype"

def computador_escolhe_jogada(n, m):
		'''
		Função que determina como o computador joga, usando estratégia
		vencedora.
		'''
		restante= n - (m+1)
		multiplo = n // (m+1)
		resto = n % (m+1)
		if resto < m + 1 and multiplo >= 1 and multiplo < 3:
			jogada = resto
			print("\nComputador retirou",jogada,"peças.")
			return int(jogada)
		elif n <= m:
			jogada = n
			print("\nComputador retirou",jogada,"peças.")
			return int(jogada)
		elif restante > m:
			jogada = m
			print("\nComputador retirou",jogada,"peças.")
			return int(jogada)


def usuario_escolhe_jogada(n, m):
	'''
	Função que recolhe a jogada do usuário.
	Não permite movimentos ilegais como retirar 0 peças,
	ou mais peças do que existem no tabuleiro 
	ou permitidas por rodada ou colocar peças no tabuleiro.
	'''
	jogada = 0
	while jogada <= 0 or jogada > m:
		jogada = int(input("Digite quantas peças você quer tirar do tabuleiro: "))
		if jogada <= m and jogada > 0 and (n - jogada) >= 0 :
			return int(jogada)
		print("Você deve retirar entre uma peça e",m,"peça(s) do tabuleiro para ser uma jogada válida.")
		print("Se houver menos peças no tabuleiro que o limite máximo por rodada, então o número de peças no tabuleiro (",n,") passará a ser o limite máximo")
		jogada = 0


def usuarios(n, m, nome):
	'''
	Função que permite identificar usuários e 
	quando eles farão suas jogadas.
	'''
	print("\n\n"+nome+", faça sua jogada.")
	return usuario_escolhe_jogada(n, m)
	

def partida():
	'''
	Função que determina quem iniciará a partida,
	quais serão os parãmetros da partida e como a partida será jogada
	entre um usuário e o computador.
	'''
	n = int(input("\nQuantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	while m > n or n == 0 or m == 0:
		print("O limite de peças por jogada tem que ser menor que número de peças do tabuleiro \n e nenhuma das duas quantidades pode ser zero.")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
	 
	pRetiradas = 0

	if n % (m+1) == 0:
		print("\nVocê começa!\n")
		while n != 0:
			print("\nPeças no tabuleiro:",n,"\nRetirada limite:",m)
			print("Peças retiradas na ultima jogada:", pRetiradas)
			pRetiradas =  usuario_escolhe_jogada(n, m)
			n = n - pRetiradas
			if n == 0:
				print("\n###### Você venceu!######")
				return False
			print("\nPeças no tabuleiro:",n,"\nRetirada limite:",m)
			print("Peças retiradas na ultima jogada:", pRetiradas)
			pRetiradas = computador_escolhe_jogada(n, m)
			n = n - pRetiradas            
			if n == 0:
					print("\n###### Computador venceu!######\n")
					return True
	else:
		print("\nComputador começa!\n")
		while n != 0:
			print("\nPeças no tabuleiro:",n,"\nRetirada limite:",m)
			print("Peças retiradas na ultima jogada:", pRetiradas)
			pRetiradas = computador_escolhe_jogada(n, m)
			n = n - pRetiradas
			if n == 0:
				print("\n###### Computador venceu!######\n")
				return True
			print("\nPeças no tabuleiro:",n,"\nRetirada limite:",m)
			print("Peças retiradas na ultima jogada:", pRetiradas)
			pRetiradas =  usuario_escolhe_jogada(n, m)
			n = n - pRetiradas
			if n == 0:
				print("\n###### Você venceu!######\n")
				return False


def nome_usuario():
	'''
	Função para guardar o nome de cada usuário 
	na partida ente dois usuários.
	'''
	nome = input("Digite nome do jogador: ")
	nome = nome.upper()
	return nome

			
def partida_usuarios(user1, user2):
	'''
	Função que determina quem iniciará a partida,
	quais serão os parãmetros da partida e como a partida será jogada
	entre dois usuários.
	'''
	n = int(input("\nQuantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	while m > n or n == 0 or m == 0:
		print("O limite de peças por jogada tem que ser menor que número de peças do tabuleiro")
		print("e nenhuma das duas quantidades pode ser zero.")
		n = int(input("Quantas peças? "))
		m = int(input("Limite de peças por jogada? "))
		
	quem_começa = random.choice([1,2])
	pRetiradas = 0
	 
	if quem_começa == 1:
		print("\n"+user1+" começa!\n")
		while n != 0:
			print("\nPeças no tabuleiro:",n,"\nRetirada limite:",m)
			print("Peças retiradas na ultima jogada:", pRetiradas)
			pRetiradas =  usuarios(n, m, user1)
			n = n - pRetiradas
			if n == 0:
				print("\n###### "+user1+" venceu!######")
				return False
			print("\nPeças no tabuleiro:",n,"\nRetirada limite:",m)
			print("Peças retiradas na ultima jogada:", pRetiradas)
			pRetiradas = usuarios(n, m, user2)
			n = n - pRetiradas            
			if n == 0:
					print("\n###### "+user2+" venceu!######\n")
					return True
	else:
		print("\n"+user2+" começa!\n")
		while n != 0:
			print("\nPeças no tabuleiro:",n,"\nRetirada limite:",m)
			print("Peças retiradas na ultima jogada:", pRetiradas)
			pRetiradas = usuarios(n, m, user2)
			n = n - pRetiradas
			if n == 0:
				print("\n###### "+user2+" venceu!######\n")
				return True
			print("\nPeças no tabuleiro:",n,"\nRetirada limite:",m)
			print("Peças retiradas na ultima jogada:", pRetiradas)
			pRetiradas =  usuarios(n, m, user1)
			n = n - pRetiradas
			if n == 0:
				print("\n###### "+user1+" venceu!######\n")
				return False


def campeonato():
	'''
	Função que determina três rodadas entre usuário
	e computador. Conta e demonstra ao final as vitórias
	do usuário e computador.
	'''
	print("*******1a Rodada*******")
	v_comp = v_usuario = 0
	vitoria = partida()
	if vitoria:
		v_comp = v_comp + 1
	else:
		v_usuario = v_usuario +1
	print("*******2a Rodada*******")
	vitoria = partida()
	if vitoria:
		v_comp = v_comp + 1
	else:
		v_usuario = v_usuario +1
	print("*******3a Rodada*******")
	vitoria = partida()
	if vitoria:
		v_comp = v_comp + 1
	else:
		v_usuario = v_usuario +1
	print("Placar: Você",v_usuario, "X",  v_comp, "Computador")


def campeonato_usuarios(user1, user2):
	'''
	Função que determina três rodadas entre usuários. Conta e demonstra ao final as vitórias
	de cada usuário.
	'''	
	print("*******1a Rodada*******")
	v_user1 = v_user2 = 0
	vitoria = partida_usuarios(user1, user2)
	if vitoria:
		v_user2 = v_user2 + 1
	else:
		v_user1 = v_user1 +1
	print("Placar: "+user1+" ",v_user1, "X",  v_user2, user2+"\n\n")
	
	print("*******2a Rodada*******")
	vitoria = partida_usuarios(user1, user2)
	if vitoria:
		v_user2 = v_user2 + 1
	else:
		v_user1 = v_user1 +1
	print("Placar: "+user1+" ",v_user1, "X",  v_user2, user2+"\n\n")
	
	print("*******3a Rodada*******")
	vitoria = partida_usuarios(user1, user2)
	if vitoria:
		v_user2 = v_user2 + 1
	else:
		v_user1 = v_user1 +1
	print("##########################################################")
	print("Placar: "+user1+" ",v_user1, "X",  v_user2, user2+"\n")
	print("##########################################################")


def inicio():
	escolha = 0
	while escolha != 1 or escolha !=2 or escolha !=3:
			print("\n\n-------------------------------------------------\n")
			print("	Seja bem vindo ao jogo do Nim!")
			print("\n-------------------------------------------------\n\n")
			print("Escolha:")
			print("1- para jogar uma partida contra o computador.")
			print("2- para jogar um campeonato contra o computador.")
			print("3- para jogar uma partida contra outro usuário.")
			print("4- para jogar um campeonato contra outro usuário.")
			print("5- para sair do programa.\n\n")
			escolha = int(input("Sua escolha foi: "))
			if escolha == 1:
					partida()
			elif escolha == 2:
					campeonato()
			elif escolha == 3:
					user1 = nome_usuario()
					user2 = nome_usuario() 
					partida_usuarios(user1, user2)
			elif escolha == 4:
					user1 = nome_usuario()
					user2 = nome_usuario() 
					campeonato_usuarios(user1, user2)
			elif escolha == 5:
					quit()
			else:
					print("Você deve escolher entre as opções 1, 2, 3, 4 ou 5 apenas.")


inicio()