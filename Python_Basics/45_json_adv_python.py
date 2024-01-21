import json, os

os.chdir('Python\\Python_Basics')

with open('45.1_workspace.json') as f_json:
    # str1 = f_json.read() # if strings are used then loads() should be used
    data = json.load(f_json)
    # print(json.dumps(data, indent=2))
    print(data['main']['children'][0]['children'][0]['state']['type'])
    print(data['main']['children'][0]['children'][0]['state']['state']['file'])
    dummy_dict = dict()
    i = 0
    for v in data['main']['children'][0]['children']:
        i+=1
        dummy_dict[f'id-{i}'] = [v['id'], v['state']['type'], v['state']['state']['file']]

print(dummy_dict)
with open('45.2_writing_json.json','w') as json_write:
    json.dump(dummy_dict,json_write, indent=2)