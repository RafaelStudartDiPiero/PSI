from django.urls import path

from .views import ProfileDetailView,ProfileListView, RatingListView
app_name = "users"

urlpatterns = [
    path("", ProfileListView.as_view(), name="user_list"),
    path("<int:pk>/profile/", ProfileDetailView.as_view(), name='profile_page'),
    path("<int:pk>/rating/", RatingListView.as_view(), name='rating_list'),
]
