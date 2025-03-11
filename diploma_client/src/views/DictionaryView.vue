<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <!-- Добавленный блок с названием языка -->
      <div class="mb-6">
        <h1 class="text-font-main text-xl md:text-2xl font-normal font-main">
          Словарь для языка: {{ userStore.language?.name }}
        </h1>
      </div>

      <!-- Поиск и фильтры -->
      <div class="mb-8 space-y-4 md:space-y-0 md:flex md:space-x-4 font-main">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Поиск по словам или переводам"
          class="w-full md:w-1/3 p-3 bg-background-two text-font-main rounded-lg focus:outline-none focus:ring-2 focus:ring-button-main"
          @input="handleSearch"
        />

        <Listbox v-model="selectedCategory" @update:modelValue="fetchWords">
          <div class="relative w-full md:w-1/3 font-main">
            <!-- Кнопка-триггер -->
            <ListboxButton
              class="w-full p-3 bg-background-two text-font-main rounded-lg focus:outline-none focus:ring-2 focus:ring-button-main text-left appearance-none pr-10"
            >
              {{ dictionaryStore.categories.find(c => c.id === selectedCategory)?.name || 'Все категории' }}
              <!-- Стрелка -->
              <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                <svg class="w-5 h-5 text-button-main" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </ListboxButton>

            <!-- Выпадающий список -->
            <ListboxOptions
              class="absolute z-10 w-full mt-1 bg-background-two rounded-lg shadow-lg focus:outline-none max-h-60 overflow-auto"
            >
              <!-- Опция "Все категории" -->
              <ListboxOption
                :value="null"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-two text-font-main',
                    'p-3 transition-colors'
                  ]"
                >
                  Все категории
                </li>
              </ListboxOption>

              <!-- Остальные опции -->
              <ListboxOption
                v-for="category in dictionaryStore.categories"
                :key="category.id"
                :value="category.id"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-two text-font-main',
                    'p-3 transition-colors'
                  ]"
                >
                  {{ category.name }}
                </li>
              </ListboxOption>
            </ListboxOptions>
          </div>
        </Listbox>

        <Listbox v-model="selectedPartOfSpeech" @update:modelValue="fetchWords">
          <div class="relative w-full md:w-1/3 font-main">
            <!-- Кнопка-триггер -->
            <ListboxButton
              class="w-full p-3 bg-background-two text-font-main rounded-lg focus:outline-none focus:ring-2 focus:ring-button-main text-left appearance-none pr-10"
            >
              {{ dictionaryStore.partsOfSpeech.find(p => p.id === selectedPartOfSpeech)?.name || 'Все части речи' }}
              <!-- Стрелка -->
              <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                <svg class="w-5 h-5 text-button-main" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </ListboxButton>

            <!-- Выпадающий список -->
            <ListboxOptions
              class="absolute z-10 w-full mt-1 bg-background-two rounded-lg shadow-lg focus:outline-none max-h-60 overflow-auto"
            >
              <!-- Опция "Все части речи" -->
              <ListboxOption
                :value="null"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-two text-font-main',
                    'p-3 transition-colors'
                  ]"
                >
                  Все части речи
                </li>
              </ListboxOption>

              <!-- Остальные опции -->
              <ListboxOption
                v-for="part in dictionaryStore.partsOfSpeech"
                :key="part.id"
                :value="part.id"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-background-three text-font-main' : 'bg-background-two text-font-main',
                    'p-3 transition-colors'
                  ]"
                >
                  {{ part.name }}
                </li>
              </ListboxOption>
            </ListboxOptions>
          </div>
        </Listbox>
      </div>

      <!-- Список слов -->
      <div class="grid grid-cols-1 xl:grid-cols-2 2xl:grid-cols-2 gap-4">
        <div
          v-for="translation in dictionaryStore.translations"
          :key="translation.id"
          class="p-6 bg-background-two rounded-lg shadow-lg flex flex-col md:flex-row justify-between items-center"
        >
          <!-- Поля для слов -->
          <div class="flex flex-grow space-x-4 w-full md:w-auto font-main">
            <div class="flex-1 p-2 rounded-lg bg-background-three text-font-main text-center truncate font-semibold">
              {{ translation.word.text }}
            </div>
            <div class="text-font-main self-center">
              —
            </div>
            <div class="flex-1 p-2 rounded-lg bg-background-three text-font-main text-center truncate font-semibold">
              {{ translation.text }}
            </div>
          </div>

          <!-- Кнопки -->
          <div class="flex space-x-4 mt-4 md:mt-0 md:ml-4 font-main">
            <!-- Кнопка проигрывания аудио -->
            <button
              @click="playAudio(translation.audio)"
              class="p-2 bg-button-main text-button-text rounded-lg hover:bg-button-mainhover transition duration-300"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"
                />
              </svg>
            </button>

            <!-- Кнопка удаления из избранного -->
            <button
              v-if="isFavorite(translation.id)"
              @click="removeFromFavorites(translation.id)"
              class="p-2 bg-button-cancel text-button-text rounded-lg hover:bg-button-cancelhover transition duration-300"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>

            <!-- Кнопка добавления в избранное -->
            <button
              v-else
              @click="addToFavorites(translation.id)"
              class="p-2 bg-button-main text-button-text rounded-lg hover:bg-button-mainhover transition duration-300"
            >
              <svg
                class="w-6 h-6"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Пагинация -->
      <div class="mt-8 flex justify-center space-x-4 font-main">
        <button
          :disabled="dictionaryStore.currentPage === 1"
          @click="prevPage"
          class="p-2 bg-neutral-800 text-font-main rounded-lg hover:bg-background-three transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Назад
        </button>
        <span class="text-font-main text-base self-center font-main">
          Страница {{ dictionaryStore.currentPage }} из {{ totalPages }}
        </span>
        <button
          :disabled="dictionaryStore.currentPage >= totalPages"
          @click="nextPage"
          class="p-2 bg-background-two text-font-main rounded-lg hover:bg-background-three transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Вперед
        </button>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useDictionaryStore } from '@/stores/dictionaryStore';
