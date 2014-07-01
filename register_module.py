"""
This file contains functions for registering the pcduino and for removing 
it from the server. 

This should only be done once
"""
from bin.network.server_comm import *
from bin.util.authorization import *
from bin.util.constants import MODULE_ID
SERVER_URL = 'http://remote-light.herokuapp.com/module/%i/' % MODULE_ID

##Function for contacting the server and registering the PcDuino
def Register ():
    """ This function lets the server know that there is a new module
    if the MOLUDULE_ID in constants.py is unique the server will return an
    authoraztion key that will be needed for any later api requests made by the 
    pcduino. This key will be saved in a text file by this function. If the MODULE_ID 
    is already in use the bad reqistraion staus code wil be printed 
        
    """
    data = None
    r = PostJSONToServer(data, SERVER_URL)
    if r.status_code == 200:
        if r.text != 'Bad Module ID':
            SaveModuleAuthorizationID(r.text)
            print('Registered')
        else:
            print (r.text)
    else:
        print('Not Registered')
        print(r.text)
##Function for removoving  the pCduino from the server
def UnRegister():
    """
    Sends an API requests to the server to remove all of data for this module 
    from the database.
        
    This should only be called if the module will be disconnected.
    
    """
    
    data = FormRegistrationJSON(AUTH_ID)
    r = DeleteJSONToServer(data, SERVER_URL)
    print(r.status_code)

Register()
