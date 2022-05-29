from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('ProdDetail/<int:pk>', views.ProductDetail.as_view(), name='prod_detail'),
]