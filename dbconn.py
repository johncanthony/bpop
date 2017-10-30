#import psycopg2
from Credentials import *
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.url import URL 


class DBCONN():

    def __init__(self,hostname='192.168.1.75',credentials='cred.yml',db='bubbles',port=49162):
	self.hostname = hostname
	self.cred = Credentials(credentials).get()
	self.db = db
	self.port = port
    
	#Create Connection information
        conn_url = {'drivername':'postgres',
		    'username'  : self.cred['user'],
		    'password'  : self.cred['password'],
		    'host'  : self.hostname,
		    'port'      : self.port,
		    'database'  : self.db
		   } 
	self.conn = create_engine(URL(**conn_url),client_encoding='utf8')
	self.meta = MetaData(bind=self.conn,reflect=True)

    def get_conn(self):
	return self.conn

    def get_meta(self):
	return self.meta   

    def close(self):
	self.conn.close()


    

