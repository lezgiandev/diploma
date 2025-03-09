import {defineStore} from 'pinia';
import {ref} from 'vue';
import {
  addToFavorites,
  getCategories,
  getPartsOfSpeech,
  getWords,
  removeFromFavorites,
} from '@/services/dictionaryService';
import type {Category, PartOfSpeech, Translation} from '@/types/dictionary';

export const useDictionaryStore = defineStore('dictionary', () => {
  const translations = ref<Translation[]>([]);
  const favorites = ref<Translation[]>([]);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const currentPage = ref(1);
  const pageSize = ref(20);
  const totalCount = ref(0);

  const categories = ref<Category[]>([]);
  const partsOfSpeech = ref<PartOfSpeech[]>([])

  const fetchWords = async (params: {
    category?: number;
    partOfSpeech?: number;
    search?: string;
  }) => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await getWords({
        ...params,
        page: currentPage.value,
      });
      translations.value = response.results;
      totalCount.value = response.count;
    } catch (err) {
      error.value = 'Ошибка при загрузке слов';
      console.error('Ошибка при загрузке слов:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const fetchCategories = async () => {
    try {
      categories.value = await getCategories();
    } catch (err) {
      console.error('Ошибка при загрузке категорий:', err);
    }
  };

  const fetchPartsOfSpeech = async () => {
    try {
      partsOfSpeech.value = await getPartsOfSpeech();
    } catch (err) {
      console.error('Ошибка при загрузке частей речи:', err);
    }
  };

  const addFavorite = async (translationId: number) => {
    try {
      await addToFavorites(translationId);
      const translation = translations.value.find((t) => t.id === translationId);
      if (translation) {
        favorites.value.push(translation);
      }
    } catch (err) {
      console.error('Ошибка при добавлении в избранное:', err);
    }
  };

  const removeFavorite = async (translationId: number) => {
    try {
      await removeFromFavorites(translationId); // Используем translationId
      favorites.value = favorites.value.filter((t) => t.id !== translationId);
    } catch (err) {
      console.error('Ошибка при удалении из избранного:', err);
    }
  };

  const isFavorite = (translationId: number) => {
    return favorites.value.some((fav) => fav.id === translationId);
  };

  const initialize = async () => {
    await fetchCategories();
    await fetchPartsOfSpeech();
    await fetchWords({});
  };

  return {
    translations,
    favorites,
    isLoading,
    error,
    currentPage,
    pageSize,
    totalCount,
    categories,
    partsOfSpeech,
    fetchWords,
    addFavorite,
    removeFavorite,
    isFavorite,
    initialize,
  };
});
