import copy
#table de jeu

matrice = {   "1":"_", "2":"_", "3":"_"
			, "4":"_", "5":"_", "6":"_"
			, "7":"_", "8":"_", "9":"_"
			}

matrice_updated = {   "1":"1", "2":"2", "3":"3"
					, "4":"4", "5":"5", "6":"6"
					, "7":"7", "8":"8", "9":"9"
					}


position_x = {   "1_2_3" : 0, "4_5_6" : 0,"7_8_9" : 0
               , "1_4_7" : 0, "2_5_8" : 0,"3_6_9" : 0
               , "1_5_9" : 0, "3_5_7" : 0}

position_o = {   "1_2_3" : 0, "4_5_6" : 0,"7_8_9" : 0
               , "1_4_7" : 0, "2_5_8" : 0,"3_6_9" : 0
               , "1_5_9" : 0, "3_5_7" : 0}

best_solution = ["1","3","7","9"]

player_name = []
player_icon = []

# Menu du jeu

print("Bienvenue !")
while True:
	nb_player = input("Nombre de joueur : ")

	if nb_player in ("1","2"):
		break

if nb_player == "1" :
	#tes joueurs
	player1_name = input("Nom premier joueur : ")
	player2_name = "Jarvis"


if nb_player == "2" :
	#tes joueurs
	player1_name = input("Nom premier joueur : ")
	player2_name = input("Nom deuxième joueur : ")



while True:
	player1_icon = input("Choissisez entre les 'X' et les 'O' : ").capitalize()

	if player1_icon in ("X","O"):
		break

if player1_icon == "X":
	player2_icon = "O"

	player_name.append(str(player1_name))
	player_name.append(str(player2_name))

	player_icon.append(player1_icon.upper())
	player_icon.append(player2_icon.upper())
	
	player_pos = [position_x,position_o]

else:
	player2_icon = "X"

	player_name.append(str(player1_name))
	player_name.append(str(player2_name))

	player_icon.append(player1_icon.upper())
	player_icon.append(player2_icon.upper())

	player_pos = [position_o,position_x]


#maquette en cours de partie
def affichage(source):
	print("")
	print("Tic Tac Toe !")
	print(" _______")
	print("| {} {} {} |".format(source["1"],source["2"],source["3"]))
	print("| {} {} {} |".format(source["4"],source["5"],source["6"]))
	print("| {} {} {} |".format(source["7"],source["8"],source["9"]))
	print("|_______|")
	print("")


#faire la somme de position x et o
def warning_winner() :

	win_x = ""
	win_o = ""

	#somme des listes x et o
	position = copy.deepcopy(position_x)
	for x_cle, x_values in position.items():
		for o_cle, o_values in position_o.items():
			if x_cle == o_cle :
				position[x_cle] = x_values + o_values

	pos_x = copy.deepcopy(position_x)
	pos_o = copy.deepcopy(position_o)

	# si somme = 3 , plus de solution possible
	# alors ligne ou colonne = 9
	for cle , values in position.items() : 
		for x_cle , x_values in pos_x.items():
			if cle == x_cle and values == 3 :
				pos_x[cle] = 9

	for cle , values in position.items() : 
		for o_cle , o_values in pos_o.items():
			if cle == o_cle and values == 3 :
				pos_o[cle] = 9

	# pour X
	# il ne reste que les vraies solutions = 2
	for pos_cle, pos_values in pos_x.items():
		if pos_values == 2:
			win_comb = pos_cle.split("_")

			#on identifie la valeur à jouer dans la combinaison gagnante
			for mat_cle, mat_values in matrice_updated.items():
				if mat_values in win_comb:
					win_x = mat_values
					break
				else:
					win_x = ""
	
	# Pour O
	# il ne reste que les vraies solutions = 2
	for pos_cle, pos_values in pos_o.items():
		if pos_values == 2:
			win_comb = pos_cle.split("_")

			#on identifie la valeur à jouer dans la combinaison gagnante
			for mat_cle, mat_values in matrice_updated.items():
				if mat_values in win_comb:
					win_o = mat_values
					break
				else:
					win_o = ""

	# Priorité à la victoire de l'ordinateur
	# Suivi du contre pour empecher l'adversaire de gagner
	if player_icon[1] == "O":
		if win_o != "" :
			win = win_o
		else:
			win = win_x

	if player_icon[1] == "X":
		if win_x != "" :
			win = win_x
		else:
			win = win_o

	return win

#tour de role
def current_player(player,icon):
	global user_choice
	#choix du joueur
	if j == 0:
		user_choice = input("{} ( {} ), a toi de jouer ! Choisi un chiffre parmi ceux restant ci-dessus : ".format(player,icon))

	if j == 1 and nb_player == "2":
		user_choice = input("{} ( {} ), a toi de jouer ! Choisi un chiffre parmi ceux restant ci-dessus : ".format(player,icon))
	#comb_gagnant = "" ou X gagnant ou O gagnant
	comb_gagnant = warning_winner()

	# Si c'est à l'ordinateur de jouer
	#	Et il y a un combo gagnant 
	#		Et que l'on joue contre l'ordinateur
	if j == 1 and comb_gagnant != "" and nb_player == "1" :
		# L'ordinateur gagne ou contre l'adversaire dans cette ordre
		user_choice = warning_winner()

	# Si c'est à l'ordinateur de jouer
	#	Et il y a pas de combo gagnant 
	#		Et que l'on joue contre l'ordinateur
	#			Et que ma stratégie pour jouer n'est pas vide
	if j == 1 and comb_gagnant == "" and nb_player == "1" and len(best_solution) > 0 :
		# L'ordinateur joue la meilleur stratégie
		user_choice = best_solution[0]




	#mise a jour des matrices
	matrice[user_choice] = icon
	matrice_updated[user_choice]= "_"
	if user_choice in best_solution :
		best_solution.remove(user_choice)


def position_alim(pos):
	global check
	for cle, values in pos.items():
		if str(user_choice) in cle:
			pos[cle] += 1

		if pos[cle] == 3:
			check = True
			break

if __name__ == "__main__":

	print(" ")
	print(" =======================")
	print(" === Voici la grille ===")
	print(" =======================")

	affichage(matrice_updated)

	print(" =======================")

	while True:
		check = False

		for i in range(0,9):
			j = i%2

			if check == False:
				affichage(matrice)

				current_player(player_name[j],player_icon[j])

				position_alim(player_pos[j])


			if check == True:
				affichage(matrice)
				print("Bravo {} tu as gagné !!! ".format(player_name[j]))
				break

			if i == 8:
				check = True
				affichage(matrice)
				print("Egalité ! Vous êtes tous les 2 trop forts ! ")
				break
		
		if check == True:
			break



