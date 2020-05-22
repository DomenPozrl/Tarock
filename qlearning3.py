import pickle
import random
from state_and_reward import *
from Tarock import Tarock
class QlearningFinal:

	def __init__(self, alpha, eps, parts = False):
		self.alpha = alpha
		self.eps = eps

		self.q_solo_first = pickle.load(open("q_solo_first.pickle", "rb"))
		self.q_solo_second = pickle.load(open("q_solo_second.pickle", "rb"))
		self.q_solo_third = pickle.load(open("q_solo_third.pickle", "rb"))
		print("Loaded solo player tables")
		if not parts:
			self.q_duo_first = pickle.load(open("q_duo_first.pickle", "rb"))
		else:
			d = pickle.load(open("q_duo_first_1.pickle", "rb"))
			d2 = pickle.load(open("q_duo_first_2.pickle", "rb"))
			x = dict()

			for a in d:
				x[a] = d[a]
			for a in d2:
				x[a] = d2[a]
			self.q_duo_first = x
			del d
			del d2
		print("Loaded the big kahuna")
		self.q_duo_second = pickle.load(open("q_duo_second.pickle", "rb"))
		self.q_duo_third = pickle.load(open("q_duo_third.pickle", "rb"))

	def store_qtables(self):
		file = open("q_solo_first.pickle", "wb")
		pickle.dump(self.q_solo_first, file)
		file.close()

		del self.q_solo_first

		print("A")
		file = open("q_solo_second.pickle", "wb")
		pickle.dump(self.q_solo_second, file)
		file.close()

		del self.q_solo_second

		print("B")
		file = open("q_solo_third.pickle", "wb")
		pickle.dump(self.q_solo_third, file)
		file.close()

		del self.q_solo_third

		print("C")
		kljuci = list(self.q_duo_first.keys())
		kljucil = len(kljuci)//2

		#a = l[0:ll//2] + l[ll//2:ll]

		prva_polovica = kljuci[0:kljucil//2]
		druga_polovica = kljuci[kljucil//2:kljucil]

		q_duo_first_1 = {key: self.q_duo_first[key] for key in prva_polovica}

		file = open("q_duo_first_1.pickle", "wb")
		pickle.dump(q_duo_first_1, file)
		file.close()

		print("D")

		del q_duo_first_1

		q_duo_first_2 = {key: self.q_duo_first[key] for key in druga_polovica}

		file = open("q_duo_first_2.pickle", "wb")
		pickle.dump(q_duo_first_2, file)
		file.close()


		print("DD")

		file = open("q_duo_second.pickle", "wb")
		pickle.dump(self.q_duo_second, file)
		file.close()

		print("E")
		file = open("q_duo_third.pickle", "wb")
		pickle.dump(self.q_duo_third, file)
		file.close()
		print("F")

	def update_tables(self, state1, a1, rw1, state2, a2, rw2, state3, a3, rw3, state4, a4, rw4, state5, a5, rw5, state6, a6, rw6):
		if rw1 != 0:
			self.q_solo_first[state1][a1] += self.alpha * rw1 
		if rw2 != 0:
			self.q_solo_second[state2][a2] += self.alpha * rw2
		if rw3 != 0:
			self.q_solo_third[state3][a3] += self.alpha * rw3
		if rw4 != 0:
			self.q_duo_first[state4][a4] += self.alpha * rw4
		if rw5 != 0:
			self.q_duo_second[state5][a5] += self.alpha * rw5
		if rw6 != 0:
			self.q_duo_third[state6][a6] += self.alpha * rw6
	
	def get_action(self, table, state):
		
			if table == 0:
				return list(sorted(list(enumerate(self.q_solo_first[state])), key=lambda x: x[1]))
			if table == 1:
				return list(sorted(list(enumerate(self.q_solo_second[state])), key=lambda x: x[1]))
			if table == 2:
				return list(sorted(list(enumerate(self.q_solo_third[state])), key=lambda x: x[1]))
			if table == 3:
				return list(sorted(list(enumerate(self.q_duo_first[state])), key=lambda x: x[1]))
			if table == 4:
				return list(sorted(list(enumerate(self.q_duo_second[state])), key=lambda x: x[1]))
			if table == 5:
				return list(sorted(list(enumerate(self.q_duo_third[state])), key=lambda x: x[1]))

	def get_action_wrapper(self, table, state, hand):
		mam_taroka = False
		for card in hand:
			if isTarock(card):
				mam_taroka = True

		if random.random() < self.eps:
			if mam_taroka:
				if table == 0:
					return random.choice(list(range(len(self.q_solo_first[state]))))
				if table == 1:
					return random.choice(list(range(len(self.q_solo_second[state]))))
				if table == 2:
					return random.choice(list(range(len(self.q_solo_third[state]))))
				if table == 3:
					return random.choice(list(range(len(self.q_duo_first[state]))))
				if table == 4:
					return random.choice(list(range(len(self.q_duo_second[state]))))
				if table == 5:
					return random.choice(list(range(len(self.q_duo_third[state]))))
			else:
				if table == 0:
					return random.choice([1,2])
				if table == 1:
					return random.choice(list(range(len(self.q_solo_second[state]))))
				if table == 2:
					return random.choice(list(range(len(self.q_solo_third[state]))))
				if table == 3:
					return random.choice([1,2,3])
				if table == 4:
					return random.choice(list(range(len(self.q_duo_second[state]))))
				if table == 5:
					return random.choice(list(range(len(self.q_duo_third[state]))))

		else:
			akcije = list(reversed(self.get_action(table, state)))

			if table == 0 or table == 3:
				if mam_taroka:
					return akcije[0][0]
				else:
					for akcija, cena in akcije:
						if akcija not in [2,3]:
							return akcija
			else:
				return akcije[0][0]

if __name__ == "__main__":

	ql = QlearningFinal(0.1, 0.1)
	print("Loaded the Q-tables")

	number_of_games = 100000
	counter = 0
	while counter < number_of_games:
		print(f"{int((counter/number_of_games)*10000)/100}% done")

		##################SET UP THE GAME####################
		tarock = Tarock()
		cards = tarock.deal_cards()
		player1 = cards[0]
		player2 = cards[1]
		player3 = cards[2]
		talon = cards[3]
		players = [player1, player2, player3]

		#################DECIDE PAIRING######################
		solo_player = random.choice([0, 1, 2])
		duo = [x for x in [0, 1, 2] if x != solo_player]

		#the solo player starts
		starting_player = solo_player
		second_player = duo[0]
		third_player = duo[1]

		###########SETUP CORRECT TABLE CONNECTIONS##########
		solo_tables = [ql.q_solo_first, ql.q_solo_second, ql.q_solo_third]
		duo_tables = [ql.q_duo_first, ql.q_duo_second, ql.q_duo_third]

		#set up discard pile
		discard = []

		#############START PLAYING THE GAME###################
		while player1 and player2 and player3:

			#adjust for the new starting player
			second_player = (starting_player + 1) % 3
			third_player = (starting_player + 2) % 3


			#reset the stack and stack_order
			stack = []
			stack_order = []
			
			#to know how to pass to update table
			table_indexes = []
			forced_moves = []
			#######################################################################
			########################### FIRST PLAYER ##############################
			#######################################################################

			if starting_player == solo_player:
				
				#get the correct state
				state1 = get_state_solo_first(players[starting_player], discard, second_player, third_player)
				
				#get the best action
				action1 = ql.get_action_wrapper(0, state1, players[starting_player])

				#get the card that is played by this action
				card1 = action_solo_first(players[starting_player], action1)

				#append the card to the stack and player to stack_order
				stack.append(card1)
				stack_order.append(starting_player)

				#play the card
				tarock.play_card(players[starting_player], card1)
				table_indexes.append(0)
			else:

				#get the partner
				partner = duo[0] if starting_player == duo[1] else duo[1]

				#get the correct state
				state1 = get_state_duo_first(players[starting_player], discard, second_player, third_player, partner)
				
				#get the best action
				action1 = ql.get_action_wrapper(3, state1, players[starting_player])

				#get the card that is played by this action
				card1 = action_duo_first(players[starting_player], action1, state1)

				#append the card to the stack and player to stack_order
				stack.append(card1)
				stack_order.append(starting_player)

				#play the card
				tarock.play_card(players[starting_player], card1)
				table_indexes.append(3)

			#######################################################################
			########################### SECOND PLAYER #############################
			#######################################################################

			if second_player == solo_player:
				#get legal moves for this round
				legal_moves1 = tarock.legal_moves(card1, players[second_player])
				
				#get the correct state
				state2 = get_state_solo_second(tarock, stack, players[second_player], discard, second_player, third_player)
				
				#get the best action
				action2 = ql.get_action_wrapper(1, state2, players[second_player])

				if len(legal_moves1) > 1:
					#get the card that is played by this action
					card2 = action_solo_second(legal_moves1, action2, stack)
					forced_moves.append(False)
				else:
					forced_moves.append(True)
					card2 = legal_moves1[0]
				#append the card to the stack and player to stack_order
				stack.append(card2)
				stack_order.append(second_player)

				#play the card
				tarock.play_card(players[second_player], card2)
				table_indexes.append(1)
			else:
				legal_moves1 = tarock.legal_moves(card1, players[second_player])
				#get the partner
				partner = duo[0] if second_player == duo[1] else duo[1]

				
				#get the correct state
				state2 = get_state_duo_second(tarock, stack, players[second_player], discard, second_player, third_player, partner)
				
				#get the best action
				action2 = ql.get_action_wrapper(4, state2, players[second_player])
				if len(legal_moves1) > 1:
					#get the card that is played by this action
					card2 = action_duo_second(legal_moves1, action2, stack)
					forced_moves.append(False)
				else:
					forced_moves.append(True)
					card2 = legal_moves1[0]

				#append the card to the stack and player to stack_order
				stack.append(card2)
				stack_order.append(second_player)

				#play the card
				tarock.play_card(players[second_player], card2)
				table_indexes.append(4)

			#######################################################################
			############################ THIRD PLAYER #############################
			#######################################################################

			if third_player == solo_player:
				
				#get legal moves for this round
				legal_moves2 = tarock.legal_moves(card1, players[third_player])

				
				#get the correct state
				state3 = get_state_solo_third(tarock, stack, players[third_player], discard, third_player)
				
				#get the best action
				action3 = ql.get_action_wrapper(2, state3, players[third_player])
				if len(legal_moves2) > 1:
					#get the card that is played by this action
					card3 = action_solo_third(legal_moves2, action3, stack)
					forced_moves.append(False)
				else:
					forced_moves.append(True)
					card3 = legal_moves2[0]
				#append the card to the stack and player to stack_order
				stack.append(card3)
				stack_order.append(third_player)

				#play the card
				tarock.play_card(players[third_player], card3)
				table_indexes.append(2)
			else:

				legal_moves2 = tarock.legal_moves(card1, players[third_player])
				#get the partner
				partner = duo[0] if third_player == duo[1] else duo[1]

				

				#get the correct state
				state3 = get_state_duo_third(tarock, stack, players[third_player], discard, third_player)
				
				#get the best action
				action3 = ql.get_action_wrapper(5, state3, players[third_player])

				if len(legal_moves2) > 1:
					#get the card that is played by this action
					card3 = action_duo_third(legal_moves2, action3, stack)
					forced_moves.append(False)
				else:
					forced_moves.append(True)
					card3 = legal_moves2[0]

				#append the card to the stack and player to stack_order
				stack.append(card3)
				stack_order.append(third_player)

				#play the card
				tarock.play_card(players[third_player], card3)
				table_indexes.append(5)

			#######################################################################
			############################## REWARDS ################################
			#######################################################################

			winning_player_index = tarock.winning_player(stack) - 1 #because i'm a bad programmer and wasn't consistent
			winning_player = stack_order[winning_player_index]

			if starting_player == solo_player:
				rw1 = reward_solo_first(tarock, stack, stack_order, players[starting_player], action1)
			else:
				partner = duo[0] if starting_player == duo[1] else duo[1]
				rw1 = reward_duo_first(tarock, stack, stack_order, players[starting_player], action1, partner)


			if second_player == solo_player:
				if forced_moves[0]:
					rw2 = 0
				else:
					rw2 = reward_solo_second(tarock, stack, stack_order, players[second_player], action2)
			else:
				partner = duo[0] if second_player == duo[1] else duo[1]
				if forced_moves[0]:
					rw2 = 0
				else:
					rw2 = reward_duo_second(tarock, stack, stack_order, players[second_player], action2, partner)

			if third_player == solo_player:
				if forced_moves[1]:
					rw3 = 0
				else:
					rw3 = reward_solo_third(tarock, stack, stack_order, players[second_player], action3)
			else:
				partner = duo[0] if third_player == duo[1] else duo[1]
				if forced_moves[1]:
					rw3 = 0
				rw3 = reward_duo_third(tarock, stack, stack_order, players[third_player], action3, partner)

			#print(table_indexes)
			#ql.update_tables(state1, a1, rw1, state2, a2, rw2, state3, a3, rw3, state4, a4 rw4, state5, a5 rw5, state6, a6 rw6)
			if table_indexes == [0,4,5]:
				#q solo first
				#q duo second
				#q duo third
				
				ql.update_tables(state1, action1, rw1, 0, 0, 0, 0, 0, 0, 0, 0, 0, state2, action2, rw2, state3, action3, rw3)
			elif table_indexes == [3,1,5]:
				#q duo first
				#q solo second
				#q duo third
				ql.update_tables(0,0,0, state2, action2, rw2, 0, 0, 0, state1, action1, rw1, 0, 0, 0, state3, action3, rw3)
			else:
				#[3,4,2]
				#q duo first
				#q duo second
				#q solo third
				ql.update_tables(0,0,0,0,0,0,state3, action3, rw3, state1, action1, rw1, state2, action2, rw2, 0,0,0)

			discard.append(list(zip(stack, stack_order)))
			starting_player = winning_player
		counter += 1

	ql.store_qtables()
