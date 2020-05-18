from play import Game
import pickle
from Tarock import Tarock
from qlearning import QLearningTarock
import random
from qlearning2 import QLearning

def random_choice(sez):
	return random.choice(sez)

if __name__ == "__main__":
	wins = 0
	score1 = 0
	score2 = 0
	count = 0
	"""
	https://medium.com/@SmartLabAI/reinforcement-learning-algorithms-an-intuitive-overview-904e2dff5bbc
	10000 games
	
	we are playing for score1
	**********************************************
	*************************************************************************************
	*************************************************************************************
	*FINAL RESULTS:
	Wins: 2558, win ratio: 0.2558
	Average score1: 25.0496
	Aerage score2: 37.145*
	*************************************************************************************
	*************************************************************************************

	we are playing for score2
	**********************************************
	*************************************************************************************
	*************************************************************************************
	*FINAL RESULTS:
	Wins: 1013, win ratio: 0.1013
	Average score1: 18.6741
	Aerage score2: 43.5919*
	*************************************************************************************
	*************************************************************************************
	

	we are playing for score 1
	*************************************************************************************
	*************************************************************************************
	*FINAL RESULTS:
	Wins: 990, win ratio: 0.099
	Average score1: 18.3591
	Aerage score2: 43.8611*
	*************************************************************************************
	*************************************************************************************

	we are playing for score 2
	*************************************************************************************
	*************************************************************************************
	*FINAL RESULTS:
	Wins: 2321, win ratio: 0.2321
	Average score1: 22.1396
	Aerage score2: 40.1107*
	*************************************************************************************
	*************************************************************************************
	"""
	q = QLearning(0.3, 0.1, 0.1)
	#q.init_qtable()
	#q.store_qtable("qnew_1.pickle", "action_labels_1.pickle")
	q.load_qtable("qnew_1.pickle", "action_labels_1.pickle")

	strat3 = q.get_action

	while count < 10000:	

		tarock = Tarock()
		cards = tarock.deal_cards()
		player1 = cards[0]
		player2 = cards[1]
		player3 = cards[2]
		talon = cards[3]
		players = [player1, player2, player3]
		
		#Q = QLearningTarock(0.3,0.1,0.1)
		#Q.load_qtables("q1_2.pickle", "q2_2.pickle")
		#strat3 = Q.return_action
		player_strats = [random_choice, random_choice, strat3]
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
			
			for player in [starting_player, second_player, third_player]:
				print(f"Player: {player} hand:")
				tarock.print_hand(players[player])
				if players[player] == player3:
					igralec_indexi = [0,1,2]
					igralec_indexi.remove(player)
					igralec2 = igralec_indexi[0]
					igralec3 = igralec_indexi[1]
					print(player, igralec2, igralec3, "A")
					state1 = tarock.get_new_state(players[player], discard, stack, igralec2, igralec3)
					card1, x = player_strats[player](state1, players[player], randomly=False)
					print(card1, x, "AAAAAAAAAAAAAAa")
					tarock.play_card(players[player], card1)
					stack.append(card1)
					stack_order.append(player)
					pomozna.append((card1, player))
				else:
					if len(stack) > 0:
						card = player_strats[player](tarock.legal_moves(stack[0], players[player]))
					else:
						card = player_strats[player](players[player])
					tarock.play_card(players[player], card)
					stack.append(card)
					stack_order.append(player)
					pomozna.append((card, player))
				
			discard.append(pomozna)	
			tarock.print_hand(stack)
			winner_index = tarock.winning_player(stack) - 1
			starting_player = stack_order[winner_index]

			#stejemo po tarokovsko
			#starting player je zdej ze nastavljen na winnerja runde
			if starting_player in pair:
				cummulative_reward[1] += tarock.eval_stack(stack)
			else:
				cummulative_reward[0] += tarock.eval_stack(stack)
			print(f"Winner: {starting_player}")
			print("---------------------------------------------------")
		print("**********************************************")
		print(f"Final tally of the game: {cummulative_reward}")
		print("**********************************************")

		score1 += cummulative_reward[0]
		score2 += cummulative_reward[1]

		if cummulative_reward[0] > cummulative_reward[1]:
			wins += 1

		count += 1

	print("*************************************************************************************")
	print("*************************************************************************************")
	print(f"*FINAL RESULTS:\nWins: {wins}, win ratio: {wins/count}\nAverage score1: {score1/count}\nAerage score2: {score2/count}*")
	print("*************************************************************************************")
	print("*************************************************************************************")


		