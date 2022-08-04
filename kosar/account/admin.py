from django.contrib import admin
from .models import Profile

admin.site.register(Profile)


def ready(self):
    import users.signals