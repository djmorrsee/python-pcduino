"""
Package for dealing with the auroazatoin_id required by the server 
"""

import os
this_dir = os.path.dirname(__file__)
auth_file_path = os.path.join(this_dir, 'm_auth_id.txt')

## Saves authorizatioin ID during registration
#@param m_auth_id given at reistaration
def SaveModuleAuthorizationID(m_auth_id):
	"""Saves authorizatioin ID during registration

	:param m_auth_id: given at reistaration
	:type m_auth_id: int 
	
	"""
	file = open(auth_file_path, 'w+')
	file.write(m_auth_id)
	file.close()

def GetModuleAuthorizationID():
	""" Returns the authorization id if there is one
	"""
	file = open(auth_file_path, 'r')
	if file:
		return file.readlines()[0]
	else:
		return None
