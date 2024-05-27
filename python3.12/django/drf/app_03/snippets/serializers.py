from rest_framework import serializers
from django.contrib.auth.models import User 
from snippets.models import Snippet, LANG_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['url', 'highlight', 'id', 'title', 'code', 'linenos', 'lang', 'style', 'owner']
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User 
        fields = ['url', 'id', 'username', 'snippets']