from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import User


class ProfileDetailView(DetailView):
    model = User
    template_name = 'users/user.html'

    def get_context_data(self, **kwargs):
        users = User.objects.all()
        context = super(ProfileDetailView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(User, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context
