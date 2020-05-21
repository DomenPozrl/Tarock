def isHeart(karta_id):
        return karta_id >= 1 and karta_id <= 8
    
def isDiamond(karta_id):
    return karta_id >= 11 and karta_id <= 18

def isSpade(karta_id):
    return karta_id >= 21 and karta_id <= 28

def isClub(karta_id):
    return karta_id >= 31 and karta_id <= 38

def isTarock(karta_id):
    return karta_id >= 40 and karta_id <= 61

def is_same_color(karta1, karta2):
    return (isHeart(karta1) and isHeart(karta2)) or (isSpade(karta1) and isSpade(karta2)) or (isClub(karta1) and isClub(karta2)) or (isDiamond(karta1) and isDiamond(karta2)) or (isTarock(karta1) and isTarock(karta2))

def search_discard(discard, card):
        
        #[[(card, player), (card, player), (card, player)], [(card, player), (card, player), (card, player)]]
        
        for play in discard:

            for card1, player in play:
                if card1 == card:
                    return True
        return False

def winning_player(stack):
        
        first = stack[0]
        second = stack[1]
        third = stack[2]

        if is_same_color(first, second) and is_same_color(first, third):
            #returns the number of the winning player
            return stack.index(max(stack)) + 1
        elif isTarock(first) or isTarock(second) or isTarock(third):
            return stack.index(max(stack)) + 1
        elif is_same_color(first, second):
            return 1 if first > second else 2
        elif is_same_color(first,third):
            return 1 if first > third else 3
        else:
            return 1

def skrt_igrane_karte(player, c, discard):
    
    #look back at played hands
    for prvi, drugi, tretji in discard:
        player1 = prvi[1]
        player2 = drugi[1]
        player3 = tretji[1]

        karta1 = prvi[0]
        karta2 = drugi[0]
        karta3 = tretji[0]

        
        #samo ce ni prvi igralec nam pove a je skrt al ni
        if player != player1:

            #ce je nas player igralec 2 in je prva karta igrana iste barve kot karta za katero gledamo ce je skrt
            if player == player2 and is_same_color(karta1, c):
                
                #ce najdemo da je igral karto k ni iste barve potem return je skrt
                if not is_same_color(karta2, karta1):
                    return True
            if player == player3 and is_same_color(karta1, c):

                if not is_same_color(karta3, karta1):
                    return True
    return False

#returns list of cards that can win the stack
def lahko_poberes(stack, legal_moves):
	#
	if len(stack) == 1:

		#ce sta iste barve lahko poberejo vse tiste k so vecje
		if is_same_color(stack[0], legal_moves[0]):
			return [card for card in legal_moves if card > stack[0]]
		
		#ce nista iste barve in so moji legal movsi taroki lahko vsi poberejo
		elif isTarock(legal_moves[0]):
			return legal_moves
		
		#ce nista iste barve in so moji legal movsi karte druge barve pomen da ne morm z nicemer pobrat
		else:
			return []	

	else:

		c1 = stack[0]
		c2 = stack[1]

		#ce usi barvamo
		if is_same_color(c1, c2) and is_same_color(c1, legal_moves[0]):
			return [card for card in legal_moves if card > max(stack)]

		#ce c2 ne barva, ma taroka, jz barvam in ce c2 ne barva, ma taroka in jz ne barvam in nimam taroka
		elif not is_same_color(c1, c2) and isTarock(c2) and not isTarock(legal_moves[0]):
			return []

		#ce c2 ne barva, ma taroka, jz ne barvam, mam taroka
		elif not is_same_color(c1, c2) and isTarock(c2) and isTarock(legal_moves[0]):
			return [card for card in legal_moves if card > c2]

		#ce c2 barva in jz ne barvam, mam taroka
		elif is_same_color(c1, c2) and isTarock(legal_moves[0]):
			return legal_moves
		else:
			return []

