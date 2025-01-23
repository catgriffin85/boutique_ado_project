from django.urls import path
from .import views


from django.urls import path
from .views import all_products

urlpatterns = [
    path('', all_products, name='all_products'),
]
