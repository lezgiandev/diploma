from rest_framework import serializers
from .models import User
from apps.language.models import Language
from ..language.serializers import LanguageSerializer


class UserSerializer(serializers.ModelSerializer):
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'language')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            language=validated_data['language']
        )
        return user


class LanguageUpdateSerializer(serializers.Serializer):
    language_id = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())


class UserLanguageSerializer(serializers.ModelSerializer):
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('language',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep['language'] or {}