from django.urls import path

from .views import ProfileDetailView
app_name = "users"

urlpatterns = [
    path("<int:pk>/profile/", ProfileDetailView.as_view(), name='profile_page'),
]
