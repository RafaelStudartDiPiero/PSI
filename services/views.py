from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .models import Category, Service


class ServiceDetailView(DetailView):
    queryset = Service.available.all()


class ServiceListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Service.available.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context


class AddServiceView(CreateView):
    model = Service
    template_name = 'service_add.html'
    fields = '__all__'