#player2 in player3 sta naslednji in se naslednji igralec
def get_state_solo_first(hand, discard, player2, player3):
	"""
	state_solo_first_labels = [
		["herc kralj", [0,1,2]],
		["herc dama", [0, 1]],
		["karo kralj", [0,1,2]],
		["karo dama", [0, 1]],
		["pik kralj", [0,1,2]],
		["pik dama", [0, 1]],
		["kriz kralj", [0,1,2]],
		["kriz dama", [0, 1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["player2 skrt herc", [0,1]],
		["player2 skrt karo", [0,1]],
		["player2 skrt pik", [0,1]],
		["player2 skrt kriz", [0,1]],
		["player2 skrt taroki", [0,1]],
		["player3 skrt herc", [0,1]],
		["player3 skrt karo", [0,1]],
		["player3 skrt pik", [0,1]],
		["player3 skrt kriz", [0,1]],
		["player3 skrt taroki", [0,1]],
	]
	"""
	state = []

	#herc kralj
	if 8 in hand:
		state.append(1)
	elif search_discard(discard, 8):
		state.append(0)
	else:
		state.append(2)

	#herc dama
	if 7 in hand:
		state.append(1)
	else:
		state.append(0)

	#karo kralj
	if 18 in hand:
		state.append(1)
	elif search_discard(discard, 18):
		state.append(0)
	else:
		state.append(2)

	#karo dama
	if 17 in hand:
		state.append(1)
	else:
		state.append(0)


	#pik kralj
	if 28 in hand:
		state.append(1)
	elif search_discard(discard, 28):
		state.append(0)
	else:
		state.append(2)

	#pik dama
	if 27 in hand:
		state.append(1)
	else:
		state.append(0)

	#kriz kralj
	if 38 in hand:
		state.append(1)
	elif search_discard(discard, 38):
		state.append(0)
	else:
		state.append(2)

	#kriz dama
	if 37 in hand:
		state.append(1)
	else:
		state.append(0)

	#nizki taroki so od I do X 40 - 50
	#srednji taroki so od XI do XV 51 - 55
	#visoki so od XVII do ŠKIS 56 - 61

	#nizki taroki
	sem = False
	for tarok in range(40, 51):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	#srednji taroki
	sem = False
	for tarok in range(51, 56):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)


	#veliki taroki
	sem = False
	for tarok in range(56, 62):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	#player2 skrt herca
	if skrt_igrane_karte(player2, 8, discard):
		state.append(1)
	else:
		state.append(0)

	#player2 skrt kare
	if skrt_igrane_karte(player2, 18, discard):
		state.append(1)
	else:
		state.append(0)

	#player2 skrt pika
	if skrt_igrane_karte(player2, 28, discard):
		state.append(1)
	else:
		state.append(0)

	#player2 skrt kriza
	if skrt_igrane_karte(player2, 38, discard):
		state.append(1)
	else:
		state.append(0)

	#player2 skrt taroka
	if skrt_igrane_karte(player2, 61, discard):
		state.append(1)
	else:
		state.append(0)

	#player3 skrt herca
	if skrt_igrane_karte(player3, 8, discard):
		state.append(1)
	else:
		state.append(0)

	#player3 skrt kare
	if skrt_igrane_karte(player3, 18, discard):
		state.append(1)
	else:
		state.append(0)

	#player3 skrt pika
	if skrt_igrane_karte(player3, 28, discard):
		state.append(1)
	else:
		state.append(0)

	#player3 skrt kriza
	if skrt_igrane_karte(player3, 38, discard):
		state.append(1)
	else:
		state.append(0)

	#player3 skrt taroka
	if skrt_igrane_karte(player3, 61, discard):
		state.append(1)
	else:
		state.append(0)

	return tuple(state)







