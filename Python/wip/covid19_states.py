import requests
import re
import json


r = requests.get('https://covidtracking.com/api/v1/states/current.json')
data = r.json()
print(json.dumps(data, indent=4))
# print(type(data))

# def _url(path):
#     return 'https://covidtracking.com' + path

# def get_data():
#     return requests.get(_url('/api/states'))


# def rd_data():
#     resp = get_data()
#     if resp.status_code != 200:
#         # This means something went wrong.
#         raise ApiError('GET /api/states {}'.format(resp.status_code))

#     total_data = resp.json()
#     #total_data=total_data[0]
#     print(total_data.keys)
#     #return total_data
#     #return json.dumps(parsed, indent=4)

# def get_states():
#     state_data = rd_data()
#     print(state_data)
#     for data in state_data:
#         print(state_data['state'])

# rd_data()
# #get_states()