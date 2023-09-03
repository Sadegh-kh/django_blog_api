from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.PostListApi.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetailApi.as_view(), name="post_detail"),
    path("users/", views.UserListApi.as_view(), name="user_list"),
    path("users/<int:pk>", views.UserDetailApi.as_view(), name="user_detail"),
]