def get_state_solo_second(tarock_instance, stack, hand, discard, me, zadnji_player):
	"""
	state_solo_second_labels = [
		["vrednost prve karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]],
		["zadnji player skrt barve", [0,1]],
		["zadnji player skrt taroke", [0,1]]
	]
	"""
	state = []

	first_card = stack[0]
	legal_moves = tarock_instance.legal_moves(first_card, hand)
	poberes = lahko_poberes(stack, legal_moves)

	#vrednost prve karte
	state.append(tarock_instance.id_to_points[first_card])


	#a je prva karta tarok
	if tarock_instance.isTarock(first_card):
		state.append(1)
	else:
		state.append(0)

	#a sm skrt te barve
	if skrt_igrane_karte(me, first_card, discard):
		state.append(1)
	else:
		state.append(0)

	#a lahko poberem z barvo
	if len(poberes) > 0 and not isTarock(poberes[0]):
		state.append(1)
	else:
		state.append(0)

	#a lahko poberem s tarokom
	if len(poberes) > 0 and isTarock(poberes[0]):
		state.append(1)
	else:
		state.append(0)

	#nizki taroki
	sem = False
	for tarok in range(40, 51):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	#srednji taroki
	sem = False
	for tarok in range(51, 56):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)


	#veliki taroki
	sem = False
	for tarok in range(56, 62):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)
	
	#mamo kralja te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [8, 18, 28, 38]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	#mamo damo te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [7, 17, 27, 37]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)


	#mamo cavala te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [6, 16, 26, 36]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)


	#mamo poba te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [5, 15, 25, 35]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	#mamo platlca te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [4,3,2,1, 14, 13, 12, 11, 24, 23, 22, 21, 34, 33, 32, 31]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	if skrt_igrane_karte(zadnji_player, first_card, discard):
		state.append(1)
	else:
		state.append(0)

	if skrt_igrane_karte(zadnji_player, 61, discard):
		state.append(1)
	else:
		state.append(0)
	
	return tuple(state)

def get_state_solo_third(tarock_instance, stack, hand, discard, me):
	"""
	state_solo_second_labels = [
		["vrednost prve karte", [0,2,3,4,5]],
		["vrednost druge karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]],
	]
	"""
	state = []

	first_card = stack[0]
	second_card = stack[1]
	legal_moves = tarock_instance.legal_moves(first_card, hand)
	poberes = lahko_poberes(stack, legal_moves)

	#vrednost prve karte
	state.append(tarock_instance.id_to_points[first_card])

	#vrednost druge karte
	state.append(tarock_instance.id_to_points[second_card])
	
	#a je prva karta tarok
	if tarock_instance.isTarock(first_card):
		state.append(1)
	else:
		state.append(0)

	#a sm skrt te barve
	if skrt_igrane_karte(me, first_card, discard):
		state.append(1)
	else:
		state.append(0)

	#a lahko poberem z barvo
	if len(poberes) > 0 and not isTarock(poberes[0]):
		state.append(1)
	else:
		state.append(0)

	#a lahko poberem s tarokom
	if len(poberes) > 0 and isTarock(poberes[0]):
		state.append(1)
	else:
		state.append(0)

	#nizki taroki
	sem = False
	for tarok in range(40, 51):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	#srednji taroki
	sem = False
	for tarok in range(51, 56):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)


	#veliki taroki
	sem = False
	for tarok in range(56, 62):
		if tarok in hand:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)
	
	#mamo kralja te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [8, 18, 28, 38]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	#mamo damo te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [7, 17, 27, 37]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)


	#mamo cavala te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [6, 16, 26, 36]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)


	#mamo poba te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [5, 15, 25, 35]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	#mamo platlca te barve
	sem = False
	for card in hand:
		if is_same_color(first_card, card) and card in [4,3,2,1, 14, 13, 12, 11, 24, 23, 22, 21, 34, 33, 32, 31]:
			state.append(1)
			sem = True
			break
	if not sem:
		state.append(0)

	return tuple(state)


def get_state_duo_first(hand, discard, player2, player3, partner):
	"""state_duo_first_labels = [ 
		["herc kralj", [0,1,2]],
		["herc dama", [0, 1]],
		["karo kralj", [0,1,2]],
		["karo dama", [0, 1]],
		["pik kralj", [0,1,2]],
		["pik dama", [0, 1]],
		["kriz kralj", [0,1,2]],
		["kriz dama", [0, 1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["player2 skrt herc", [0,1]],
		["player2 skrt karo", [0,1]],
		["player2 skrt pik", [0,1]],
		["player2 skrt kriz", [0,1]],
		["player2 taroki", [0,1]],
		["player3 skrt herc", [0,1]],
		["player3 skrt karo", [0,1]],
		["player3 skrt pik", [0,1]],
		["player3 skrt kriz", [0,1]],
		["player3 taroki", [0,1]],
		["a je moj kolega zadnji", [0, 1]]
	]"""
	state = list(get_state_solo_first(hand, discard, player2, player3))
	if player3 == partner:
		state.append(1)
	else:
		state.append(0)

	return tuple(state)

