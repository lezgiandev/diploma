import {defineStore} from 'pinia';
import {ref} from 'vue';
import {
  addToFavoritesBook,
  getBooks,
  getBookSentences,
  getFavoriteBooks,
  removeFromFavoritesBook,
} from '@/services/libraryService';
import type {Book, Sentence} from '@/types/types.ts';

export const useLibraryStore = defineStore('library', () => {
  const books = ref<Book[]>([]);
  const favoriteBooks = ref<Book[]>([]);
  const currentBookSentences = ref<Sentence[]>([]);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  const currentPage = ref(1);
  const pageSize = ref(10);
  const totalCount = ref(0);

  const fetchBooks = async () => {
    isLoading.value = true;
    error.value = null;
    try {
      const response = await getBooks({
        page: currentPage.value,
      });
      books.value = response.results;
      totalCount.value = response.count;
    } catch (err) {
      error.value = 'Ошибка при загрузке книг';
      console.error('Ошибка при загрузке книг:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const fetchBookSentences = async (bookId: number) => {
    isLoading.value = true;
    try {
      currentBookSentences.value = await getBookSentences(bookId, {});

      if (!books.value.some(b => b.id === bookId)) {
        await fetchBooks();
      }
    } catch (err) {
      console.error('Ошибка при загрузке предложений:', err);
    } finally {
      isLoading.value = false;
    }
  };

  const fetchFavorites = async () => {
    try {
      const response = await getFavoriteBooks({});
      favoriteBooks.value = response.results.map(fb => fb.book);
    } catch (err) {
      console.error('Ошибка при загрузке избранных:', err);
    }
  };

  const addFavorite = async (bookId: number) => {
    try {
      await addToFavoritesBook(bookId);
      await fetchFavorites();
    } catch (err) {
      console.error('Ошибка при добавлении в избранное:', err);
    }
  };

  const removeFavorite = async (bookId: number) => {
    try {
      await removeFromFavoritesBook(bookId);
      await fetchFavorites();
    } catch (err) {
      console.error('Ошибка при удалении из избранного:', err);
    }
  };

  const isFavorite = (bookId: number) => {
    return favoriteBooks.value.some(fb => fb.id === bookId);
  };

  return {
    books,
    favoriteBooks,
    currentBookSentences,
    isLoading,
    error,
    currentPage,
    pageSize,
    totalCount,
    fetchBooks,
    fetchBookSentences,
    fetchFavorites,
    addFavorite,
    removeFavorite,
    isFavorite,
  };
});
