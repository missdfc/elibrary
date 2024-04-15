from rest_framework import serializers
from .models import *

# serializers is used to serialize objects and expose the endpoints we want to

class GenereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genere
        fields = '__all__'


class FileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileType
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    genere = GenereSerializer()
    file_type = FileTypeSerializer()
    class Meta:
        model = Books
        fields = '__all__'