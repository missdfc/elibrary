from rest_framework import serializers
from .models import Books

# serializers is used to serialize objects and expose the endpoints we want to
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'