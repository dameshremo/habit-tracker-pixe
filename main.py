import requests
from datetime import datetime

TOKEN = "#######Replae with your Token from pixe########" 
USERNAME = "test"
GRAPHID = "test7"

endpoint = "https://pixe.la/v1/users"
user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
############## This is used to Create a Habit graph. Once this is created, it is better to comment these lines#######
# graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
#
# graph_param = {
#     "id": "damesh7",
#     "name": "Gym",
#     "unit": "commit",
#     "type": "int",
#     "color": "sora"
# }
#
# graph_headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_param, headers=graph_headers)
# print(response)
##############################This is used to Post your habit in the grapgh like commit or km you ran in your Treadmil#####
# today = datetime.now()
#
# print(today.strftime("%Y%m%d"))
#
# graph_post_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}"
#
# graph_param = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "2",
# }
#
# graph_headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_post_endpoint, json=graph_param, headers=graph_headers)
# print(response)
#############This is used to update the excisting details that you had added in the graph using PUT method############
today = datetime.now()

today_graph_update = today.strftime("%Y%m%d")

graph_put_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{today_graph_update}"

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

graph_param = {
    "quantity": "1"
}

response = requests.put(url=graph_put_endpoint, json=graph_param, headers=graph_headers)
print(response)

#############This is used to delete the excisting details that you had added in the graph using PUT method############
today = datetime.now()

today_graph_update = today.strftime("%Y%m%d")

graph_put_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{today_graph_update}"

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(url=graph_put_endpoint, headers=graph_headers)
print(response)
