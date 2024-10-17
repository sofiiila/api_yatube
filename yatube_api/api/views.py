from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import exceptions
from posts.models import Post, Group
from . import serializers


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(PostViewSet, self).perform_destroy(instance)


class CommentViewSet(ModelViewSet):
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        pk_post = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=pk_post)
        return post.comments.all()

    def perform_create(self, serializer):
        pk_post = self.kwargs.get('post_id')
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=pk_post)
        )

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(CommentViewSet, self).perform_destroy(instance)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
