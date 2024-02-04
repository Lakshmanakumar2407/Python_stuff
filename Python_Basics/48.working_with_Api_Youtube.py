import requests, json
from googleapiclient.discovery import build

api_key = 'AIzaSyCh6COSAypNg9y6J5iCX0kcf41Ct2XWdhk'
# params = {
#     'part': 'snippet',
#     'home': True,
#     'maxResults': 10,
#     'key': api_key,
# }


service = build('youtube','v3', developerKey = api_key)
response = service.playlists().list(part = 'contentDetails, snippet', channelId = 'UCCezIgC97PvUuR4_gbFUs5g', maxResults = 25)
response = service.playlists().list(part = 'contentDetails, snippet', id = 'PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU', maxResults = 25)
response = service.playlistItems().list(part = 'contentDetails, snippet', playlistId = 'PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU', maxResults = 125)
# response = service.playlistItems().list_next(response, response.execute())
response = service.videos().list(part = 'contentDetails', id = '-aKFBoZpiqA', maxResults = 25)
output = json.dumps(response.execute(),indent=2)
output1 = response.execute()
s_string = output1['items'][0]['contentDetails']['duration'][2:]
def stringop(some_string):
    n_list =[]
    temp_string = ''
    for char in some_string:
        if char.isalpha():
            n_list.append(int(temp_string))
            temp_string = ''
        else:
            temp_string += char
    return n_list

print(stringop(s_string))

# response = requests.get('https://www.googleapis.com/youtube/v3/activities',params=params)
# print(response.status_code)
