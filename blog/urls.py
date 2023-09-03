from rest_framework.routers import SimpleRouter

from . import views

app_name = "blog"

router = SimpleRouter()
router.register("users", views.UserViewSetApi, basename="users")
router.register("", views.PostViewSetApi, basename="posts")

urlpatterns = router.urls