import { Listbox, ListboxButton, ListboxOptions, ListboxOption } from '@headlessui/vue'
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import {useUserStore} from "@/stores/userStore.ts";

const dictionaryStore = useDictionaryStore();
const userStore = useUserStore();

const searchQuery = ref('');
const selectedCategory = ref<number | null>(null);
const selectedPartOfSpeech = ref<number | null>(null);

const totalPages = computed(() => Math.ceil(dictionaryStore.totalCount / dictionaryStore.pageSize));

const fetchWords = async () => {
  await dictionaryStore.fetchWords({
    category: selectedCategory.value ? Number(selectedCategory.value) : undefined,
    partOfSpeech: selectedPartOfSpeech.value ? Number(selectedPartOfSpeech.value) : undefined,
    search: searchQuery.value,
  });
};

let searchTimeout: number | null = null;
const handleSearch = () => {
  if (searchTimeout) clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    fetchWords();
  }, 300);
};

const nextPage = () => {
  dictionaryStore.currentPage += 1;
  fetchWords();
};

const prevPage = () => {
  if (dictionaryStore.currentPage > 1) {
    dictionaryStore.currentPage -= 1;
    fetchWords();
  }
};

const playAudio = (audioUrl: string) => {
  if (audioUrl) {
    const audio = new Audio(audioUrl);
    audio.play();
  }
};

const addToFavorites = async (translationId: number) => {
  await dictionaryStore.addFavorite(translationId);
};

const removeFromFavorites = async (translationId: number) => {
  await dictionaryStore.removeFavorite(translationId);
};

const isFavorite = (translationId: number) => {
  return dictionaryStore.favorites.some((fav) => fav.id === translationId);
};

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await dictionaryStore.initialize();
});
</script>
