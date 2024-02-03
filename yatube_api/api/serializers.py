from rest_framework.serializers import ModelSerializer, SerializerMethodField

from posts.models import Comment, Group, Post


class PostModelSerializer(ModelSerializer):

    author = SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.username

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
            'author',
        )


class GroupModelSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = read_only_fields = (
            'id',
            'title',
            'slug',
            'description',
        )


class CommentModelSerializer(ModelSerializer):

    author = SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.username

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
            'author',
            'post',
            'created',
        )
