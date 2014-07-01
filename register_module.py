from bin.network.server_comm import *
from bin.util.authorization import *
from bin.util.constants import *


# SERVER_URL = 'http://remote-light.herokuapp.com/module/%i/' % MODULE_ID
SERVER_URL = 'http://192.168.1.108:5000/module/%i/' % MODULE_ID


##Function for contacting the server and registering the PcDuino
def Register ():
    data = FormRegistrationJSON(AUTH_ID)
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

    data = FormRegistrationJSON(AUTH_ID)
    r = DeleteJSONToServer(data, SERVER_URL)
    print(r.status_code)

Register()
