from Tarock import Tarock
import numpy as np
import random
#from qlearning import QLearningTarock
from qlearning_attributes import *

class Game:

	def __init__(self, player1func, player2func, player3func, update_function):
		self.tarock = Tarock()
		self.cards = self.tarock.deal_cards()
		self.player1 = self.cards[0]
		self.player2 = self.cards[1]
		self.player3 = self.cards[2]
		self.talon = self.cards[3]
		self.update_function = update_function
		self.players = [self.player1, self.player2, self.player3]
		self.player_strats = [player1func, player2func, player3func]
		self.discard = []

	#players = [0, 1, 2]
	#i = i
	#i+1 = (i + 1) % 3
	#i+2 = (i + 2) % 3
	#returns reward for player1, player2, player3 respectively [rw1, rw2, rw3]
	#lets start just by having each player play for himself
	def play_one_turn(self, starting_player, starting_card, second_player, second_card, third_player, third_card):
		stack = [starting_card, second_card, third_card]
		self.tarock.play_card(self.players[starting_player], starting_card)
		self.tarock.play_card(self.players[second_player], second_card)
		self.tarock.play_card(self.players[third_player], third_card)
		points = sum([self.tarock.id_to_points[starting_card], self.tarock.id_to_points[second_card], self.tarock.id_to_points[third_card]])
		winner = self.tarock.winning_player(stack) - 1 #gotta do the minus 1 because i wasn't consistent when coding
		
		#ce mamo samo platelce al pa samo taroke se steje za eno tocko
		if points == 0:
			points = 1
		
		#vsi dobijo isto kolicino tock samo pri winnerju grejo v plus, pri loserjih pa v minus
		rewards = [-points, -points, -points]

		rewards[winner] *= -1

		return rewards, winner, newState1, newState2, newState3


	def play_game(self):
		
		starting_player = 0
		cummulative_reward = [0,0,0]

		while self.player1 and self.player2 and self.player3:
			second_player = (starting_player + 1) % 3
			third_player = (starting_player + 2) % 3
			
			#how to select cards each player gets his own strategy, that takes as an input current_stack, legal moves, hand, cards played so far
			#it should return which card to play

			#for player in self.players:
			#		self.tarock.print_hand(player)
			#print("--------------------------------------")

			#current stack is empty because this is the first player and noone has played anything yet
			#legal_moves are the entire hand, because nothing was played yet
			#hand is just the hand we currently have
			#and what has been played so far is in the discard pile
			state1 = self.tarock.get_state_wrapper(player_id=starting_player,
																player2=second_player,
																player3=third_player,
																current_stack=[],
																stack_value=0, 
																legal_moves=self.players[starting_player],
																hand=self.players[starting_player],
																discard=self.discard)
			action1 = self.player_strats[starting_player](state1, self.players[starting_player], False)
			#print(f"Action1: {action1}")
			starting_card = self.tarock.choose_card_lead(self.players[starting_player], action1)
			############################################################################################################
			
			state2 = self.tarock.get_state_wrapper(player_id=starting_player,
															player2=second_player,
															player3=third_player,
															current_stack=[starting_card],
															stack_value=self.tarock.id_to_points[starting_card],
															legal_moves=self.tarock.legal_moves(starting_card, self.players[second_player]),
															hand=self.players[second_player],
															discard=self.discard)
			action2 = self.player_strats[second_player](state2, self.tarock.legal_moves(starting_card, self.players[second_player]), True)
			#print(f"Action2: {action2}")
			second_card = self.tarock.choose_card_play([starting_card], self.tarock.legal_moves(starting_card, self.players[second_player]), action2)

			###################################################################################################################
			state3 = self.tarock.get_state_wrapper(player_id=starting_player,
															player2=second_player,
															player3=third_player,
															current_stack=[starting_card, second_card], 
															stack_value=self.tarock.id_to_points[starting_card] + self.tarock.id_to_points[second_card],
															legal_moves=self.tarock.legal_moves(starting_card, self.players[third_player]),
															hand=self.players[third_player],
															discard=self.discard)

			action3 = self.player_strats[third_player](state3, self.tarock.legal_moves(starting_card, self.players[third_player]), True)
			#print(f"Action3: {action3}")
			third_card = self.tarock.choose_card_play([starting_card, second_card], self.tarock.legal_moves(starting_card, self.players[third_player]), action3)


			self.discard.append(((starting_card, starting_player), (second_card, second_player),  (third_card, third_player)))
			############################################################################################
			####################GOTTA DO THE REWARD OUTSIDE THE FUNCTION################################
			############################################################################################
			############################################################################################
			stack = [starting_card, second_card, third_card]
			stack_order = [starting_player, second_player, third_player]

			self.tarock.play_card(self.players[starting_player], starting_card)
			newState1 = self.tarock.get_state_wrapper(player_id=starting_player,
																player2=second_player,
																player3=third_player,
																current_stack=[],
																stack_value=0, 
																legal_moves=self.players[starting_player],
																hand=self.players[starting_player],
																discard=self.discard)
			self.tarock.play_card(self.players[second_player], second_card)
			newState2 = self.tarock.get_state_wrapper(player_id=starting_player,
															player2=second_player,
															player3=third_player,
															current_stack=[starting_card],
															stack_value=self.tarock.id_to_points[starting_card],
															legal_moves=self.tarock.legal_moves(starting_card, self.players[second_player]),
															hand=self.players[second_player],
															discard=self.discard)
			self.tarock.play_card(self.players[third_player], third_card)
			newState3 = self.tarock.get_state_wrapper(player_id=starting_player,
															player2=second_player,
															player3=third_player,
															current_stack=[starting_card, second_card], 
															stack_value=self.tarock.id_to_points[starting_card] + self.tarock.id_to_points[second_card],
															legal_moves=self.tarock.legal_moves(starting_card, self.players[third_player]),
															hand=self.players[third_player],
															discard=self.discard)
			points = sum([self.tarock.id_to_points[starting_card], self.tarock.id_to_points[second_card], self.tarock.id_to_points[third_card]])
			winner = self.tarock.winning_player(stack) - 1 #gotta do the minus 1 because i wasn't consistent when coding
			
			#ce mamo samo platelce al pa samo taroke se steje za eno tocko
			if points == 0:
				points = 1
			
			#vsi dobijo isto kolicino tock samo pri winnerju grejo v plus, pri loserjih pa v minus
			rewards = [-points, -points, -points]

			rewards[winner] *= -1

			#print(starting_player, second_player, third_player)
			#print(rewards)
			cummulative_reward[starting_player] += rewards[0]
			cummulative_reward[second_player] += rewards[1]
			cummulative_reward[third_player] += rewards[2]
			#we update the table (self, state, action, reward, newstate, is_play)
			self.update_function(state1, action1, rewards[0], newState1, False)
			self.update_function(state2, action2, rewards[1], newState2, True)
			self.update_function(state3, action3, rewards[2], newState3, True)





			############################################################################################
			############################################################################################
			############################################################################################
			#reward, winner = self.play_one_turn(starting_player, starting_card, second_player, second_card, third_player, third_card)

			#self.tarock.print_hand([starting_card, second_card, third_card])
			#print(rewards, winner)
			#print("==========================================================================")


			#cummulative_reward = cummulative_reward + np.array(rewards)  to je itak glupo k je vsakic drug player na drugih mestih
			starting_player = stack_order[winner]

		return cummulative_reward


def random_legal_card(state, legal_moves):
	return random.choice(legal_moves)

if __name__ == "__main__":
	
	Q = QLearningTarock(0.3,0.1,0.1)
	Q.initialize_qtables(state_labels1, state_labels2, action_labels1, action_labels2, constraints1=constraints1, constraints2=constraints2)
	#print(Q.qtable2)
	#print(Q.qtable1)
	#exit(-1)
	aaa = Q.return_action
	update_function = Q.update_table
	game = Game(aaa, aaa, aaa, update_function)
	a = game.play_game()
	print(f"Final rewards: {a}")
	



	

