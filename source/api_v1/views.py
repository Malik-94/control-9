from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from webapp.models import Gallery, Comments
from api_v1.serializers import GallerySerializer, CommentsSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


    @action(methods=['post'], detail=True)
    def Gallery_up(self, request, pk=None):
        Gallery = self.get_object()
        Gallery.laike += 1
        Gallery.save()
        return Response({'id': Gallery.pk, 'rating': Gallery.laike})


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


    @action(methods=['post'], detail=True)
    def Gallery_up(self, request, pk=None):
        Gallery = self.get_object()
        Gallery.laike -= 1
        Gallery.save()
        return Response({'id': Gallery.pk, 'rating': Gallery.laike})

