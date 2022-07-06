from django.urls import path

from .views import AboutPageView, HomePageView, submit_review

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('submit_review/<int:rated_id>/', submit_review, name='submit_review'),
]
