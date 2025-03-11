export interface Category {
  id: number;
  name: string;
}

export interface PartOfSpeech {
  id: number;
  name: string;
}

export interface Word {
  id: number;
  text: string;
  category: Category;
  part_of_speech: PartOfSpeech;
}

export interface Translation {
  id: number;
  text: string;
  audio: string;
  language: string;
  word: Word;
}

export interface Language {
  id: number;
  name: string;
  flag: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
  password: string;
  language: Language;
}

export interface FavoriteWord {
  id: number;
  user: User;
  translation: Translation;
}

export interface DictionaryResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Translation[];
}

export interface FavoriteWordResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: FavoriteWord[];
}

export interface Book {
  id: number;
  title: string;
  author: string;
  language: Language;
  logo: string;
}

export interface BookResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Book[];
}

export interface Sentence {
  id: number;
  text: string;
  audio: string;
  translate: string;
  book: Book;
}

export interface FavoriteBook {
  id: number;
  user: User;
  book: Book;
}

export interface FavoriteBookResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: FavoriteBook[];
}
