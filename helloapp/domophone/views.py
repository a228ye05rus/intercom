from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic import DetailView

def index(request):
    product = Product.objects.all()

    return render(request, 'domophone/layout.html', {'prod': product})


class ProductDetail(DetailView):
    model = Product
    template_name ='domophone/ProdDetail.html'
    context_object_name = 'prod'
