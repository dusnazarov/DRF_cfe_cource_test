# //////// DRF class based View  ////////////
# from django.urls import path
# from .import views 

# urlpatterns = [
#     path('<int:pk>/', views.product_detail_view),
#     path('create/', views.product_list_create_view),   
#     path('list/', views.product_list_create_view),   
#     path('<int:pk>/delete/', views.product_delete_view),
#     path('<int:pk>/update/', views.product_update_view),
# ]


# ////////  DRF Mixin and Generic API View  ////////////
# from django.urls import path
# from .import views 

# urlpatterns = [
#     path('list/', views.product_mixin_view),
#     path('<int:pk>/', views.product_mixin_view),    
#     path('create/', views.product_mixin_view),       
    
# ]


# //////////// DRF function based View  //////////////
from django.urls import path
from .import views 

urlpatterns = [
    path('list/', views.product_alt_view),    
    path('<int:pk>/', views.product_alt_view),
    path('create/', views.product_alt_view),
    
]
