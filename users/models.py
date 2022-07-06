from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    def get_absolute_url(self):
        return reverse("users:profile_page", kwargs={"pk": self.id})

    def get_rating_url(self):
        return reverse("users:rating_list", kwargs={"pk": self.id})
