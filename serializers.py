from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Assuming User is imported or defined
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video  # Assuming Video is imported or defined
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  # Assuming Comment is imported or defined
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like  # Assuming Like is imported or defined
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription  # Assuming Subscription is imported or defined
        fields = '__all__'