def get_state_duo_second(tarock_instance, stack, hand, discard, me, zadnji_player, partner):
	"""
	state_duo_second_labels = [
		["vrednost prve karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]],
		["zadnji player skrt barve", [0,1]],
		["zadnji player ima se taroke", [0,1]],
		["a je za mano se kolega", [0, 1]]
	]
	"""
	state = list(get_state_solo_second(tarock_instance, stack, hand, discard, me, zadnji_player))

	if zadnji_player == partner:
		state.append(1)
	else:
		state.append(0)

	return tuple(state)

def get_state_duo_third(tarock_instance, stack, hand, discard, me):
	"""
	state_duo_third_labels = [
		["vrednost prve karte", [0,2,3,4,5]],
		["vrednost druge karte", [0,2,3,4,5]],
		["a lahko poberem z barvo", [0, 1]],
		["a lahko poberem s tarokom", [0, 1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]],
		["kolega ze pobere"], [0, 1]
	]


	"""
	state = list(get_state_solo_third(tarock_instance, stack, hand, discard, me))

	c1 = stack[0]
	c2 = stack[1]

	if (is_same_color(c1, c2) and c2 > c1) or (not is_same_color(c1, c2) and isTarock(c2)):
		state.append(1)
	else:
		state.append(0)

	return tuple(state)

def strong_open(hand):
	#get all the colors
	herc = list(sorted([card for card in hand if isHeart(card)]))
	karo = list(sorted([card for card in hand if isDiamond(card)]))
	pik = list(sorted([card for card in hand if isSpade(card)]))
	kriz = list(sorted([card for card in hand if isClub(card)]))

	maxherc = int(str(herc[-1])[-1])
	maxkaro = int(str(karo[-1])[-1])
	maxpik = int(str(pik[-1])[-1])
	maxkriz = int(str(kriz[-1])[-1])

	l = list(sorted([(0, maxherc), (1, maxkaro), (2, maxpik), (3, maxkriz)], key=lambda x: x[1]))[-1]

	if l[0] == 0:
		return herc[-1]
	elif l[0] == 1:
		return karo[-1]
	elif l[0] == 2:
		return pik[-1]
	else:
		return kriz[-1]

def weak_open(hand):
	#get all the colors
	herc = list(sorted([card for card in hand if isHeart(card)]))
	karo = list(sorted([card for card in hand if isDiamond(card)]))
	pik = list(sorted([card for card in hand if isSpade(card)]))
	kriz = list(sorted([card for card in hand if isClub(card)]))

	minherc = int(str(herc[0])[-1]) if len(herc) > 0 else 10
	minkaro = int(str(karo[0])[-1]) if len(karo) > 0 else 10
	minpik = int(str(pik[0])[-1]) if len(pik) > 0 else 10
	minkriz = int(str(kriz[0])[-1]) if len(kriz) > 0 else 10

	l = list(sorted([(0, minherc), (1, minkaro), (2, minpik), (3, minkriz)], key=lambda x: x[1]))[0]

	if l[0] == 0:
		return herc[0]
	elif l[0] == 1:
		return karo[0]
	elif l[0] == 2:
		return pik[0]
	else:
		return kriz[0]

def strong_tarock(hand):
	taroki = [card for card in hand if isTarock(card)]
	high_taroki = list(sorted([card for card in taroki if card in list(range(56, 62))]))

	return high_taroki[0]

def weak_tarock(hand):
	taroki = list(sorted([card for card in hand if isTarock(card)]))
	return taroki[0]

def take_low(legal_moves, stack):
	taking_moves = list(sorted(lahko_poberes(stack, legal_moves)))

	return taking_moves[0]

