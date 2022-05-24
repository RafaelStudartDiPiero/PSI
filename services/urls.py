from django.urls import path

from .views import ServiceDetailView, ServiceListView

app_name = "services"

urlpatterns = [
    path("", ServiceListView.as_view(), name="list"),
    path("<slug:slug>/", ServiceDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ServiceListView.as_view(), name="list_by_category"),
]