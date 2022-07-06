from django.urls import path

from .views import ProfileDetailView,ProfileListView
app_name = "users"

urlpatterns = [
    path("", ProfileListView.as_view(), name="user_list"),
    path("<int:pk>/profile/", ProfileDetailView.as_view(), name='profile_page'),
]
