from django.urls import path
from .views import *

app_name = 'excursions'

urlpatterns = [
    path('', HomeExcursions.as_view(), name='home'),
    path('<slug:slug>/', ExcursionDetail.as_view(), name='excursion-detail'),
]
