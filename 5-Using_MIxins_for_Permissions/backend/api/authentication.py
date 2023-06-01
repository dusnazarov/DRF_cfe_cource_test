# from rest_framework.authentication import TokenAuthentication as BaseTokenAuth 
from rest_framework.authentication import TokenAuthentication  

class BearTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'