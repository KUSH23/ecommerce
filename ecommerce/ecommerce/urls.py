

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from accounts.views import login_page, register_page
from .views import home_page, contact_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name = "bootstrap/example.html")),
    path('contact/', contact_page, name="contacts"),
    path('cart/', include('carts.urls', namespace='cart')),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path('', home_page,name="home"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)