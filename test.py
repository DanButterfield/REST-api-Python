import requests

BASE = "http://127.0.0.1:5000/"
response = requests.patch(BASE + "video/2", {"views = 99", "likes=101"})
print(response)
'''
data = [{"likes": 90, "name": "How to Cook", "views": 2000}, {"likes": 20, "name": "How to Code", "views": 230},
        {"likes": 12340, "name": "How to Clean", "views": 5000}, {"likes": 6, "name": "How to Garden", "views": 4000},
        {"likes": 900, "name": "How to drive", "views": 60}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])  # will give in json format
    print(response.json())

input()
response = requests.patch(BASE + "video/7")
print(response.json())
'''


