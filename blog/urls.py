from django.urls import path

from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.PostListApi.as_view(), name="post_list"),
    path("<int:pk>/", views.PostDetailApi.as_view(), name="post_detail"),
]
