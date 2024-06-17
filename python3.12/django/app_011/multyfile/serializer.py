from rest_framework import serializers
from multyfile.models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    """Serializer for model FileUpload
    
    Attrs:
        file -> list of files to downloads
    """
    
    file = serializers.ListField(child=serializers.FileField(max_length=100000, 
                                                             allow_empty_file=False, 
                                                             use_url=False))
    class Meta:
        model = FileUpload
        fields = '__all__'
        
    def create(self, validated_data):
        name = validated_data['name']
        file = validated_data.pop('file')
        image_list = []
        for img in file:
            picture = FileUpload.objects.create(file=img, name=name)
            image_url = f'{picture.file.url}'
            image_list.append(image_url)
        return image_list
    
class FileUploadDisplaySerializer(serializers.ModelSerializer):
    """Display visible files serializer"""
    
    class Meta:
        model = FileUpload 
        fields = '__all__'            