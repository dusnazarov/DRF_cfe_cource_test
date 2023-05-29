# # 1)  wiews.py 6) ////////////////  Django Rest Framework Model Serializer    ///////////////////////
# from rest_framework import serializers
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):   
      
#     class Meta:
#         model = Product
#         fields = ['id','title','content','price', 'sale_price', 'get_discount']



# 2)  ////////////////  Injest Data with Django Rest Framework Views   ///////////////////////
# from rest_framework import serializers
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     my_discount_1 = serializers.SerializerMethodField(read_only=True)
#     my_discount_2 = serializers.SerializerMethodField(read_only=True)
#     my_content = serializers.SerializerMethodField(read_only=True)
    
#     class Meta:
#         model = Product
#         fields = ['id','title','content','price', 'sale_price','my_discount_1','my_discount_2','my_content' ]
        
#     def get_my_discount_1(self, obj):
#         print(obj.id)
        
#         try:        
#             return obj.get_discount()
#         except:
#             return None 
        

#     def get_my_discount_2(self, obj):
#         print(obj.id)
    
#         try:        
#             return obj.get_discount()
#         except:
#             return None 

#     def get_my_content(self, objs):
#         print(objs.id)
#         return objs.get_content()


# 3)  ////////////////  Injest Data with Django Rest Framework Views   ///////////////////////
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount_1 = serializers.SerializerMethodField(read_only=True)
    my_discount_2 = serializers.SerializerMethodField(read_only=True)
    my_content = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id','title','content','price', 'sale_price','my_discount_1','my_discount_2','my_content' ]
        
    def get_my_discount_1(self, obj):
        # print(obj.id)
        
        try:        
            return obj.get_discount()
        except:
            return None 
        

    def get_my_discount_2(self, obj):
        # print(obj.id)
    
        try:        
            return obj.get_discount()
        except:
            return None 

    def get_my_content(self, objs):
        # print(objs.id)
        return objs.get_content()
      
        
