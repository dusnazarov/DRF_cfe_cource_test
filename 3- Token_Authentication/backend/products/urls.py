# //////// DRF class based View  ////////////
from django.urls import path
from .import views 

urlpatterns = [
    path('<int:pk>/', views.product_detail_view),
    path('create/', views.product_list_create_view),   
    path('list/', views.product_list_create_view),   
    path('<int:pk>/delete/', views.product_delete_view),
    path('<int:pk>/update/', views.product_update_view),
]


