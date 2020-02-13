from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import home, about, contact, bakers

urlpatterns = [
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('bakers/', bakers, name="bakers"),
    path('', home, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('checkout/', include('checkout.urls'))
]
