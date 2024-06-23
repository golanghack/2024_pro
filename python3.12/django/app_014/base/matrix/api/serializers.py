from rest_framework import serializers
from matrix.models import Subject, Matrix, Block, Content


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['order', 'title', 'description']


class MatrixSerializer(serializers.ModelSerializer):
    modules = BlockSerializer(many=True, read_only=True)

    class Meta:
        model = Matrix
        fields = ['id', 'subject', 'title', 'slug', 'overview',
                  'created', 'owner', 'block']


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'item']


class BlockWithContentsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)

    class Meta:
        model = Block
        fields = ['order', 'title', 'description', 'contents']


class MatrixWithContentsSerializer(serializers.ModelSerializer):
    modules = BlockWithContentsSerializer(many=True)

    class Meta:
        model = Matrix
        fields = ['id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner', 'block']
