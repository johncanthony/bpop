from dbconn import DBCONN
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy import func
import json

from bubble_pop2 import *

def isBoardUnique(id):
	table_name = "Board"
	con = DBCONN()
	table = con.get_meta().tables["Board"]

        select_st = select([table.c.uid]).where(table.c.uid == str(id))
        results = con.get_conn().execute(select_st)
	
	rc=0
	for row in results:
		rc+=1

	if( rc > 0 ):
		return False

	return True


def insert_Board(board):
	b_uid = board['uid']
	b_string = json.dumps(board)
	con = DBCONN()

	
	b_table = con.get_meta().tables['Board']
	ins = b_table.insert().values(uid=b_uid,board=b_string)
	con.get_conn().execute(ins)


def drop_Board(id):
	table_name="Board"
	con = DBCONN()
	b_table = con.get_meta().tables['Board']
	del_st = b_table.delete().where(b_table.c.uid==id)
	res = con.get_conn().execute(del_st) 	


def retrieve_board(id):
	table_name="Board"
	con = DBCONN()
	table = con.get_meta().tables['Board']

	select_st = select([table]).where(table.c.uid == str(id))
	results = con.get_conn().execute(select_st)

	for row in results:
		return row	
	





#id = "2e57893f-2df9-4f14-ae7b-b60829c5360d"
#drop_board(id)

'''
b_json = json.loads(retrieve_board(id)[1])


print(board)
b=0
b=board.fromJSON(b_json)

b.bprint()
'''

'''
if(isBoardUnique(thang['uid'])):
  print("New") 
  insert_Board(thang)	
'''
	


