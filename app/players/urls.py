from django.urls import path, include

from rest_framework.routers import DefaultRouter

from players import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'players'

urlpatterns = [
    path('', include(router.urls))
]
