from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from carts.models import Cart
from .models import Product

# Create your views here.

class ProductFeaturedListView(ListView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-product_list.html"

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured-product_detail.html"
    

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/product_list.html"

    def get_queryset(self, *args, **kwargs):
        request= self.request
    
        return Product.objects.all()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"
        
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug, active = True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.get(slug=slug, active = True)
            instance = qs.first()
        except:
            raise Http404("Something is wrong..")
        return instance

# class ProductDetailView(DetailView):
#     queryset = Product.objects.all()
#     template_name = "products/product_detail.html"
        
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context