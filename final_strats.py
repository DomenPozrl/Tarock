from utils import *
import pickle


def get_state_solo_first():
	return 42

if __name__ == "__main__":
	"""
	 herc kralj 0,1,2
	 herc dama
	 ##########herc ostalo
	 karo kralj 0,1,2
	 karo dama
	 ##########karo ostalo
	 pik kralj 0,1,2
	 pik dama
	 ##########pik ostalo
	 kriz kralj 0,1,2
	 kriz dama
	 ##########kriz ostalo
	 nizki taroki mam/nimam
	 srednji taroki mam/nimam
	 visoki taroki mam/nimam
	 player2 skrt herc
	 player2 skrt karo
	 player2 skrt pik
	 player2 skrt kriz
	 player2 taroki
	 player3 skrt herc
	 player3 skrt karo
	 player3 skrt pik
	 player3 skrt kriz
	 player3 taroki
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
		["player2 taroki", [0,1]],
		["player3 skrt herc", [0,1]],
		["player3 skrt karo", [0,1]],
		["player3 skrt pik", [0,1]],
		["player3 skrt kriz", [0,1]],
		["player3 taroki", [0,1]],
	]

	def pomozna(sez):
		aa = []
		for x in [0, 1]:
				xxx = tuple(sez + [x])
				aa.append(xxx)
		return aa
	#create_for_loops(state_solo_first_labels, "novilabeli.py")
	vectors = []
	for herckralj in [0, 1, 2]:
		for hercdama in [0, 1]:
			for karokralj in [0, 1, 2]:
				for karodama in [0, 1]:
					for pikkralj in [0, 1, 2]:
						for pikdama in [0, 1]:
							for krizkralj in [0, 1, 2]:
								for krizdama in [0, 1]:
									for nizkitaroki in [0, 1]:
										for srednjitaroki in [0, 1]:
											for visokitaroki in [0, 1]:
												for player2skrtherc in [0, 1]:
													for player2skrtkaro in [0, 1]:
														for player2skrtpik in [0, 1]:
															for player2skrtkriz in [0, 1]:
																for player2taroki in [0, 1]:
																	for player3skrtherc in [0, 1]:
																		for player3skrtkaro in [0, 1]:
																			for player3skrtpik in [0, 1]:
																				for player3skrtkriz in [0, 1]:
																					#for player3taroki in [0, 1]: too many statically nested blocks
																					#vectors.append([herckralj,hercdama,karokralj,karodama,pikkralj,pikdama,krizkralj,krizdama,nizkitaroki,srednjitaroki,visokitaroki,player2skrtherc,player2skrtkaro,player2skrtpik,player2skrtkriz,player2taroki,player3skrtherc,player3skrtkaro,player3skrtpik,player3skrtkriz])
																					a,b = pomozna([herckralj,hercdama,karokralj,karodama,pikkralj,pikdama,krizkralj,krizdama,nizkitaroki,srednjitaroki,visokitaroki,player2skrtherc,player2skrtkaro,player2skrtpik,player2skrtkriz,player2taroki,player3skrtherc,player3skrtkaro,player3skrtpik,player3skrtkriz])
																					vectors.append(a)
																					vectors.append(b)
	"""final_vectors_solo_first = []
	for i in range(len(vectors)):
		vektor = vectors[i]
		vektor.append(0)

		final_vectors_solo_first.append(vektor)
	
	#final_vectors_solo_first = []
	for i in range(len(vectors)):
		vektor = vectors[i]
		vektor.append(1)

		final_vectors_solo_first.append(vektor)"""

	actions_solo_first_labels = ["strong open", "weak open", "strong tarock", "weak tarock"]

	file = open("q_solo_first.pickle", "wb")
	q_solo_first = {tuple(vector): [0 for i in range(len(actions_solo_first_labels))] for vector in vectors}
	pickle.dump(q_solo_first, file)
	file.close()

	#del state_solo_first_labels
	#del q_solo_first
	#del actions_solo_first_labels
	print("A")
	"""
	#2. stanje ko si drugi solo
	vrednost prve karte 0,2,3,4,5
	a je tarok 0, 1
	skrt barve 0, 1
	a lahko poberem z barvo 0, 1
	a lahko poberem s tarokom 0,1
	nizki taroki
	srednji taroki
	visoki taroki

	mam kralje te barve
	mam damo te barve
	mam cavala te barve
	mam poba te barve
	mam platlc te barve

	player3 skrt barve 0, 1
	player3 taroki 0, 1
	"""	
	"""state_solo_second_labels = [
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
		["zadnji player ima se taroke", [0,1]]
	]

	#create_for_loops(state_solo_second_labels, "novilabeli.py")
	final_vectors_solo_second = []
	for vrednostprvekarte in [0, 2, 3, 4, 5]:
		for ajeprvakartatarok in [0, 1]:
			for asmskrttebarve in [0, 1]:
				for alahkopoberemzbarvo in [0, 1]:
					for alahkopoberemstarokom in [0, 1]:
						for nizkitaroki in [0, 1]:
							for srednjitaroki in [0, 1]:
								for visokitaroki in [0, 1]:
									for mamkraljatebarve in [0, 1]:
										for mamdamotebarve in [0, 1]:
											for mamcavalatebarve in [0, 1]:
												for mampobatebarve in [0, 1]:
													for mamplatlcatebarve in [0, 1]:
														for zadnjiplayerskrtbarve in [0, 1]:
															for zadnjiplayerimasetaroke in [0, 1]:
																final_vectors_solo_second.append([vrednostprvekarte,ajeprvakartatarok,asmskrttebarve,alahkopoberemzbarvo,alahkopoberemstarokom,nizkitaroki,srednjitaroki,visokitaroki,mamkraljatebarve,mamdamotebarve,mamcavalatebarve,mampobatebarve,mamplatlcatebarve,zadnjiplayerskrtbarve,zadnjiplayerimasetaroke])
	
	actions_solo_second_labels = ["take low", "take high", "take all in", "let go"]

	file = open("q_solo_second.pickle", "wb")
	q_solo_second = {tuple(vector): [0 for i in range(len(actions_solo_second_labels))] for vector in final_vectors_solo_second}
	pickle.dump(q_solo_second, file)
	file.close()

	del state_solo_second_labels
	del q_solo_second
	del actions_solo_second_labels
	print("B")"""
	"""
	vrednost prve karte 0,2,3,4,5
	vrednost druge karte 0,2,3,4,5
	a lahko poberem z barvo 0, 1
	a lahko poberem s tarokom 0,1
	mam kralje te barve
	mam damo te barve
	mam cavala te barve
	mam poba te barve
	mam platlc te barve	
	"""					
	state_solo_third_labels = [
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
	create_for_loops(state_solo_third_labels, "novilabeli.py")

	final_vectors_solo_third = []
	for vrednostprvekarte in [0, 2, 3, 4, 5]:
		for vrednostdrugekarte in [0, 2, 3, 4, 5]:
			for ajeprvakartatarok in [0, 1]:
				for asmskrttebarve in [0, 1]:
					for alahkopoberemzbarvo in [0, 1]:
						for alahkopoberemstarokom in [0, 1]:
							for nizkitaroki in [0, 1]:
								for srednjitaroki in [0, 1]:
									for visokitaroki in [0, 1]:
										for mamkraljatebarve in [0, 1]:
											for mamdamotebarve in [0, 1]:
												for mamcavalatebarve in [0, 1]:
													for mampobatebarve in [0, 1]:
														for mamplatlcatebarve in [0, 1]:
															final_vectors_solo_third.append([vrednostprvekarte,vrednostdrugekarte,ajeprvakartatarok,asmskrttebarve,alahkopoberemzbarvo,alahkopoberemstarokom,nizkitaroki,srednjitaroki,visokitaroki,mamkraljatebarve,mamdamotebarve,mamcavalatebarve,mampobatebarve,mamplatlcatebarve])


	actions_solo_third_labels = ["take low", "take high", "take all in", "let go"]

	file = open("q_solo_third.pickle", "wb")
	q_solo_third = {tuple(vector): [0 for i in range(len(actions_solo_third_labels))] for vector in final_vectors_solo_third}
	pickle.dump(q_solo_third, file)
	file.close()

	del state_solo_third_labels
	del q_solo_third
	del actions_solo_third_labels
	print("C")
	###########################################################################################################################################################################################################################################################################################################################
	###########################################################################################################################################################################################################################################################################################################################

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

	#create_for_loops(state_duo_first_labels, "novilabeli.py")

	"""def pomozna(sez):
		aa = []
		for x in [0, 1]:
			for y in [0, 1]:
				xxx = tuple(sez + [x] + [y])
				aa.append(xxx)
		return aa
	
	vectors = []
	actions_duo_first_labels = ["strong open", "weak open", "strong tarock", "weak tarock", "partner open"]
	q_duo_first = dict()
	for herckralj in [0, 1, 2]:
		for hercdama in [0, 1]:
			for karokralj in [0, 1, 2]:
				for karodama in [0, 1]:
					for pikkralj in [0, 1, 2]:
						for pikdama in [0, 1]:
							for krizkralj in [0, 1, 2]:
								for krizdama in [0, 1]:
									for nizkitaroki in [0, 1]:
										for srednjitaroki in [0, 1]:
											for visokitaroki in [0, 1]:
												for player2skrtherc in [0, 1]:
													for player2skrtkaro in [0, 1]:
														for player2skrtpik in [0, 1]:
															for player2skrtkriz in [0, 1]:
																for player2taroki in [0, 1]:
																	for player3skrtherc in [0, 1]:
																		for player3skrtkaro in [0, 1]:
																			for player3skrtpik in [0, 1]:
																				for player3skrtkriz in [0, 1]:
																					#for player3taroki in [0, 1]:
																					#	for ajemojkolegazadnji in [0, 1]:
																					#vectors.append([herckralj,hercdama,karokralj,karodama,pikkralj,pikdama,krizkralj,krizdama,nizkitaroki,srednjitaroki,visokitaroki,player2skrtherc,player2skrtkaro,player2skrtpik,player2skrtkriz,player2taroki,player3skrtherc,player3skrtkaro,player3skrtpik,player3skrtkriz]) #,player3taroki,ajemojkolegazadnji]
																					a, b, c, d = pomozna([herckralj,hercdama,karokralj,karodama,pikkralj,pikdama,krizkralj,krizdama,nizkitaroki,srednjitaroki,visokitaroki,player2skrtherc,player2skrtkaro,player2skrtpik,player2skrtkriz,player2taroki,player3skrtherc,player3skrtkaro,player3skrtpik,player3skrtkriz]) #,player3taroki,ajemojkolegazadnji]
																					q_duo_first[a] = [0 for i in range(len(actions_duo_first_labels))]
																					q_duo_first[b] = [0 for i in range(len(actions_duo_first_labels))]
																					q_duo_first[c] = [0 for i in range(len(actions_duo_first_labels))]
																					q_duo_first[d] = [0 for i in range(len(actions_duo_first_labels))]
	
	"""
	"""final_vectors_duo_first = []
	for i in range(len(vectors)):
		for x in [0, 1]:
			for y in [0, 1]:
				xxx = vectors[i] + [x] + [y]
				final_vectors_duo_first.append(xxx)"""
	#del vectors		
	"""file = open("q_duo_first.pickle", "wb")
	#q_duo_first = {tuple(vector): [0 for i in range(len(actions_duo_first_labels))] for vector in final_vectors_duo_first}
	pickle.dump(q_duo_first, file)
	file.close()
	
	#del state_duo_first_labels
	del q_duo_first
	del actions_duo_first_labels
	print("D")

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
		["a je za mano se kolega", [0, 1]], 

		["zadnji player skrt barve", [0,1]],
		["zadnji player ima se taroke", [0,1]]
	]

	#create_for_loops(state_duo_second_labels, "novilabeli.py")
	final_vectors_duo_second = []
	for vrednostprvekarte in [0, 2, 3, 4, 5]:
		for ajeprvakartatarok in [0, 1]:
			for asmskrttebarve in [0, 1]:
				for alahkopoberemzbarvo in [0, 1]:
					for alahkopoberemstarokom in [0, 1]:
						for nizkitaroki in [0, 1]:
							for srednjitaroki in [0, 1]:
								for visokitaroki in [0, 1]:
									for mamkraljatebarve in [0, 1]:
										for mamdamotebarve in [0, 1]:
											for mamcavalatebarve in [0, 1]:
												for mampobatebarve in [0, 1]:
													for mamplatlcatebarve in [0, 1]:
														for ajezamanosekolega in [0, 1]:
															for zadnjiplayerskrtbarve in [0, 1]:
																for zadnjiplayerimasetaroke in [0, 1]:
																	final_vectors_duo_second.append([vrednostprvekarte,ajeprvakartatarok,asmskrttebarve,alahkopoberemzbarvo,alahkopoberemstarokom,nizkitaroki,srednjitaroki,visokitaroki,mamkraljatebarve,mamdamotebarve,mamcavalatebarve,mampobatebarve,mamplatlcatebarve,ajezamanosekolega,zadnjiplayerskrtbarve,zadnjiplayerimasetaroke])

	actions_duo_second_labels = ["take low", "take high", "take all in", "let go", "add more"]

	file = open("q_duo_second.pickle", "wb")
	q_duo_second = {tuple(vector): [0 for i in range(len(actions_duo_second_labels))] for vector in final_vectors_duo_second}
	pickle.dump(q_duo_second, file)
	file.close()

	print("x")
	del state_duo_second_labels
	del q_duo_second
	del actions_duo_second_labels

	state_duo_third_labels = [
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
		["kolega ze pobere", [0, 1]]
		
	]"""
	#create_for_loops(state_duo_second_labels, "novilabeli.py")
	final_vectors_duo_third = []
	for vrednostprvekarte in [0, 2, 3, 4, 5]:
		for vrednostdrugekarte in [0, 2, 3, 4, 5]:
			for ajeprvakartatarok in [0, 1]:
				for asmskrttebarve in [0, 1]:
					for alahkopoberemzbarvo in [0, 1]:
						for alahkopoberemstarokom in [0, 1]:
							for nizkitaroki in [0, 1]:
								for srednjitaroki in [0, 1]:
									for visokitaroki in [0, 1]:
										for mamkraljatebarve in [0, 1]:
											for mamdamotebarve in [0, 1]:
												for mamcavalatebarve in [0, 1]:
													for mampobatebarve in [0, 1]:
														for mamplatlcatebarve in [0, 1]:
															for kolegazepobere in [0, 1]:
																final_vectors_duo_third.append([vrednostprvekarte,vrednostdrugekarte,ajeprvakartatarok,asmskrttebarve,alahkopoberemzbarvo,alahkopoberemstarokom,nizkitaroki,srednjitaroki,visokitaroki,mamkraljatebarve,mamdamotebarve,mamcavalatebarve,mampobatebarve,mamplatlcatebarve,kolegazepobere])


	actions_duo_third_labels = ["take low", "take high", "take all in", "let go", "add more"]

	

	

	

	

	

	file = open("q_duo_third.pickle", "wb")
	q_duo_third = {tuple(vector): [0 for i in range(len(actions_duo_third_labels))] for vector in final_vectors_duo_third}
	pickle.dump(q_duo_third, file)
	file.close()

	#del state_duo_third_labels
	#del q_duo_third
	#del actions_duo_third_labels
	print("AA")