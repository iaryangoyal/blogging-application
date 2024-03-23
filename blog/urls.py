from django.urls import path
from .views import BlogAPIView, LikeAPIView, CommentAPIView, BlogingViewAPIView, BlogSearchAPIView,BlogDetailsAPIView

urlpatterns = [
    path('register/', BlogAPIView.as_view()),
    path('blogs/<int:blog_id>/like/', LikeAPIView.as_view()),
    path('comments/create/', CommentAPIView.as_view()),
    path('view/',  BlogingViewAPIView.as_view()),
    path('search/', BlogSearchAPIView.as_view()),
    path('blogs/<int:blog_id>/', BlogDetailsAPIView.as_view())
]