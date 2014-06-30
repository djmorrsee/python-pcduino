## @package Module Authorization Code

import os
this_dir = os.path.dirname(__file__)
auth_file_path = os.path.join(this_dir, 'm_auth_id.txt')

## Saves authorizatioin ID during registration
#@param m_auth_id given at reistaration
def SaveModuleAuthorizationID(m_auth_id):
	file = open(auth_file_path, 'w+')
	file.write(m_auth_id)
	file.close()
##Returns the authorization id if there is one
def GetModuleAuthorizationID():
	file = open(auth_file_path, 'r')
	if file:
		return file.readlines()[0]
	else:
		return None
