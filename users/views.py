from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import User
from services.models import Service, ReviewRating


class ProfileDetailView(DetailView):
    model = User
    template_name = 'users/user.html'
    reviews = None

    def get_context_data(self, **kwargs):
        users = User.objects.all()
        context = super(ProfileDetailView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(User, id=self.kwargs['pk'])

        context["page_user"] = page_user
        context["reviews"] = ReviewRating.objects.filter(rated_id=page_user.id, status=True)


        return context




class ProfileListView(ListView):
    category = None
    paginate_by = 12

    def get_queryset(self):
        queryset = User.objects.all()

        return queryset

