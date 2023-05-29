# 1) 2) 3) 4), 5), 6) ////////////////////////////////////////////////////
# import requests

# endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint, params={'abs':123}, json={'query':'Hello world'})
# # get_response = requests.get(endpoint)

# print(get_response.json())

# 7) ////////////////////////////////////////////////////
import requests
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title":"Hello world"})
print(get_response.json())






