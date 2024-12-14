from django.urls import path
from . import views


app_name = "blogs"
urlpatterns = [
    path("", views.index, name = "index"),
    path("view", views.PostList.as_view(), name="list"),
]
