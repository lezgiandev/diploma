from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.library.models import Book, Sentence, FavoriteBook
from apps.library.serializers import BookSerializer, SentenceSerializer, FavoriteBookSerializer
from apps.user.models import User


class LibraryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if isinstance(self.request.user, User) and hasattr(self.request.user, 'language'):
            return Book.objects.filter(language=self.request.user.language)
        return Book.objects.none()

    @action(detail=True, methods=['get'], url_path='sentences')
    def list_sentences(self, request, pk=None):
        book = self.get_object()
        sentences = Sentence.objects.filter(book=book)
        serializer = SentenceSerializer(sentences, many=True)
        return Response(serializer.data)


class FavoriteBookViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteBookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return FavoriteBook.objects.filter(
                user=self.request.user,
                book__language=self.request.user.language
            )
        return FavoriteBook.objects.none()

    def perform_create(self, serializer):
        if isinstance(self.request.user, User):
            book_id = serializer.validated_data['book'].id
            if FavoriteBook.objects.filter(user=self.request.user, book_id=book_id).exists():
                raise serializers.ValidationError("Эта книга уже в избранном!")
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
        book_id = request.query_params.get('book_id')
        if not book_id:
            return Response({"detail": "Необходимо указать book_id."}, status=400)

        is_favorite = FavoriteBook.objects.filter(
            user=request.user,
            book_id=book_id
        ).exists()

        return Response({"is_favorite": is_favorite})