import requests, json

# Sends the temp, light and moduel id as an HTML post request to url
def PostData (url, temp, light, m_id):
  d = {'temp':temp, 'light':light, 'm_id':m_id}
  r = requests.post(url, data=json.dumps(d))
