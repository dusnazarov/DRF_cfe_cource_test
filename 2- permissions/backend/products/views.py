from rest_framework import generics, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission


# //////////////// DRF Generics RetrieveAPIView   ///////////////////////
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
    
    
product_detail_view = ProductDetailAPIView.as_view()


#//////////////// DRF Generics ListCreateAPIView   ///////////////////////
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [IsStaffEditorPermission]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
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






