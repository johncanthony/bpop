from random import randint
from uuid import uuid4
from dbInteract import *

class board:

    def __init__(self,sizeX,sizeY):

        #self.board = { 0 : [ 9,9,9],1: [9,9,9],2: [9,9,9]}
        #self.board = { 0:[ 1,2,3,4],1:[5,6,7,8],2:[9,10,11,12],3:[13,14,15,16]}
	#self.size_x = len(self.board.keys())
        #self.size_y = len(self.board[0])
        self.size_x = sizeY
        self.size_y = sizeX
        self.board = self.build_board(self.size_x,self.size_y)
        self.points = 0
        self.max_val= 9
        self.min_val= 1
	self.uid = str(uuid4()) 


    def toJSON(self):
	json = {
		 "size_x" : self.size_x,
		 "size_y" : self.size_y,
		 "board"  : self.board,
		 "points" : self.points,
		 "max_v"  : self.max_val,
		 "min_v"  : self.min_val,
		 "uid"    : self.uid
		}
	return json
	
    @staticmethod
    def fromJSON(b_json):
	b        = board(b_json['size_x'],b_json['size_y'])
	b.board  = {int(k):[int(i) for i in v] for k,v in b_json['board'].items()}
	b.points = int(b_json['points'])
	b.max_v  = int(b_json['max_v'])
	b.min_v  = int(b_json['min_v'])
	b.uid    = b_json['uid']

	return b
   
    def populate(self):
	for y in range (0,self.size_y):
		for x in range (0,self.size_x):
			val = randint(self.min_val,self.max_val)
                        #val = 1
			self.board[y][x]=val

    def build_board(self,x_size,y_size):
        board={}
        for i in range(0,x_size):
            board[i]= [9] * y_size

        return board

    def check_up(self, x,y):
	
        if(y-1) < 0:
		return
 	if(self.board[y-1][x] == self.board[y][x]):
	  self.check_up(x,y-1)	
	  self.board[y-1][x]= -1

    def check_down(self, x,y):
        
        if(y+1) > self.size_y-1:
		return
 	if(self.board[y+1][x] == self.board[y][x]):
	  self.check_down(x,y+1)	
	  self.board[y+1][x]= -1	

    def check_left(self, x,y):
        
        if(x-1) < 0:
		return
 	if(self.board[y][x-1] == self.board[y][x]):
	   self.check_left(x-1,y)	
           self.board[y][x-1]= -1	

    def check_right(self, x,y):
     
        if(x+1) > self.size_x-1:
		return
 	if(self.board[y][x+1] == self.board[y][x]):	
	   self.check_right(x+1,y)
	   self.board[y][x+1]= -1	
	  
    def gravity(self,x,y):
	while(y>=0):
#		print("======")
#		self.bprint()
		if(self.board[y][x]==-1):
			del(self.board[y][x])
			self.board[y].insert(0,randint(self.min_val,self.max_val))
                        self.points+=1
			#continue
		y=y-1
	
    def pop(self,y,x):

#	self.board[y][x] = "X"
	
	self.check_left(x,y)
	self.check_right(x,y)
	self.check_up(x,y)
	self.check_down(x,y)
	self.board[y][x]=-1

	for x in range(0,self.size_x):
		y=self.size_y-1
		self.gravity(x,y)	
   

    def bprint(self):
        format_list = []
        print_string=""
        line = ""
        bottom_index = "X:|"
        for i in range(self.size_x):
            print_string+=str(i)+":"
            for j in range(self.size_y):
                print_string+="|{}".format(self.board[j][i])
            print(print_string)
            print_string=""

        for i in range(self.size_x):
            line+="---"
            bottom_index += str(i)+'|'
        print(line)
        print(bottom_index)
	#for i in range(self.size_x):
        #    print(print_string.format(self.board[0][i],self.board[1][i],self.board[2][i],self.board[3][i]))

    	

    def score_print(self):
        print("== Score: {}==".format(self.points))

if __name__ == "__main__":



    x =-2
    y =-2

    b = board(5,5)
    b.populate()

    print("Bubble Pop")
    print("======")

    import json


    

    while(True):
     while(int(x)!=-1):
        b.bprint()
        b.score_print()

        x = input("Enter X:")
        y = input("Enter Y:")
	if(x!=-1):
            b.pop(x,y)

     id = b.uid

     if(isBoardUnique(b.uid)):
	insert_Board(b.toJSON())
     else:
	drop_Board(b.uid)
	insert_Board(b.toJSON())
	
     #print(export)

     x =  -2
     imp_board = json.loads(retrieve_board(id)[1])
     #imp = json.loads(imp_board)
     b2 = board.fromJSON(imp_board)


