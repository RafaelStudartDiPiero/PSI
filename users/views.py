from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import User
from services.models import Service, ReviewRating


class ProfileDetailView(DetailView):
    model = User
    template_name = 'users/user.html'

    def get_context_data(self, **kwargs):
        users = User.objects.all()
        context = super(ProfileDetailView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(User, id=self.kwargs['pk'])

        context["page_user"] = page_user

        return context


class ProfileListView(ListView):
    category = None
    paginate_by = 12

    def get_queryset(self):
        queryset = User.objects.all()

        return queryset

class RatingListView(ListView):
    category = None
    paginate_by = 12
    template_name = 'users/rating_list.html'

    def get_queryset(self):
        queryset = ReviewRating.objects.all()

        rated_id = self.kwargs.get("rated.id")
        if rated_id:
            self.rated = get_object_or_404(User, id=rated_id)
            queryset = queryset.filter(rated=self.rated)

        return queryset
