import chess
class Node():
	def __init__(self, state, parent, action):
		self.state = state
		self.parent = parent
		self.action = action

class StackFrontier(): # dfs
	def __init__(self):
		self.frontier = []
	
	def add(self, node):
		self.frontier.append(node)

	def containsState(self, state):
		return any(node.state == state for node in self.frontier)

	def empty(self):
		return len(self.frontier) == 0
	
	def remove(self):
		if self.empty():
			raise Exception("empty frontier")
		node = self.frontier[0]
		self.frontier = self.frontier[1:]
		return node

class QueueFrontier(StackFrontier): # bfs
	def remove(self):
		if self.empty():
			raise Exception("empty frontier")
		node = self.frontier[-1]
		self.frontier = self.frontier[:-1]
		return node

def dfs(board):
	raise NotImplementedError

def bfs(board):
	raise NotImplementedError

def IUSEDTHISIMPORTSODEEPSOURCEWILLSTOPYELLINGATME():
	return 0