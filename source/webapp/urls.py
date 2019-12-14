from django.urls import path
from webapp.views import IndexView, GalleryView, GalleryCreateView, GalleryUpdateView, GalleryDeleteView

app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('gallery/<int:pk>/', GalleryView.as_view(), name='gallery_view'),
    path('gallery/add/', GalleryCreateView.as_view(), name='gallery_create'),
    path('gallery/<int:pk>/edit/', GalleryUpdateView.as_view(), name='gallery_update'),
    path('gallery/<int:pk>/delete/', GalleryDeleteView.as_view(), name='gallery_delete')

]