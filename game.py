from Node import node
from heapq import heapify, heappush, heappop
import copy
class priorityQueue:
     
    
    def __init__(self):
        self.heap = []
 
    # Inserts a new key 'k.f'
    def push(self, k):
        heappush(self.heap, (k.f , k))
 
    # Method to remove minimum element
    # from Priority Queue
    def pop(self):
        return heappop(self.heap)
 
    # Method to know if the Queue is empty
    def empty(self):
        if not self.heap:
            return True
        else:
            return False


class Game:
    # array goal
    goal = [['🟨','🟥'],['🟩','🟦']]
    
    def __init__(self):
        self.play()
    
    def play(self):
        
        #initiate state
        START = [['🟩','🟨'],['🟥','🟦']]
        
        #the fisrt node 
        curr = node(START,None,self.goal,0)
        #the heap with available nodes
        OPEN = priorityQueue()
        OPEN.push(curr)
        
        temp = OPEN.pop()
        self.explore(temp[1],OPEN)
       
        while not OPEN.empty():
            
            temp = OPEN.pop()
            if temp[1].h == 0 :
                self.printpath(temp[1])
                return
            self.explore(temp[1],OPEN)
            


    def printpath(self, curr):
            if curr == None:
                return
            self.printpath(curr.parent)
            printBoard(curr.board) 
            print()       
      
        

    def explore(self,temp , OPEN):
        moves = ["up","down","left","right"]
        for i in moves:
            curr = node(copy.deepcopy(temp.board) ,temp, self.goal ,temp.level+1)
            self.Move(curr,i)
            curr.calcH()
            OPEN.push(curr)
            
            


    def Move(self, curr , move):
        if move == 'up':
            self.swap(0,0,0,1,curr)
        elif move == 'down':
            self.swap(1,0,1,1,curr)
        elif move == 'right':
            self.swap(0,1,1,1,curr)
        elif move == 'left':
            self.swap(0,0,1,0,curr)        
    
    def swap(self,x,y,a,b, curr):
        curr.board[x][y] , curr.board[a][b] = curr.board[a][b] , curr.board[x][y]
        return curr

def printBoard(board):
    	
	for i in range(2):
		for j in range(2):
			print("%s " % (board[i][j]), end = " ")
			
		print()



        
