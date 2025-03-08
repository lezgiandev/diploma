from rest_framework import serializers
from .models import Category, Word, Translation, FavoriteWord, PartOfSpeech, Collection, WordInCollection


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PartOfSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartOfSpeech
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    part_of_speech = PartOfSpeechSerializer()

    class Meta:
        model = Word
        fields = ('id', 'text', 'category', 'part_of_speech')

class TranslationSerializer(serializers.ModelSerializer):
    word = WordSerializer()
    language = serializers.StringRelatedField()

    class Meta:
        model = Translation
        fields = ('id', 'text', 'audio', 'language', 'word')

class FavoriteWordSerializer(serializers.ModelSerializer):
    translation = TranslationSerializer(read_only=True)

    class Meta:
        model = FavoriteWord
        fields = ('id', 'user', 'translation')
        read_only_fields = ('user', )

class CollectionSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()

    class Meta:
        model = Collection
        fields = ('id', 'name', 'description', 'language', 'is_public')

class WordInCollectionSerializer(serializers.ModelSerializer):
    translation = TranslationSerializer(read_only=True)

    class Meta:
        model = WordInCollection
        fields = ('id', 'collection', 'translation')
        read_only_fields = ('collection',)

class AddWordToCollectionSerializer(serializers.Serializer):
    translation_id = serializers.PrimaryKeyRelatedField(queryset=Translation.objects.all())

    def create(self, validated_data):
        collection = self.context['collection']
        translation = validated_data['translation_id']
        word_in_collection, created = WordInCollection.objects.get_or_create(
            collection=collection,
            translation=translation
        )
        return word_in_collection