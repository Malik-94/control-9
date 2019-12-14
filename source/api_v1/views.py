from rest_framework import viewsets
from webapp.models import Gallery, Comments
from api_v1.serializers import GallerySerializer, CommentsSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer



class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer