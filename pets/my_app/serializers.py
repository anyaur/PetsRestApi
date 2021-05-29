import uuid

from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    # id = serializers.UUIDField(format="hex_verbose")
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    type = serializers.CharField(max_length=255)
    # photos = serializers.ImageField()
    # photos = serializers.ImageField(upload_to='images/')
    # created_at = serializers.DateTimeField()

    class Meta:
        model = Pet
        fields = ['id', 'name', 'age', 'type', 'photos', 'created_at']

    def create(self, validated_data):
        return Pet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.photos = validated_data.get('title', instance.photos)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance
