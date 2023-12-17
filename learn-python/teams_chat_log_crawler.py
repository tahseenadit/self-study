import requests
import json
import pandas as pd

def get_teams_user_messages(chat_id, message_id, access_token):
  headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
  }
  url = 'https://graph.microsoft.com/v1.0/chats/{}/messages/{}'.format(chat_id, message_id)
  print(url)
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception('Error getting Teams user messages: {}'.format(response.status_code))

def create_chat_log(user_email, message_id, access_token):
  messages = get_teams_user_messages(user_email, message_id, access_token)
  chat_logs = []

  for message in messages['value']: 
    speaker = message['id']
    chat_logs.append({'speaker': speaker})

  df = pd.DataFrame(chat_logs)
  df.to_csv('chat_log.csv', index=False)

if __name__ == '__main__':

    tenant_id = '30f52344-4663-4c2e-bab3-61bf24ebbed8'
    client_id = '5d6416fd-10b2-4c2f-8c7d-dde71737705b'
    client_secret = 'TZH8Q~~rd.N.ROr~FlW94fbpWKxjp.evQkd7Da.k'
    authorization_code = 'YOUR_AUTHORIZATION_CODE'

    data = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'client_id': client_id,
        'client_secret': client_secret
    }

    url = 'https://login.microsoftonline.com/{}/oauth2/v2.0/token'.format(tenant_id)

    response = requests.post(url, data=data)

    print(response)

    chat_id = '19:5cc35900-ed84-4288-88f5-3fa94a843402_fb270b8b-32f9-4743-93f6-53760bcd948c@unq.gbl.spaces'
    message_id = '1700130969215'
    access_token = 'TZH8Q~~rd.N.ROr~FlW94fbpWKxjp.evQkd7Da.k'

    create_chat_log(chat_id, message_id, access_token)

  #https://teams.microsoft.com/l/message/19:5cc35900-ed84-4288-88f5-3fa94a843402_fb270b8b-32f9-4743-93f6-53760bcd948c@unq.gbl.spaces/1700130969215?context=%7B%22contextType%22%3A%22chat%22%7D