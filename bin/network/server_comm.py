""" This file contains wrapper functions for api requests"""
import requests, json


def GetDataFromServer(url):
    """ A GET request
    
    :param url: the url for desired api call
    :type url: string
    """
    r = requests.get(url)
    return r

def PostJSONToServer(json_data, url):
    """POST request
   
    Should be used for posting sensor reading data
    
    :param json_data: data to be sent
    :type json_data: JSON
    
    :param url: the url for desired api call
    :type url: string
    
    """
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(json_data),headers=headers)
    return r
def DeleteJSONToServer(json_data, url):
    
    """
    DELETE request
    Should be used for posting sensor reading data
    
    :param json_data: data to be sent
    :type json_data: JSON
    
    :param url: the url for desired api call
    :type url: string
    """
    headers = {'content-type': 'application/json'}
    r = requests.delete(url, data=json.dumps(json_data),headers=headers)
    return r

def FormReadingJSON(m_id, m_auth_id, temp, light):
    """Function for turning data into JSON format
    
    :param m_id: the modules id
    :type m_id: int 
    
    :param m_auth_id: the module's API auotharazation key 
    :type m_auth_id: int 
    
    :param temp: the temperature pin readins
    :type temp: int 
    
    :param light: the light pin reading
    :type light: int 
    
    """
    data = {}
    data.update({'module_id':m_id})
    data.update({'module_auth_id':m_auth_id})
    reading = {'temperature':temp, 'light':light}
    data.update({'reading':reading})
    return data
## Used to form registration data into JSON
def FormRegistrationJSON(auth_id):
    """For delete request only
    
    :param m_auth_id: the module's API auotharazation key 
    :type m_auth_id: int 
    """
    
    data = { "auth_id" : auth_id }
    return data
