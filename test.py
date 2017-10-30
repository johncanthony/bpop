from dbconn import DBCONN
from Credentials import Credentials

hostname = "192.168.1.75"
credential_file = "cred.yml"
credentials = Credentials(credential_file)
db = "bubbles"
port = 49162


conn = DBCONN(hostname,credential_file,db,port)

print(conn.get_meta().tables)

