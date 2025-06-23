from django.contrib import admin
from django.urls import path 
from converter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.convert_currency,name='currency_converter')
]
