from django.core.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.serializers import (CommentModelSerializer, GroupModelSerializer,
                             PostModelSerializer)
from posts.models import Comment, Group, Post


class PerformUpdateDestroyMixin:
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(instance)


class PostModelViewSet(PerformUpdateDestroyMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class CommentModelViewSet(PerformUpdateDestroyMixin, ModelViewSet):
    serializer_class = CommentModelSerializer

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post()
        queryset = Comment.objects.filter(post=post)
        return queryset

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(
            post=post,
            author=self.request.user
        )
