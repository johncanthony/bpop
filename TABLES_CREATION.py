from dbconn import DBCONN

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()

class User(Base):
	__tablename__ = 'User'
	username      = Column(String())
	uid           = Column(String(), primary_key=True)
	score         = Column(Integer())

	def getJson(self):
		json  = {
			
			 "username" : self.username,
			 "uid"      : self.uid,
			 "score"    : self.score
		 	 }
		return json


class Board(Base):
	__tablename__ = "Board"
	uid           = Column(String(),primary_key=True)
	board         = Column(String())

	def getJSON(self):
		json  = {
		 	 "uid"   : self.uid,
			 "board" : self.board 	
			 }

class Game(Base):
	__tablename__ = "Game"
	uid           = Column(String(),primary_key=True)
	User          = Column(String())
	Board         = Column(String())

	def getJSON(self):
		json  = {
			 "uid"   : self.uid,
			 "user"  : self.user,
			 "board" : self.board
			}
			


if __name__ == "__main__":
	hostname = "192.168.1.75"
	cred = "cred.yml"
	db = "bubbles"
	port = "49162"
	con = DBCONN(hostname,cred,db,port)

	Base.metadata.create_all(con.get_conn())
		
