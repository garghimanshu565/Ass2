max_capacity = (12,8,5) 
j1 = max_capacity[0]
j2 = max_capacity[1]
j3 = max_capacity[2]
t = {}
result = []

def states(state):
	p = state[0]
	q = state[1]
	r = state[2]

	if(p==6 and q==6):
		result.append(state)
		return True

	if((p,q,r) in t):
		return False

	t[(p,q,r)] = 1
	if(p>0):
		if(p+q<=j2):
			if( states((0,p+q,r)) ):
				result.append(state)
				return True
		else:
			if( states((p-(j2-q), j2, r)) ):
				result.append(state)
				return True
		if(p+r<=j3):
			if( states((0,q,p+r)) ):
				result.append(state)
				return True
		else:
			if( states((p-(j3-r), q, j3)) ):
				result.append(state)
				return True

	if(q>0):
		if(p+q<=j1):
			if( states((p+q, 0, r)) ):
				result.append(state)
				return True
		else:
			if( states((j1, q-(j1-p), r)) ):
				result.append(state)
				return True
		if(q+r<=j3):
			if( states((p, 0, q+r)) ):
				result.append(state)
				return True
		else:
			if( states((p, q-(j3-r), j3)) ):
				result.append(state)
				return True
	if(r>0):
		if(p+r<=j1):
			if( states((p+r, q, 0)) ):
				result.append(state)
				return True
		else:
			if( states((j1, q, r-(j1-p))) ):
				result.append(state)
				return True
		if(q+r<=j2):
			if( states((p, q+r, 0)) ):
				result.append(state)
				return True
		else:
			if( states((p, j2, r-(j2-q))) ):
				result.append(state)
				return True

	return False

initial_state = (12,0,0)
print("Starting work...\n")
states(initial_state)
result.reverse()
for i in result:
	print(i)
print("(6, 0, 0)")
