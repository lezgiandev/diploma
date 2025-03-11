import axios from "axios";
import {API_URL} from "@/services/baseURL.ts";
import type {Language} from "@/types/types.ts";

export const getUserLanguage = async (): Promise<Language> => {
  try {
    const response = await axios.get<Language>(`${API_URL}/checklanguage/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении языка:', error);
    throw error;
  }
};

export const getAllLanguages = async (): Promise<Language[]> => {
  try {
    const response = await axios.get<Language[]>(`${API_URL}/languages/`);
    return response.data;
  } catch (error) {
    console.error('Ошибка при получении языков:', error);
    throw error;
  }
};
