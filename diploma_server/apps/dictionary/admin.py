from django.contrib import admin
from .models import Category, Word, Translation, Collection, PartOfSpeech, WordInCollection


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(PartOfSpeech)
class PartOfSpeechAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'part_of_speech', 'category')
    list_filter = ('category',)
    search_fields = ('text',)

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'language', 'text', 'audio')
    list_filter = ('language',)
    search_fields = ('text', 'word__text')

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'user', 'language', 'is_public')
    list_filter = ('user', 'is_public')
    search_fields = ('name',)

@admin.register(WordInCollection)
class WordInCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'collection', 'translation')
    list_filter = ('collection', )