import sys
import numpy as np
class Node:
	def __init__(self, state, parent, action):
		self.state = state
		self.parent = parent
		self.action = action
class stack:
	def __init__(self):
		self.frontier = []

	def add(self, node):
		self.frontier.append(node)

	def contains_state(self, state):
		return any((node.state[0] == state[0]).all() for node in self.frontier)
	
	def empty(self):
		return len(self.frontier) == 0
	
	def remove(self):
		if self.empty():
			raise Exception("Empty Frontier")
		else:
			node = self.frontier[-1]
			self.frontier = self.frontier[:-1]
			return node


class queue(stack):
	def remove(self):
		if self.empty():
			raise Exception("Empty Frontier")
		else:
			node = self.frontier[0]
			self.frontier = self.frontier[1:]
			return node

class puzzle_problem:
	def __init__(self, initial_state, start, goal_state, goal):
		self.initial_state = [initial_state, start]
		self.goal_state = [goal_state, goal] 
		self.solution = None

	def neighbour(self, state):
		mat, (row, column) = state
		ans = []
		
		if row > 0:
			matrix = np.copy(mat)
			matrix[row][column] = matrix[row - 1][column]
			matrix[row - 1][column] = 0
			ans.append(('up', [matrix, (row - 1, column)]))
		if column > 0:
			matrix = np.copy(mat)
			matrix[row][column] = matrix[row][column - 1]
			matrix[row][column - 1] = 0
			ans.append(('left', [matrix, (row, column - 1)]))
		if row < 2:
			matrix = np.copy(mat)
			matrix[row][column] = matrix[row + 1][column]
			matrix[row + 1][column] = 0
			ans.append(('down', [matrix, (row + 1, column)]))
		if column < 2:
			matrix = np.copy(mat)
			matrix[row][column] = matrix[row][column + 1]
			matrix[row][column + 1] = 0
			ans.append(('right', [matrix, (row, column + 1)]))

		return ans

	def print(self):
		solution = self.solution if self.solution is not None else None
		print("Start State:\n", self.initial_state[0], "\n")
		print("Goal State:\n",  self.goal_state[0], "\n")
		print("\nStates Explored: ", self.num_explored, "\n")
		print("Solution:\n ")
		for action, cell in zip(solution[0], solution[1]):
			print("action: ", action, "\n", cell[0], "\n")
		print("Goal Reached!!")

	def does_not_contain_state(self, state):
		for st in self.explored:
			if (st[0] == state[0]).all():
				return False
		return True
	
	def solve(self):
		self.num_explored = 0

		initial_state = Node(state=self.initial_state, parent=None, action=None)
		frontier = queue()
		frontier.add(initial_state)

		self.explored = [] 

		while True:
			if frontier.empty():
				raise Exception("No solution")

			node = frontier.remove()
			self.num_explored += 1

			if (node.state[0] == self.goal_state[0]).all():
				actions = []
				cells = []
				while node.parent is not None:
					actions.append(node.action)
					cells.append(node.state)
					node = node.parent
				actions.reverse()
				cells.reverse()
				self.solution = (actions,  cells)
				return

			self.explored.append(node.state)

			for action, state in self.neighbour(node.state):
				if not frontier.contains_state(state) and self.does_not_contain_state(state):
					child = Node(state=state, parent=node, action=action)
					frontier.add(child)


initial_state = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
goal_state = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])

start = (1, 1)
goal = (1, 0)

l = puzzle_problem(initial_state, start, goal_state, goal)
l.solve()
l.print()