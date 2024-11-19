import json
import requests


api_url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
api_key = '1c1cffc2a23cbe61a88b8ea749f7a10a'

params = {
    'auth': api_key,
    'topFinGrpNo': '020000',
    'pageNo': '1'
}

response = requests.get(api_url, params=params)
data = response.json()

# print(data['result']['baseList'])
savings = data['result']['baseList']
# print(type(data['result']['baseList']))

new_list = []
for saving in savings:
    new_data = {"model": "savings.savingproducts"}
    new_data['fields'] = saving
    new_list.append(new_data)
print(new_list)

with open('savingproducts.json', 'w', encoding='UTF-8') as m:
    json.dump(new_list, m, ensure_ascii=False, indent=2)