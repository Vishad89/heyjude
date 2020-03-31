import requests
import json

# Update to match your API key
API_KEY = 'y_NbAkKc66ryYTWUXYEu'
#API_KEY = '3c3gRvzx7uGfMYEnWKvF'

# Update to match your chosen parameters
QUERY = ''
TEAM_IDS = []
INCLUDE = []


def list_users():
    url = 'https://api.pagerduty.com/users'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'query': QUERY,
        'team_ids[]': TEAM_IDS,
        'include[]': INCLUDE
    }
    r = requests.get(url, headers=headers, params=payload)
    print('Status Code: {code}'.format(code=r.status_code))
    print(r.json())

if __name__ == '__main__':
    list_users()
