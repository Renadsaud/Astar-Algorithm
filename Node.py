class node():
    board = None
    parent = None
    goal = None
    h = 0
    level = 0
    f = 0
    def __init__(self, board , parent, goal ,level):
        self.board = board
        self.parent = parent
        self.goal = goal
        self.level = level
        self.f = self.h + self.level
       

    def __lt__(self, other):
        return (self.h < other.h)
    
    def calcH(self):
        h=0
        for i in range(len(self.goal)) :
            for j in range(len(self.goal[i])) :
                if (self.goal[i][j] != self.board[i][j]):
                        h += 1
        self.h = h
        
            