import pickle
import itertools
from qlearning_attributes import *
import random
from play import Game

def is_right_state(state):
	mnozica = set()
	for label, val in state:
		mnozica.add(label)

	return len(mnozica) == len(state)

class QLearningTarock:

	def __init__(self, gamma, alpha, eps):
		self.gamma = gamma #discount factor
		self.alpha = alpha #learning rate
		self.eps = eps #exploration vs exploitation


	#constraints are in the format int*int*list and describe which q table values have to be set to nan because they can't happen according to the rules
	#first int tells us which property we are reffering to
	#second int tells us which value of the property
	#list tells us which actions can't be performed at this value of the property
	def initialize_qtables(self, state_labels1, state_labels2, action_labels1, action_labels2, constraints1=[], constraints2=[]):
		
		#store everything as class labels just in case we need anything
		self.state_labels1 = state_labels1
		self.action_labels1 = action_labels1
		self.constraints1 = constraints1
		
		self.state_labels2 = state_labels2
		self.action_labels2 = action_labels2
		self.constraints2 = constraints2

		###############
		#FIRST Q TABLE#
		###############

		states = dict()
		sz = []
		
		#create all possible values of properties of a state
		for i, property in enumerate(self.state_labels1):
			label, values = property

			for val in values:
				sz.append((i, val))

		#create all combinations of properties
		z = itertools.combinations(sz, len(self.state_labels1))

		#only use the combinations where every property occurs only once
		for x in z:
			if is_right_state(x):
				states[x] = []

		#now we initialize the table taking into consideration the constraints
		self.qtable1 = {key: [0 for action in self.action_labels1] for key in states}

		for property, value, actions in self.constraints1:
			for key in self.qtable1:
				if key[property][1] == value:
					for i in actions:
						self.qtable1[key][i] = None

		"""for key in self.qtable1:
			print(key, self.qtable1[key])"""

		################
		#SECOND Q TABLE#
		################

		states = dict()
		sz = []
		
		#create all possible values of properties of a state
		for i, property in enumerate(self.state_labels2):
			label, values = property

			for val in values:
				sz.append((i, val))

		#create all combinations of properties
		z = itertools.combinations(sz, len(self.state_labels2))

		#only use the combinations where every property occurs only once
		for x in z:
			if is_right_state(x):
				states[x] = []

		#now we initialize the table taking into consideration the constraints
		self.qtable2 = {key: [0 for action in self.action_labels2] for key in states}

		for property, value, actions in self.constraints2:
			for key in self.qtable2:
				if key[property][1] == value:
					for i in actions:
						self.qtable2[key][i] = None

		"""for key in self.qtable2:
			print(key, self.qtable2[key])"""

	def store_qtables(self, filename1, filename2):
		file1 = open(filename1, "wb")
		file2 = open(filename2, "wb")

		pickle.dump(self.qtable1, file1)
		pickle.dump(self.qtable2, file2)

		file1.close()
		file2.close()

	def load_qtables(self, filename1, filename2):
		self.qtable1 = pickle.load(open(filename1, "rb"))
		self.qtable2 = pickle.load(open(filename2, "rb"))
	
	def find_max(self, sez):
		maks = sez[0]
		for x in sez[1:]:
			if x != None:
				if x > maks:
					maks = x 
			else:
				continue

		vsi = []
		for i in range(len(sez)):
			if sez[i] != None:
				if sez[i] == maks:
					vsi.append(i)

		return random.choice(vsi)

	def find_max2(self, sez):
		maks = None
		for i in range(len(sez)):
			item = sez[i]

			if item != None and maks == None:
				maks = item
			if item != None and item > maks:
				maks = item

		#zdej ma maks notr eno stevilko
		vsi = []

		for i in range(len(sez)):
			item = sez[i]

			if item != None and item == maks:
				vsi.append(i)

		return random.choice(vsi)

	def return_action(self, state, legal_moves, is_play):
		
		if is_play:
			moves = self.qtable1[tuple(state)]
			
			if random.random() <= self.eps:
				viable_indeksi = []
				for i in range(len(moves)):
					if moves[i] != None:
						viable_indeksi.append(i)

				return random.choice(viable_indeksi)
			else:
				
				#sez = self.qtable1[tuple(state)]
				#print(sez, "A")
				return self.find_max2(moves)
		else:
			moves = self.qtable2[tuple(state)]
			if random.random() <= self.eps:
				viable_indeksi = []
				for i in range(len(moves)):
					if moves[i] != None:
						viable_indeksi.append(i)

				return random.choice(viable_indeksi)
			else:
				
				#sez = self.qtable2[tuple(state)]
				#print(sez, "A")
				return self.find_max2(moves)
 
		#print(state, "A")
		#print(legal_moves, "B")
		#return legal_moves[0]

	def update_table(self, state, action, reward, newstate, is_play):

		if is_play:
			#Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
			max_new_state = self.find_max2(self.qtable1[tuple(newstate)])
			self.qtable1[tuple(state)][action] = self.qtable1[tuple(state)][action] + self.alpha * (reward + self.gamma*max_new_state - self.qtable1[tuple(state)][action])
		else:
			#max_new_state = self.find_max2(self.qtable2[tuple(newstate)])
			self.qtable2[tuple(state)][action] = self.qtable2[tuple(state)][action] + self.alpha * (reward) #+ self.gamma*max_new_state - self.qtable2[state][action])

if __name__ == "__main__":
	
	#create learning instance
	#Q = QLearningTarock(0.5, 0.1, 0.1)

	
	#initialize qtables, only run if you want to start the learning from scraths, otherwise use load_qtables
	#Q.initialize_qtables(state_labels1, state_labels2, action_labels1, action_labels2, constraints1=constraints1, constraints2=constraints2)
	#Q.store_qtables("q1_1.pickle", "q2_1.pickle")

	#Q.load_qtables("q1_1.pickle", "q2_1.pickle")
	Q = QLearningTarock(0.3,0.1,0.1)
	Q.initialize_qtables(state_labels1, state_labels2, action_labels1, action_labels2, constraints1=constraints1, constraints2=constraints2)
	#print(Q.qtable2)
	#print(Q.qtable1)
	#exit(-1)
	action_function = Q.return_action
	update_function = Q.update_table
	N_epochs = 100000
	counter = 0
	while counter < N_epochs:
		print(f"Take: {counter}, {int((counter/N_epochs)*10000)/100}% done")
		game = Game(action_function, action_function, action_function, update_function)
		a = game.play_game()
		#print(f"Final rewards: {a}")
		counter += 1
	Q.store_qtables("q1_2.pickle", "q2_2.pickle")