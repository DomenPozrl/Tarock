import pickle
import itertools
import random
from Tarock import Tarock

def is_right_state(state):
	mnozica = set()
	for label, val in state:
		mnozica.add(label)

	return len(mnozica) == len(state)

class QLearning:

	def __init__(self, gamma, alpha, eps):

		self.gamma = gamma
		self.alpha = alpha
		self.eps = eps


	def init_qtable(self):
		
		from qlearning_attributes import states, actions
		
		self.Q = dict()
		self.action_labels = actions
		for state in states:
			self.Q[tuple(state)] = [0 for action in actions]

	def store_qtable(self, filename, filename2):
		file = open(filename, "wb")
		pickle.dump(self.Q, file)
		file.close()

		file = open(filename2, "wb")
		pickle.dump(self.action_labels, file)
		file.close()


	def load_qtable(self, filename, filename2):
		self.Q = pickle.load(open(filename, "rb"))
		self.action_labels = pickle.load(open(filename2, "rb"))
	

	def get_action(self, state, legal_actions, randomly=True):
		if random.random() <= self.eps and randomly:
			random_action = random.choice(legal_actions)
			return random_action, self.Q[state][self.action_labels.index(random_action)]
		else:
			state_actions = self.Q[state]
			action_score_pairs = zip(self.action_labels, state_actions)
			filtered = list(filter(lambda x: x[0] in legal_actions, action_score_pairs))
			urejen = list(sorted(filtered, key=lambda x: x[1]))

		return urejen[-1]
		#return urejen[0]

	def update_table(self, state, action, reward, new_state):
		
		#get important parts
		new_state_score = self.get_action(new_state, self.action_labels, randomly=False)[1]
		action_index = self.action_labels.index(action)
		state_score = self.Q[state][action_index]

		#update table
		self.Q[state][action_index] = state_score + self.alpha * (reward + self.gamma*new_state_score - state_score)

				


if __name__ == "__main__":

	q = QLearning(0.3, 0.1, 0.1)
	#q.init_qtable()
	#q.store_qtable("qnew_1.pickle", "action_labels_1.pickle")
	q.load_qtable("qnew_1.pickle", "action_labels_1.pickle")

	strat3 = q.get_action
	
	player_strats = [strat3, strat3, strat3]
	number_of_games = 1000000
	counter = 0
	while counter < number_of_games:
		print(f"{int((counter/number_of_games)*10000)/100}% done")
		#print("========================================================================================= NEW GAME =========================================================================================")
		#print("============================================================================================================================================================================================")

		tarock = Tarock()
		cards = tarock.deal_cards()
		player1 = cards[0]
		player2 = cards[1]
		player3 = cards[2]
		talon = cards[3]
		players = [player1, player2, player3]
		#print("Player 0:")
		#tarock.print_hand(player1)
		#print("Player 1:")
		#tarock.print_hand(player2)
		#print("Player 2:")
		#tarock.print_hand(player3)
		#print("============================================================================================================================================================================================")
		discard = []

		starting_player = 0

		pairing = [0, (1,2)]

		#prvo mesto za solo playerja, drugo mesta za pair
		cummulative_reward = [0, 0]

		solo_player = pairing[0]
		pair = pairing[1]

		while player1 and player2 and player3:
				second_player = (starting_player + 1) % 3
				third_player = (starting_player + 2) % 3
				
				stack = []
				stack_order = []
				pomozna = []

				round_discard = []
				#print(f"Player {starting_player}:")
				#tarock.print_hand(players[starting_player])
				#print(f"Player {second_player}:")
				#tarock.print_hand(players[second_player])
				#print(f"Player {third_player}:")
				#tarock.print_hand(players[third_player])

				############################################################################################################################################
				#play the first move and calculate the new states. the rewards will be calculated at the end
				

				state1 = tarock.get_new_state(players[starting_player], discard, stack, second_player, third_player)
				card1, _ = player_strats[starting_player](state1, players[starting_player])
				#print(f"Player {starting_player} played: {tarock.id_to_cards[card1]}")
				
				#print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
				tarock.play_card(players[starting_player], card1)
				stack.append(card1)
				#print(f"Current stack:")
				#tarock.print_hand(stack)
				stack_order.append(starting_player)
				round_discard.append((card1, starting_player))
				newstate1 = tarock.get_new_state(players[starting_player], discard, stack, second_player, third_player)

				############################################################################################################################################
				#play the second move
				

				state2 = tarock.get_new_state(players[second_player], discard, stack, starting_player, third_player)
				card2, _ = player_strats[second_player](state2, players[second_player])
				#print(f"Player {second_player} played: {tarock.id_to_cards[card2]}")
				
				#print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

				tarock.play_card(players[second_player], card2)
				stack.append(card2)
				#print(f"Current stack:")
				#tarock.print_hand(stack)
				stack_order.append(second_player)
				round_discard.append((card2, second_player))
				newstate2 = tarock.get_new_state(players[second_player], discard, stack, starting_player, third_player)

				############################################################################################################################################
				#play the third move
				

				state3 = tarock.get_new_state(players[third_player], discard, stack, starting_player, second_player)
				card3, _ = player_strats[third_player](state3, players[third_player])
				#print(f"Player {third_player} played: {tarock.id_to_cards[card3]}")
				
				#print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

				tarock.play_card(players[third_player], card3)
				stack.append(card3)
				#print(f"Current stack:")
				#tarock.print_hand(stack)
				stack_order.append(third_player)
				round_discard.append((card3, third_player))
				newstate3 = tarock.get_new_state(players[third_player], discard, stack, starting_player, second_player)

				############################################################################################################################################
				#now get the winner and update the table three times with respective rewards
				winning_player_index = tarock.winning_player(stack) - 1 #because i'm a bad programmer and wasn't consistent
				winning_player = stack_order[winning_player_index]

				starting_player = winning_player
				#print(f"Winning player: {winning_player}")
				#print("============================================================================================================================================================================================")
				reward = tarock.eval_stack(stack)
				discard.append(round_discard)
				

				#update for starting player
				reward1 = reward if winning_player == starting_player else -1*reward
				q.update_table(state1, card1, reward1, newstate1)


				#update for second player
				reward2 = reward if winning_player == second_player else -1*reward
				q.update_table(state2, card2, reward2, newstate2)


				#update for second player
				reward3 = reward if winning_player == third_player else -1*reward
				q.update_table(state3, card3, reward3, newstate3)

		counter += 1

	q.store_qtable("qnew_1.pickle", "action_labels_1.pickle")