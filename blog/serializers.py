from rest_framework import serializers
from .models import Blog, Like, Comment


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    featured_comment = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'likes_count', 'comments_count', 'featured_comment')

    def get_likes_count(self, obj):
        return str(obj.like_set.count()) + "likes"

    def get_comments_count(self, obj):
        return obj.comment_set.count()

    def get_featured_comment(self, obj):
        # Get one of the comments associated with this blog (you can modify this logic as needed)
        featured_comment = obj.comment_set.first()
        if featured_comment:
            return CommentSerializer(featured_comment).data
        else:
            return None