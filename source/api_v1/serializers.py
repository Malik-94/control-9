from rest_framework import serializers
from webapp.models import Gallery, Comments



class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'text', 'images', 'author', 'created_at')


class GallerySerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ('id', 'images', 'signature', 'created_at', 'laike', 'author', 'comments')

