from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='trybloghome'),
    path('about/', views.about, name='tryblogabout')
]
