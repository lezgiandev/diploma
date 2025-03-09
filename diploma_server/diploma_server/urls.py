from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.dictionary.views import DictionaryViewSet, FavoriteWordViewSet, CollectionViewSet, CategoryViewSet, \
    PartOfSpeechViewSet
from apps.language.views import LanguageListView
from apps.library.views import LibraryViewSet, FavoriteBookViewSet
from apps.user.views import RegisterView, LanguageUpdateView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'parts-of-speech', PartOfSpeechViewSet, basename='parts-of-speech')
router.register(r'dictionary', DictionaryViewSet, basename='dictionary')
router.register(r'library', LibraryViewSet, basename='library')
router.register(r'favoriteWords', FavoriteWordViewSet, basename='favoriteWords')
router.register(r'favoriteBooks', FavoriteBookViewSet, basename='favoriteBooks')
router.register(r'collections', CollectionViewSet, basename='collections')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/languages/', LanguageListView.as_view(), name='language-list'),
    path('api/user/language/', LanguageUpdateView.as_view(), name='language-update'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)