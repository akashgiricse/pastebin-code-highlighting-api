from rest_framework.schemas import get_schema_view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(title='Pastebin API')
swagger_schema_view = get_swagger_view(title='Pastebin API')


# create a router and register our viewset with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# the API URLs are now determined automatically by the routers
urlpatterns = [
    path('schema/', schema_view),
    path('swagger-docs', swagger_schema_view),
    path('', include(router.urls)),

]