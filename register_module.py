from bin.network.server_comm import PostJSONToServer, FormRegistrationJSON
from bin.util.constants import MODULE_ID, AUTH_ID
from bin.util.authorization import SaveModuleAuthorizationID

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

Register()
