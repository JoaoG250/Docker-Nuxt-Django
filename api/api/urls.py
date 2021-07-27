from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework import routers

from core import views as core_views

router = routers.DefaultRouter()
router.register(r"todos", core_views.TodoViewSet, "todo")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
