# blog/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer, LikeSerializer, CommentSerializer
from user_auth.models import User_login
from user_auth.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Blog, Like, Comment
from django.core.mail import send_mail


class BlogAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        blogs = Blog.objects.all().select_related('like')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog post does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if Like.objects.filter(user=request.user, blog=blog).exists():
            return Response({"error": "You have already liked this blog post"}, status=status.HTTP_400_BAD_REQUEST)

        like = Like(user=request.user, blog=blog)
        like.save()

        return Response({"message": "Like added successfully"}, status=status.HTTP_201_CREATED)

class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogingViewAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BlogSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        search_query = request.query_params.get('q', None)
        if search_query:
            blogs_with_comment = Blog.objects.filter(comment__comment__icontains=search_query).distinct()
            serializer = BlogSerializer(blogs_with_comment, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a search query"}, status=status.HTTP_400_BAD_REQUEST)
        
#update till now

# feature for no of likes and views comments on that perticular blog

class BlogDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
            return Response({"error": "Blog post does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the blog details along with likes and comments
        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)