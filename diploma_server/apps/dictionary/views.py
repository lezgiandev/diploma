from rest_framework import viewsets, filters, serializers, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Translation, FavoriteWord, Collection, WordInCollection
from .serializers import TranslationSerializer, FavoriteWordSerializer, CollectionSerializer, \
    AddWordToCollectionSerializer, WordInCollectionSerializer
from apps.user.models import User


class DictionaryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TranslationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['word__category', 'word__part_of_speech']
    search_fields = ['text', 'word__text']

    def get_queryset(self):
        if isinstance(self.request.user, User) and hasattr(self.request.user, 'language'):
            return Translation.objects.filter(language=self.request.user.language)
        return Translation.objects.none()


class FavoriteWordViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteWordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return FavoriteWord.objects.filter(
                user=self.request.user,
                translation__language=self.request.user.language
            )
        return FavoriteWord.objects.none()

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            translation_id = serializer.validated_data['translation'].id
            if FavoriteWord.objects.filter(user=self.request.user, translation_id=translation_id).exists():
                raise serializers.ValidationError("Это слово уже в избранном!")
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError("Пользователь не авторизован!")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"detail": "У вас нет прав на удаление этого объекта."}, status=403)
        self.perform_destroy(instance)
        return Response(status=204)

    @action(detail=False, methods=['get'], url_path='check-favorite')
    def check_favorite(self, request):
        translation_id = request.query_params.get('translation_id')
        if not translation_id:
            return Response({"detail": "Необходимо указать translation_id."}, status=400)

        is_favorite = FavoriteWord.objects.filter(
            user=request.user,
            translation_id=translation_id
        ).exists()

        return Response({"is_favorite": is_favorite})


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if isinstance(self.request.user, User) and hasattr(self.request.user, 'language'):
            return Collection.objects.filter(user=self.request.user, language=self.request.user.language)
        return Collection.objects.none()

    @action(detail=False, methods=['get'], url_path='public-collections')
    def public_collections(self, request):
        public_collections = Collection.objects.filter(is_public=True)
        serializer = CollectionSerializer(public_collections, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def toggle_public_status(self, request, pk=None):
        collection = self.get_object()
        if collection.user != request.user:
            return Response({"detail": "У вас нет прав на изменение статуса этой коллекции."}, status=403)

        collection.is_public = not collection.is_public
        collection.save()
        return Response({"status": "success", "is_public": collection.is_public})

    @action(detail=True, methods=['post'])
    def add_word(self, request, pk=None):
        collection = self.get_object()
        serializer = AddWordToCollectionSerializer(data=request.data, context={'collection': collection})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'], url_path='remove_word')
    def remove_word(self, request, pk=None):
        collection = self.get_object()
        translation_id = request.query_params.get('translation_id')

        if not translation_id:
            return Response(
                {"detail": "Необходимо указать translation_id."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            word_in_collection = WordInCollection.objects.get(
                collection=collection,
                translation_id=translation_id
            )
            word_in_collection.delete()
            return Response(
                {"status": "Слово удалено из коллекции."},
                status=status.HTTP_204_NO_CONTENT
            )
        except WordInCollection.DoesNotExist:
            return Response(
                {"detail": "Слово не найдено в коллекции."},
                status=status.HTTP_404_NOT_FOUND
            )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"detail": "У вас нет прав на удаление этого объекта."}, status=403)
        self.perform_destroy(instance)
        return Response(status=204)

    @action(detail=True, methods=['get'], url_path='words')
    def list_words(self, request, pk=None):
        collection = self.get_object()
        words_in_collection = WordInCollection.objects.filter(collection=collection)
        serializer = WordInCollectionSerializer(words_in_collection, many=True)
        return Response(serializer.data)