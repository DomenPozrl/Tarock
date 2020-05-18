from utils import *
from Tarock import Tarock

state_labels1 = [("vrednost igranih kart", [1,2,3]), #1 = runing sum 1, 2 = running sum <= 3, 3 = running sum > 3
					("skrt igrane karte", [0,1]), 
					("lahko poberes igrane karte", [0,1]),
					("player2 skrt igrane karte", [0,1]),
					("player3 skrt igrane karte", [0,1]),
					("imam se tarokov", [0,1]),
					("player2 nima vec tarokov", [0,1]),
					("player3 nima vec tarokov", [0,1])]

action_labels1 = ["spustis", "poberes min", "poberes mid", "poberes max"]

constraints1 = [(2, 0, [1,2,3])]

state_labels2 = [("imas kralja", [0,1]), 
				("imas damo", [0,1]),
				("imas pob/caval", [0,1]),
				("imas platlca", [0,1]),
				("imam se tarokov", [0,1]),
				("player2 nima vec tarokov", [0,1]),
				("player3 nima vec tarokov", [0,1])]

action_labels2 = ["igras platlca", "igras pob/caval", "igras damo", "igras kralja", "igras tarok"]

constraints2 = [(0, 0, [3]),
				(1, 0, [2]),
				(2, 0, [1]),
				(3, 0, [0]),
				(4, 0, [4])]



new_states = [("herc kralj", [0,1,2]),
			  ("herc dama", [0,1,2]),
			  ("kara kralj", [0,1,2]),
			  ("kara dama", [0,1,2]),
			  ("pik kralj", [0,1,2]),
			  ("pik dama", [0,1,2]),
			  ("kriz kralj", [0,1,2]),
			  ("kriz dama", [0,1,2]),
			  ("mega taroka", [0,1,2,3,4,5]),
			  ("pagat", [0,1,2]),
			  ("player2 brez tarokov", [0, 1]),
			  ("player3 brez tarokov", [0, 1]),
			  ("vrednost stacka", [0,1,2])]

#create_for_loops(new_states, "testiram.py")

states = []

for herckralj in [0, 1, 2]:
	for hercdama in [0, 1, 2]:
		for karakralj in [0, 1, 2]:
			for karadama in [0, 1, 2]:
				for pikkralj in [0, 1, 2]:
					for pikdama in [0, 1, 2]:
						for krizkralj in [0, 1, 2]:
							for krizdama in [0, 1, 2]:
								for megataroka in [0, 1, 2, 3, 4, 5]:
									for pagat in [0, 1, 2]:
										for player2breztarokov in [0, 1]:
											for player3breztarokov in [0, 1]:
												for vrednoststacka in [0, 1, 2]:
													states.append([herckralj,hercdama,karakralj,karadama,pikkralj,pikdama,krizkralj,krizdama,megataroka,pagat,player2breztarokov,player3breztarokov,vrednoststacka])

t = Tarock()

actions = list(t.id_to_cards.keys())


