"""mydjangoreviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.forms.widgets import Media
# We need to define URLS in our project's urls file and use the include()funtion to point those URLS to our app.
from django.urls import path, include
# By default, Django's development server can not display uploaded media files because of this you must add some code to your project app's urls file to allow the development server to do so.
# This code should be removed for production
# This will require the following modules.
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductList

# we need to define URL in our project's url.py file for our products
urlpatterns = [
    path('', ProductList.as_view(), name='product-home'),
    path('products/', include('products.urls')),
    path('reviews/', include('reviews.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# At the end of the urlpatterns variable, add the static function which references MEDIA_URL and MEDIA_ROOT variable which we will define in the setting.py file latter as arguments.
