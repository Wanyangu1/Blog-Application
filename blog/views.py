from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    """
    View to handle creating a new post.
    """
    data = request.data.copy()  
    data['author'] = request.user.id  

    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_list(request):
    """
    View to list all published posts.
    """
    posts = Post.objects.filter(status='published')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, year, month, day, slug):
    """
    View to retrieve details of a specific published post.
    """
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def post_comments(request, post_id):
    """
    View to handle listing and creating comments for a specific post.
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'GET':
        # Retrieve all active comments related to the specified post
        comments = Comment.objects.filter(post=post_id, active=True).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new comment associated with the specified post
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)  # Ensure `post` field is populated with the Post instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

