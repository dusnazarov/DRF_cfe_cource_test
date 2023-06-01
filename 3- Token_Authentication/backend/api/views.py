# # 1) ///////////////////////////////////////////
# from django.http import JsonResponse 

# def api_home(request, *args, **kwargs):
#     print(request.body)         #   b'{"query": "Hello world"}'
#     print(request.GET)          #   <QueryDict: {'abs': ['123']}>
#     print(request.POST)         #   <QueryDict: {}>
#     print(type(request.body))   #   <class 'bytes'>
   
#     return JsonResponse({"message":"Hi there, this is  your Django API response!!"})

   
# # 2) //////////////////////////////
# from django.http import JsonResponse
# import json

# def api_home(request, *args, **kwargs):
#     data = {}

#     try:
#         data = json.loads(request.body)
       
#     except:
#         pass   
    
#     print(type(data))          #  <class 'dict'>
#     print(data)                #  {'query': 'Hello world'}
#     return JsonResponse(data)


# # 3) ///////////// Django Model Instance as an API Response //////////////////
# from django.http import JsonResponse
# from products.models import Product


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first() 
        
#     data = {}
#     if model_data:
#         data["id"] = model_data.id
#         data["title"] = model_data.title
#         data["content"] = model_data.content
#         data["price"] = model_data.price
   
#     return JsonResponse(data)


# # 4) /////////////   Django Model Instance to Dictionary ////////////////////////
# from django.http import JsonResponse
# from products.models import Product
# from django.forms.models import model_to_dict


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first() 
    
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id','title','price'])        
   
#     return JsonResponse(data)

# # 5 ) /////////////  Django Rest Framework (DRF) View & Response  ////////////////////////
# from products.models import Product
# from django.forms.models import model_to_dict
# from rest_framework.response import Response
# from rest_framework.decorators import api_view 


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """ 
#     DRF API View
#     """  
#     model_data = Product.objects.all().order_by("?").first() 
    
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id','title', 'price'])
#         print(type(data))    #  <class 'dict'>    
    
#     return Response(data)   

# 6) ///////////// Django Rest Framework Model Serializer ////////////////////////
# from products.models import Product
# from rest_framework.response import Response
# from rest_framework.decorators import api_view 
# from products.serializers import ProductSerializer

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first() 
    
#     data = {}
#     if instance:        
#         data = ProductSerializer(instance).data    
#     return Response(data)

# 7) ///////////// Injest Data with Django Rest Framework Views  ////////////////////////
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)       
        return Response(serializer.data)
    return Response({"invalid":"not good data"}, status=400)