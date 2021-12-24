from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.results, name='results'),
    path('ajax/getListBrands', views.getListBrands, name='getListBrands'),
    path('ajax/avradmin', views.avradmin, name='avradmin'),
]
