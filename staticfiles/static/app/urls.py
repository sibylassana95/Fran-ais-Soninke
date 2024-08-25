from django.urls import path

from . import views

urlpatterns = [
    path('', views.traduction, name='traduction'),
    path('about/', views.about, name='about'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('auto/', views.traductionauto, name='traductionauto'),
    path('contribution',views.contribution, name='contribution'),
]
