from rest_framework import serializers
from .models import DecisionTree

class DecisionTreeSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = DecisionTree
        fields = ['id', 'title', 'description', 'owner', 'data', 'created_at', 'updated_at']