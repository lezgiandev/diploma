from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.language.models import Language
from apps.language.serializers import LanguageSerializer


class LanguageListView(generics.ListAPIView):
    permission_classes = [AllowAny]

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer