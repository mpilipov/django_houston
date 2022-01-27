from django.urls import path
from . import views

urlpatterns = [
    # В зависимости от входных данных вызывается разная функция из view
    path('', views.piedpaper, name='piedpaper'),
]