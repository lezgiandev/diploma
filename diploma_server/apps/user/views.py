from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, LanguageUpdateSerializer, UserLanguageSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = LanguageUpdateSerializer(data=request.data)
        if serializer.is_valid():
            request.user.language = serializer.validated_data['language_id']
            request.user.save()
            return Response({'status': 'User language was updated!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageRetrieveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserLanguageSerializer(request.user)
        return Response(serializer.data)