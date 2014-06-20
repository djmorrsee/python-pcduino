import requests, json

# Sends the temp, light and moduel id as an HTML post request to url
def PostData (url, temp, light, m_id):
  d = {'temp':temp, 'light':light, 'm_id':m_id}
  headers = {'content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(d),headers=headers)
  print r.text
