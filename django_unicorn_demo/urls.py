from django.urls import path, include

from unicorn.views import index

urlpatterns = [
    path("", index, name="index"),
    path("unicorn/", include("django_unicorn.urls")),
]
