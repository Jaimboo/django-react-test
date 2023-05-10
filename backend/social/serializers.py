from rest_framework import serializers
from social.models import Post, User

class PostSerializer(serializers.ModelSerializer):
    prova = serializers.PrimaryKeyRelatedField(
        default = serializers.CurrentUserDefault(),
        queryset = User.objects.all(),
    )
    
    class Meta:
        model = Post
        fields = ('id', 'prova', 'content', 'created')