## @package Module Authorization Code

## Saves authorizatioin ID during registration
#@param m_auth_id given at reistaration
def SaveModuleAuthorizationID(m_auth_id):
	file = open('bin/util/m_auth_id.txt', 'w+')
	file.write(m_auth_id)
	file.close()
##Returns the authorization id if there is one
def GetModuleAuthorizationID():
	file = open('bin/util/m_auth_id.txt', 'r')
	if file:
		return file.readlines()[0]
	else:
		return None



# auth_ids = []
#
# def BuildAuthIDs():
# 	auth_file = open('auth_file.txt', 'r')
#
# 	auth_ids = []
# 	for _id in auth_file.readlines():
# 		auth_ids.append()
#
# 	auth_file.close()
#
# def VerifyAuthData(data):
# 	return data.keys() == ["auth_id"]
#
# def VerifyModuleData(data):
# 	return data.keys() == ["module_auth_id", "module_id", "reading"]
#
# def AuthorizeAuthData(data):
# 	return data["auth_id"] in auth_ids
#
# BuildAuthIDs()
