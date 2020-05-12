from play import Game
import pickle
from Tarock import Tarock
from qlearning import QLearningTarock
import random

def random_choice(sez):
	return random.choice(sez)

if __name__ == "__main__":
	tarock = Tarock()
	cards = tarock.deal_cards()
	player1 = cards[0]
	player2 = cards[1]
	player3 = cards[2]
	talon = cards[3]
	players = [player1, player2, player3]
	
	Q = QLearningTarock(0.3,0.1,0.1)
	Q.load_qtables("q1_2.pickle", "q2_2.pickle")
	strat3 = Q.return_action
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

		for player in [starting_player, second_player, third_player]:
			print(f"Player: {player} hand:")
			tarock.print_hand(players[player])
			if players[player] == player3:
				if len(stack) == 0:
					state = tarock.get_state_wrapper(player_id=starting_player,
												player2=second_player,
												player3=third_player,
												current_stack=stack,
												stack_value=sum([tarock.id_to_points[c] for c in stack]), 
												legal_moves=players[player],
												hand=players[player],
												discard=discard)
					action = player_strats[player](state, players[player], False)
					card = tarock.choose_card_lead(players[player], action)
					
				else:
					state = tarock.get_state_wrapper(player_id=starting_player,
												player2=second_player,
												player3=third_player,
												current_stack=stack,
												stack_value=sum([tarock.id_to_points[c] for c in stack]), 
												legal_moves=tarock.legal_moves(stack[0], players[player]),
												hand=players[player],
												discard=discard)
					action = player_strats[player](state, players[player], True)
					card = tarock.choose_card_play(stack, tarock.legal_moves(stack[0], players[player]), action)
				tarock.play_card(players[player], card)
				stack.append(card)
				stack_order.append(player)
			else:
				if len(stack) == 0:
					card = player_strats[player](players[player])
				else:
					card = player_strats[player](tarock.legal_moves(stack[0], players[player]))
				tarock.play_card(players[player], card)
				stack.append(card)
				stack_order.append(player)
			
			
		tarock.print_hand(stack)
		print(stack_order)
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


		