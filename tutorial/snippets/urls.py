from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# create a router and register our viewset with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# the API URLs are now determined automatically by the routers
urlpatterns = [
    path('', include(router.urls)),
]