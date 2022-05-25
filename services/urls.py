from django.urls import path

from .views import ServiceDetailView, ServiceListView, AddServiceView

app_name = "services"

urlpatterns = [
    path("", ServiceListView.as_view(), name="list"),
    path("add/", AddServiceView.as_view(), name = "add"),
    path("category/<slug:slug>/", ServiceListView.as_view(), name="list_by_category"),
    path("<slug:slug>/", ServiceDetailView.as_view(), name="detail"),

]