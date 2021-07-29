from rest_framework import serializers

from employees.models.position import Position as Master


class PositionPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )

class PositionPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )

class PositionPrivateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )

class PositionPrivateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )