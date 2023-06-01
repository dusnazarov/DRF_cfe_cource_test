
# # #  //////////////// DRF Generics ListCreateAPIView    ///////////////////////
# import requests

# endpoint = "http://127.0.0.1:8000/api/products/create/"


# data = {
#     "title":"This field is done now 7"    
       
# }

# get_response = requests.post(endpoint, json=data)
# print(get_response.json())



# #  //////////////// DRF Generics ListCreateAPIView    ///////////////////////
import requests

endpoint = "http://127.0.0.1:8000/api/products/create/"

headers = {'Authorization': 'Bearer 964f4788e4a3cd15bd41daa3ce78514911c3a5cf'}


data = {
    "title":"This field is done now 8"    
       
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())