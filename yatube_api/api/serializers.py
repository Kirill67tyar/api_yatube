from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
)

from posts.models import Comment, Group, Post


class PostModelSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'author',
            'image',
            'group',
            'pub_date',
        )
        read_only_fields = (
            'id',
            'image',
            'pub_date',
        )


class GroupModelSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )


class CommentModelSerializer(ModelSerializer):

    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created',
        )
        read_only_fields = (
            'id',
            'post',
            'created',
        )
