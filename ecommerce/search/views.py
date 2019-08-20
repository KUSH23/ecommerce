from django.views.generic import ListView
from django.shortcuts import render

from products.models import Product
# Create your views here.

class SearchProductView(ListView):
    # queryset = Product.objects.all()
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request= self.request
        query = request.GET.get('q')
        print(query)
        if query is not None:
            return Product.objects.search(query)
        else:
            return Product.objects.none()