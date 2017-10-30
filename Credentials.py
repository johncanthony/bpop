import yaml
import sys

class Credentials:

    def __init__(self,cred_file='creds.yml'):
	config=self.credential_conf(cred_file)
	self.user = config['user']['name']
	self.password = config['user']['password']
        

    def credential_conf(self,file_url):
	try:
	    creds = yaml.load(open(file_url))
	except IOError as e:
	    ERR_CRED_FILE="Error: Credential File cannot be found, or had insufficient permission"
	    print(ERR_CRED_FILE)
	    sys.exit(1)
	
	try:
	   user_check = creds['user']
	   user_name_check = creds['user']['name']
	   user_pass_check = creds['user']['password']
	except KeyError as e:
	   ERR_YAML_SYNTAX="Error: Credential file syntax malformation"
	   print("Missing field: %s" % (e))
	   print(ERR_YAML_SYNTAX)
	   sys.exit(1)

	return creds


    def get(self):
	return {'user':self.user,'password':self.password}

'''
if __name__=="__main__":
    creds = Credentials("cred.yml")
    print(creds.get())
'''	    

	