def take_high(legal_moves, stack):
	taking_moves = list(sorted(lahko_poberes(stack, legal_moves))) 
	if len(taking_moves) == 1:
		return taking_moves[0]
	elif len(taking_moves) == 2:
		return taking_moves[1]
	else:
		return taking_moves[len(taking_moves)//2]

def take_allin(legal_moves, stack):
	taking_moves = list(sorted(lahko_poberes(stack, legal_moves)))
	return taking_moves[-1]

def let_go(legal_moves):
	return list(sorted(legal_moves))[0]

def partner_open(state_duo_first, legal_moves): #legal moves here should just be hand because this is the opening action
	if state_duo_first[-1] != 1:
		#to pomeni da je moj parnter zadnji (player3)
		herci = [card for card in legal_moves if is_same_color(card, 8)]
		karo = [card for card in legal_moves if is_same_color(card, 18)]
		piki = [card for card in legal_moves if is_same_color(card, 28)]
		krizi = [card for card in legal_moves if is_same_color(card, 38)]
		
		#skrt herca
		if state_duo_first[11] == 1 and len(herci) > 0:
			return list(sorted(herci))[0]
		elif state_duo_first[12] == 1 and len(karo) > 0:
			return list(sorted(karo))[0]
		elif state_duo_first[13] == 1 and len(piki) > 0:
			return list(sorted(piki))[0]
		elif state_duo_first[14] == 1 and len(krizi) > 0:
			return list(sorted(krizi))[0]
		else:
			return list(sorted(legal_moves))[0]
	else:
		#to pomeni da je moj parnter zadnji (player3)
		herci = [card for card in legal_moves if is_same_color(card, 8)]
		karo = [card for card in legal_moves if is_same_color(card, 18)]
		piki = [card for card in legal_moves if is_same_color(card, 28)]
		krizi = [card for card in legal_moves if is_same_color(card, 38)]
		
		#skrt herca
		if state_duo_first[15] == 1 and len(herci) > 0:
			return list(sorted(herci))[0]
		elif state_duo_first[16] == 1 and len(karo) > 0:
			return list(sorted(karo))[0]
		elif state_duo_first[17] == 1 and len(piki) > 0:
			return list(sorted(piki))[0]
		elif state_duo_first[18] == 1 and len(krizi) > 0:
			return list(sorted(krizi))[0]
		else:
			return list(sorted(legal_moves))[0]

def add_more(legal_moves):
	movi = list(sorted(legal_moves))
	return movi[-1]

def action_solo_first(hand, action):
	actions_solo_first_labels = ["strong open", "weak open", "strong tarock", "weak tarock"]

	if action == 3:
		try:
			return weak_tarock(hand)
		except:
			4

	if action == 2:
		try:
			return strong_tarock(hand)
		except:
			4

	if action == 0:
		try:
			return strong_open(hand)
		except:
			4
	if action == 1:
		try:
			return weak_open(hand)
		except:
			4
	


def action_solo_second(legal_moves, action, stack):
	actions_solo_second_labels = ["take low", "take high", "take all in", "let go"]
	pobiralnica = lahko_poberes(stack, legal_moves)
	if action == 0 and len(pobiralnica) > 0:
		return take_low(legal_moves, stack)
	elif action == 1 and len(pobiralnica) > 0:
		return take_high(legal_moves, stack)
	elif action == 2 and len(pobiralnica) > 0:
		return take_allin(legal_moves, stack)
	else:
		return let_go(legal_moves)

def action_solo_third(legal_moves, action, stack):
	actions_solo_third_labels = ["take low", "take high", "take all in", "let go"]
	pobiralnica = lahko_poberes(stack, legal_moves)
	if action == 0 and len(pobiralnica) > 0:
		return take_low(legal_moves, stack)
	elif action == 1 and len(pobiralnica) > 0:
		return take_high(legal_moves, stack)
	elif action == 2 and len(pobiralnica) > 0:
		return take_allin(legal_moves, stack)
	else:
		return let_go(legal_moves)

def action_duo_first(hand, action, state):
	actions_duo_first_labels = ["strong open", "weak open", "strong tarock", "weak tarock", "partner open"]
	"""if action == 0:
		return strong_open(hand)
	elif action == 1:
		return weak_open(hand)
	elif action == 2:
		return strong_tarock(hand)
	elif action == 3:
		return weak_tarock(hand)
	else:
		return partner_open(state, hand)"""

	if action == 3:
		try:
			return weak_tarock(hand)
		except:
			4

	if action == 2:
		try:
			return strong_tarock(hand)
		except:
			4

	if action == 0:
		try:
			return strong_open(hand)
		except:
			4
	if action == 1:
		try:
			return weak_open(hand)
		except:
			4
	if action == 4:
		try:
			return partner_open(state, hand)
		except:
			4

def action_duo_second(legal_moves, action, stack):
	actions_duo_second_labels = ["take low", "take high", "take all in", "let go", "add more"]
	pobiralnica = lahko_poberes(stack, legal_moves)
	if action == 0 and len(pobiralnica) > 0:
		return take_low(legal_moves, stack)
	elif action == 1 and len(pobiralnica) > 0:
		return take_high(legal_moves, stack)
	elif action == 2 and len(pobiralnica) > 0 :
		return take_allin(legal_moves, stack)
	elif action == 3:
		return let_go(legal_moves)
	else:
		return add_more(legal_moves)

def action_duo_third(legal_moves, action, stack):
	actions_duo_third_labels = ["take low", "take high", "take all in", "let go", "add more"]
	pobiralnica = lahko_poberes(stack, legal_moves)
	if action == 0 and len(pobiralnica) > 0:
		return take_low(legal_moves, stack)
	elif action == 1 and len(pobiralnica) > 0:
		return take_high(legal_moves, stack)
	elif action == 2 and len(pobiralnica) > 0:
		return take_allin(legal_moves, stack)
	elif action == 3:
		return let_go(legal_moves)
	else:
		return add_more(legal_moves)

#rewards

def reward_solo_first(tarock_instance, stack, stack_order, hand, action):
	me = stack_order[0]
	my_card = stack[0]

	stack_value = tarock_instance.eval_stack(stack)
	winner = stack_order[tarock_instance.winning_player(stack)-1]

	actions_solo_first_labels = ["strong open", "weak open", "strong tarock", "weak tarock"]
	legal_moves = tarock_instance.legal_moves(stack[0], hand)
	"""
	se reward:
 	nagradis ko odpre strong in pobere (premo sorazmerno s tockami k pobere)
	kaznujes ko odpre strong in ne pobere -||-
	nagradis ko odpre weak in nasprotnik pobere malo (premo sorazmerno s tockami k jih nasprotnik pobere)
	kaznuje k odpres weak in nasportnik pobere veliko 
	kaznuje k odpres weak ampak bi ti lahko pobral ce bi odpru strong (prides vn z platlcom padejo dol pob pa kaval, ti mas pa kralja u roki al pa damo)
	nagradis neki ko tarokiras in poberes
	nagradis malo man ko tarokiras ampak ne poberes
	kaznujes ko probas tarokirat pa zgubis tocke vec kot 1

	"""
	reward = 0

	if action == 0 and winner == me:
		reward += stack_value
	if action == 0 and winner != me:
		reward += -1* stack_value
	



	if action == 1 and winner != me:
		#kaznujes ce odpres weak in pobere nasprotnik ampak bi lahko stih ti pobral
		if len(lahko_poberes(stack[1:], legal_moves)) > 0:
			reward += -1*stack_value

		elif stack_value <= 2:
			reward += 2
		else:
			reward += (-1 * stack_value)/3

	if action == 2:
		if winner == me:
			reward += 2
		else:
			if stack_value > 2:
				reward += -2

	if action == 3:
		if winner == me:
			reward += 3
		else:
			if stack_value > 3:
				reward += -3

	return reward

def reward_solo_second(tarock_instance, stack, stack_order, hand, action):
	"""
	
	reward:
	nagradis ce poberes stih na koncu glede na to kok si pobral
	zdej ce poberes high pa te on cufne more bit mal kazni
	ce poberes all in pa te on cufne more bit se vec kazni
	ce poberes low pa te on cufne pol je zelo malo kazni
	ce spustis pa je kazen ce pridejo tocke skoz
	ce spustis pa poberes je 0 tock vredno

	pa pac te kazni morjo bit tko ane, ce ne mors druzga kt spustit nevem ce je kulm
	da te kaznujem sam po drugi strani pa to povzroca da sparas karte mogoce
	"""
	me = stack_order[1]
	my_card = stack[1]

	stack_value = tarock_instance.eval_stack(stack)
	winner = stack_order[tarock_instance.winning_player(stack)-1]
	legal_moves = tarock_instance.legal_moves(stack[0], hand)
	actions_solo_second_labels = ["take low", "take high", "take all in", "let go"]

	reward = 0

	if action == 0:
		if winner == me:
			reward += stack_value
		else:
			reward += -1 *stack_value/3
	if action == 1:
		if winner == me:
			reward += 1.5 * stack_value
		else:
			reward += -1 * stack_value/2
	if action == 2:
		if winner == me:
			reward += 2 * stack_value
		else:
			reward += -1 * stack_value
	if action == 3:
		if winner != me:
			if stack_value == 0:
				reward += 2
			else:
				if len(lahko_poberes([stack[0], stack[2]], legal_moves)) > 0:
					reward += -1 * stack_value

	return reward

def reward_solo_third(tarock_instance, stack, stack_order, hand, action):
	"""
	reward
	tolko tock kokr poberes
	ampak ce poberes z high pa bi lahko z low je kazen
	ce poberes z all in pa bi lahko z high je kazen
	ce poberes z all in pa bi lahko z low je mega kazen
	"""
	me = stack_order[2]
	my_card = stack[2]

	stack_value = tarock_instance.eval_stack(stack)
	winner = stack_order[tarock_instance.winning_player(stack)-1]
	legal_moves = tarock_instance.legal_moves(stack[0], hand)
	actions_solo_third_labels = ["take low", "take high", "take all in", "let go"]
	poberes = lahko_poberes(stack[:2], legal_moves)

	if winner == me:
		reward = 2*stack_value
	else:
		if(len(poberes)) > 0 and action != 3:
			reward = -3 * stack_value
			return reward
		else:
			if (len(poberes)) == 0:
				reward = 0

	if not isTarock(my_card) and winner == me and (action in [0,1,2]):
		reward += 5

	if isTarock(my_card) and action == 1:
		if min(poberes) < my_card:
			reward += -2

	if isTarock(my_card) and action == 2:
		if min(poberes) < my_card:
			reward += -2

	if len(poberes) > 0 and action==3 and winner != me:
		reward = -20

	return reward


def reward_duo_first(tarock_instance, stack, stack_order, hand, action, kolega):
	
	us = [stack_order[0], kolega]
	my_card = stack[0]

	stack_value = tarock_instance.eval_stack(stack)
	winner = stack_order[tarock_instance.winning_player(stack)-1]

	actions_solo_first_labels = ["strong open", "weak open", "strong tarock", "weak tarock", "partner open"]
	legal_moves = tarock_instance.legal_moves(stack[0], hand)
	"""
	se reward:
 	nagradis ko odpre strong in pobere (premo sorazmerno s tockami k pobere)
	kaznujes ko odpre strong in ne pobere -||-
	nagradis ko odpre weak in nasprotnik pobere malo (premo sorazmerno s tockami k jih nasprotnik pobere)
	kaznuje k odpres weak in nasportnik pobere veliko 
	kaznuje k odpres weak ampak bi ti lahko pobral ce bi odpru strong (prides vn z platlcom padejo dol pob pa kaval, ti mas pa kralja u roki al pa damo)
	nagradis neki ko tarokiras in poberes
	nagradis malo man ko tarokiras ampak ne poberes
	kaznujes ko probas tarokirat pa zgubis tocke vec kot 1

	"""
	reward = 0

	if action == 0 and winner in us:
		reward += stack_value
	if action == 0 and winner not in us:
		reward += -1* stack_value
	



	if action == 1 and winner not in us:
		#kaznujes ce odpres weak in pobere nasprotnik ampak bi lahko stih ti pobral
		if len(lahko_poberes(stack[1:], legal_moves)) > 0:
			reward += -1*stack_value
		elif stack_value <= 2:
			reward += 2
		else:
			reward += (-1 * stack_value)/3

	if action == 2:
		if winner in us:
			reward += 2
		else:
			if stack_value > 2:
				reward += -2

	if action == 3:
		if winner in us:
			reward += 3
		else:
			if stack_value > 3:
				reward += -3

	if action == 4:
		if winner == kolega:
			reward += stack_value
		else:
			reward += -1 * stack_value/2

	return reward

def reward_duo_second(tarock_instance, stack, stack_order, hand, action, kolega):
	"""
	
	reward:
	nagradis ce poberes stih na koncu glede na to kok si pobral
	zdej ce poberes high pa te on cufne more bit mal kazni
	ce poberes all in pa te on cufne more bit se vec kazni
	ce poberes low pa te on cufne pol je zelo malo kazni
	ce spustis pa je kazen ce pridejo tocke skoz
	ce spustis pa poberes je 0 tock vredno

	pa pac te kazni morjo bit tko ane, ce ne mors druzga kt spustit nevem ce je kulm
	da te kaznujem sam po drugi strani pa to povzroca da sparas karte mogoce
	"""
	us = [stack_order[1], kolega]
	my_card = stack[1]

	stack_value = tarock_instance.eval_stack(stack)
	winner = stack_order[tarock_instance.winning_player(stack)-1]
	legal_moves = tarock_instance.legal_moves(stack[0], hand)
	actions_solo_second_labels = ["take low", "take high", "take all in", "let go"]

	reward = 0

	if action == 0:
		if winner in us:
			reward += stack_value
		else:
			reward += -1 *stack_value/3
	if action == 1:
		if winner in us:
			reward += 1.5 * stack_value
		else:
			reward += -1 * stack_value/2
	if action == 2:
		if winner in us:
			reward += 2 * stack_value
		else:
			reward += -1 * stack_value
	if action == 3:
		if winner not in us:
			if stack_value == 0:
				reward += 2
			else:
				if len(lahko_poberes([stack[0], stack[2]], legal_moves)) > 0:
					reward += -1 * stack_value

	return reward

def reward_duo_third(tarock_instance, stack, stack_order, hand, action, kolega):
	"""
	reward
	tolko tock kokr poberes
	ampak ce poberes z high pa bi lahko z low je kazen
	ce poberes z all in pa bi lahko z high je kazen
	ce poberes z all in pa bi lahko z low je mega kazen
	"""
	us = [stack_order[2], kolega]
	my_card = stack[2]

	stack_value = tarock_instance.eval_stack(stack)
	winner = stack_order[tarock_instance.winning_player(stack)-1]
	legal_moves = tarock_instance.legal_moves(stack[0], hand)
	actions_solo_third_labels = ["take low", "take high", "take all in", "let go"]
	poberes = lahko_poberes(stack[:2], legal_moves)

	if winner in us:
		reward = 2*stack_value
	else:
		if(len(poberes)) > 0 and action != 3:
			reward = -3 * stack_value
			return reward
		else:
			if (len(poberes)) == 0:
				reward = 0

	if not isTarock(my_card) and winner in us and (action in [0,1,2]):
		reward += 5

	if isTarock(my_card) and action == 1 and winner in us:
		if min(poberes) < my_card:
			reward += -2

	if isTarock(my_card) and action == 2 and winner in us:
		if min(poberes) < my_card:
			reward += -2

	if len(poberes) > 0 and action==3 and winner not in us:
		reward = -20

	return reward

if __name__ == "__main__":
	print(strong_open([53, 5, 51, 58, 28, 27, 32, 12, 18, 49, 44, 35, 54, 26, 60, 37]))
	print(weak_open([53, 5, 51, 58, 28, 27, 32, 12, 18, 49, 44, 35, 54, 26, 60, 37]))
	print("| XIV (53) | B♥ (5) | XII (51) | XIX (58) | K♠ (28) | Q♠ (27) | 8♣ (32) | 3♦ (12) | K♦ (18) | X (49) | V (44) | B♣ (35) | XV (54) | C♠ (26) | XXI (60) | Q♣ (37) |")