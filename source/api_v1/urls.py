from django.urls import include, path
from rest_framework import routers
from api_v1 import views

router = routers.DefaultRouter()
router.register(r'Gallery', views.GalleryViewSet)
router.register(r'Comments', views.CommentsViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
]