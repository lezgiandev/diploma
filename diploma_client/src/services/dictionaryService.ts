import axios from 'axios';
import { API_URL } from '@/services/baseURL';
import type {Category, DictionaryResponse, PartOfSpeech} from '@/types/dictionary';

export const getWords = async (params: {
  category?: number;
  partOfSpeech?: number;
  search?: string;
  page?: number;
}): Promise<DictionaryResponse> => {
  try {
    const response = await axios.get<DictionaryResponse>(`${API_URL}/dictionary/`, {
      params: {
        word__category: params.category,
        word__part_of_speech: params.partOfSpeech,
        search: params.search,
        page: params.page,
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении слов:', error);
    throw error;
  }
};

export const getCategories = async (): Promise<Category[]> => {
  try {
    const response = await axios.get<Category[]>(`${API_URL}/categories/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении категорий:', error);
    throw error;
  }
};

export const getPartsOfSpeech = async (): Promise<PartOfSpeech[]> => {
  try {
    const response = await axios.get<PartOfSpeech[]>(`${API_URL}/parts-of-speech/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении частей речи:', error);
    throw error;
  }
};

export const addToFavorites = async (translationId: number): Promise<void> => {
  try {
    await axios.post(
      `${API_URL}/favoriteWords/`,
      { translation: translationId },
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

export const removeFromFavorites = async (translationId: number): Promise<void> => {
  try {
    await axios.delete(`${API_URL}/favoriteWords/delete/`, {
      params: {
        translation_id: translationId,
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
