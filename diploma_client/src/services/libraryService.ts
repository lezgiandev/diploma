import type {BookResponse, FavoriteBookResponse, Sentence} from "@/types/types.ts";
import axios from "axios";
import {API_URL} from "@/services/baseURL.ts";

export const getBooks = async (params: {
  page?: number;
}): Promise<BookResponse> => {
  try {
    const response = await axios.get<BookResponse>(`${API_URL}/library/`, {
      params: {
        page: params.page,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении книг:', error);
    throw error;
  }
};

export const getBookSentences = async (bookId: number, params: {
  page?: number;
}): Promise<Sentence[]> => {
  try {
    const response = await axios.get<Sentence[]>(`${API_URL}/library/${bookId}/sentences/`, {
      params: {
        page: params.page,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении предложений:', error);
    throw error;
  }
};

export const getFavoriteBooks = async (params: {
  page?: number;
}): Promise<FavoriteBookResponse> => {
  try {
    const response = await axios.get<FavoriteBookResponse>(`${API_URL}/favoriteBooks/`, {
      params: {
        page: params.page,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении избранных книг:', error);
    throw error;
  }
};

export const addToFavoritesBook = async (bookId: number): Promise<void> => {
  try {
    await axios.post(
      `${API_URL}/favoriteBooks/`,
      { book_id: bookId },
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      }
    );
  } catch (error) {
    console.error('Ошибка при добавлении в избранное:', error);
    throw error;
  }
};

export const removeFromFavoritesBook = async (bookId: number): Promise<void> => {
  try {
    await axios.delete(`${API_URL}/favoriteBooks/delete/`, {
      params: {
        book_id: bookId,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
  } catch (error) {
    console.error('Ошибка при удалении из избранного:', error);
    throw error;
  }
};
