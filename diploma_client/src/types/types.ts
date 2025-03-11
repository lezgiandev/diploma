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


export interface DictionaryResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Translation[];
}
