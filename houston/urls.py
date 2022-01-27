from django.urls import path
from . import views

urlpatterns = [
    # В зависимости от входных данных вызывается разная функция из view
    path('', views.index, name='houston-main'),
    path('page', views.page, name='page'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/add_study', views.add_study, name='add-study')
]