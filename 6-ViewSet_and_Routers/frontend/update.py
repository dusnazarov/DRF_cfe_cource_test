# ////////////////   DRF Generics UpdateAPIView   ///////////////////////
import requests

endpoint = "http://127.0.0.1:8000/api/products/6/update/"

data = {
    "title":"Hello world my old friend 1",
    "price":129.00
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
