def create_for_loops(states, filename):

	s = ""
	tab_counter = 1
	vector = "["
	for state, value in states:
		s += f"for {state.replace(' ', '')} in {value}:\n"
		vector += state.replace(' ', '') + ","
		for i in range(tab_counter):	
			s += "\t"
		tab_counter += 1

	vector = vector[:-1]
	vector += "]"
	
	#for i in range(tab_counter):
	#	s += "\t"
	s+= vector
	
	file = open(filename, "w")
	file.write(s)
	file.close()

