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