from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skin/', views.skin_form, name='skin_form'),
    path('hair/', views.hair_form, name='hair_form'),
    path('body/', views.body_form, name='body_form'),
    path('health/', views.health_form, name='health_form'),
    path('results/', views.generate_suggestions, name='results'),
]
