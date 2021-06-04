
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

player_name = []
player_icon = []

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
	
else:
	player2_icon = "X"

	player_name.append(str(player1_name))
	player_name.append(str(player2_name))

	player_icon.append(player1_icon.upper())
	player_icon.append(player2_icon.upper())

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


#tour de role
def current_player(player,icon):
	global user_choice
	#choix du joueur
	user_choice = input("{} ( {} ), a toi de jouer ! Choisi un chiffre parmi ceux restant ci-dessus : ".format(player,icon))

	#mise a jour de la matrice
	matrice[user_choice] = icon
	matrice_updated[user_choice]= "_"


def position_x_alim():
	global check
	for cle, values in position_x.items():
		if str(user_choice) in cle:
			position_x[cle] += 1

		if position_x[cle] == 3:
			check = True
			break

def position_o_alim():
	global check
	for cle, values in position_o.items():
		if str(user_choice) in cle:
			position_o[cle] += 1

		if position_o[cle] == 3:
			check = True
			break

print(" ")
print(" =======================")
print(" === Voici la grille ===")
print(" =======================")

affichage(matrice_updated)

print(" =======================")

icon_start = "X"
while True:
	check = False

	for i in range(0,9):
		j = i%2

		if check == False:
			affichage(matrice)

			current_player(player_name[j],player_icon[j])

			if player_icon[j] == "X":
				position_x_alim()
			if player_icon[j] == "O":
				position_o_alim()

		if i == 8:
			print("Egalité ! Vous êtes tous les 2 trop forts ! ")
			break
			
		if check == True:
			affichage(matrice)
			print("Bravo {} tu as gagné !!! ".format(player_name[j]))
			break

	
	if check == True:
		break

