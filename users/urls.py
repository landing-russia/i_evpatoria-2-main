from django.urls import path
from .views import UserProfileView, UpdateProfileView

app_name = 'users'


urlpatterns = [

    path("update-profile/", UpdateProfileView.as_view(), name="update"),
    path('<int:pk>/', UserProfileView.as_view(), name='profile'),
]
