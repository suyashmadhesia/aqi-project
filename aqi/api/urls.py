from django.urls import path
from .views import AQIView

urlpatterns =[
    path('aqi', AQIView.as_view(), name='aqi-list'),
]