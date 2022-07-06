from django.urls import path

from .views import ServiceDetailView, ServiceListView, AddServiceView,UpdateServiceView

app_name = "services"

urlpatterns = [
    path("", ServiceListView.as_view(), name="list"),
    path("add/", AddServiceView.as_view(), name="add"),
    path("category/<slug:slug>/", ServiceListView.as_view(), name="list_by_category"),
    path("<slug:slug>/", ServiceDetailView.as_view(), name="detail"),
    path("update/<slug:slug>/", UpdateServiceView.as_view(), name="update"),
]
