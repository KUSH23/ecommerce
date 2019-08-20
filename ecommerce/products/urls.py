from django.urls import path, re_path
from .views import ProductListView, ProductDetailSlugView, ProductFeaturedListView, ProductFeaturedDetailView

app_name = 'products'
urlpatterns = [
    path('featured/', ProductFeaturedListView.as_view()),
    re_path(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    path('', ProductListView.as_view(), name='list'),
    # re_path(r'^(?P<pk>\d+)/$', ProductDetailView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),    
]


