from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


# //////////////// DRF Generics RetrieveAPIView   ///////////////////////
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIView.as_view()


#//////////////// DRF Generics ListCreateAPIView   ///////////////////////
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')  or None
        if content is None:
            content = title
        serializer.save(content=content)     
       
product_list_create_view = ProductListCreateAPIView.as_view()


# //////////////// DRF Generics DestroyAPIView   ///////////////////////
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
       super().perform_destroy(instance)  
       
product_delete_view = ProductDestroyAPIView.as_view()


# //////////////// DRF Generics UpdateAPIView   ///////////////////////
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        # print(instance)
        # print(instance.title)
        if not instance.content:
            instance.content = instance.title               
    
product_update_view = ProductUpdateAPIView.as_view()



# ////////////////   DRF Mixin and Generic API View   ///////////////////////
from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
        
    ):
        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'  
    
    def get(self, request, pk=None, *args, **kwargs):
        print(args, kwargs)
        
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
        
product_mixin_view = ProductMixinView.as_view()


# ////////////////   DRF Function Based View   ///////////////////////
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
        
    if request.method == "GET": 
        if pk is not None:
           obj = get_object_or_404(Product, pk=pk)
           data = ProductSerializer(obj, many=False).data
           return Response(data)
             
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
        
    if request.method == 'POST':           
        serializer = ProductSerializer(data=request.data)        
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')  or None
            if content is None:
                content = title
            serializer.save(content=content)            
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)
