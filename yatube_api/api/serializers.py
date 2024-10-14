from rest_framework import serializers
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    "Сериализатор для модели Post"
    author = serializers.StringRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class GroupSerializer(serializers.ModelSerializer):
    "Сериализатор для модели Group"
    class Meta:
        model = Group
        fields = ('pk', 'title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):
    "Сериализатор для модели Comment"
    author = serializers.StringRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
)

    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')

