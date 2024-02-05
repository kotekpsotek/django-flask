# Here I assing "view functions" from ./views file to url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("d/", views.template),
    path("database/", views.databse_view),
    path("json/", views.json_response, name="json response")
]