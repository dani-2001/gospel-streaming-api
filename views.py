from rest_framework import viewsets, permissions
from .models import Video, Comment, Like, Subscription, UserProfile
from .serializers import VideoSerializer, CommentSerializer, LikeSerializer, SubscriptionSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Authentication views (use Django Rest Framework's built-in views)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class AuthView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=400)

# Video management
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        video = self.get_object()
        Like.objects.create(user=request.user, video=video)
        return Response({'status': 'video liked'})

# Comments management
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

# Likes management
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

# Subscriptions management
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

# User profiles management
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

# Search and recommendations
class SearchView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        videos = Video.objects.filter(title__icontains=query)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

# Recommendations (Example Implementation)
class RecommendationView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def recommend(self, request):
        recommended_videos = Video.objects.filter(recommended=True)  # Example filter
        serializer = VideoSerializer(recommended_videos, many=True)
        return Response(serializer.data)