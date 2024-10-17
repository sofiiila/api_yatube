from rest_framework import serializers
from posts.models import Post, Comment, Group


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(

        read_only=True,

        default=serializers.CurrentUserDefault()

    )

    class Meta:
        model = Post

        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group

        fields = ('pk', 'title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(

        read_only=True,

        default=serializers.CurrentUserDefault()

    )

    post = serializers.PrimaryKeyRelatedField(

        read_only=True,

    )

    class Meta:
        model = Comment

        fields = ('id', 'author', 'post', 'text', 'created')


