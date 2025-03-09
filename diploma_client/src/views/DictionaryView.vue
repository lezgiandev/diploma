<template>
  <div class="min-h-screen flex flex-col bg-stone-900">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <!-- Поиск и фильтры -->
      <div class="mb-8 space-y-4 md:space-y-0 md:flex md:space-x-4 font-nunito">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Поиск по словам или переводам"
          class="w-full md:w-1/3 p-3 bg-stone-800 text-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-300"
          @input="handleSearch"
        />

        <Listbox v-model="selectedCategory" @update:modelValue="fetchWords">
          <div class="relative w-full md:w-1/3">
            <!-- Кнопка-триггер -->
            <ListboxButton
              class="w-full p-3 bg-stone-800 text-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-300 text-left appearance-none pr-10"
            >
              {{ dictionaryStore.categories.find(c => c.id === selectedCategory)?.name || 'Все категории' }}
              <!-- Стрелка -->
              <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                <svg class="w-5 h-5 text-orange-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </ListboxButton>

            <!-- Выпадающий список -->
            <ListboxOptions
              class="absolute z-10 w-full mt-1 bg-stone-800 rounded-lg shadow-lg focus:outline-none max-h-60 overflow-auto"
            >
              <!-- Опция "Все категории" -->
              <ListboxOption
                :value="null"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-stone-700 text-orange-300' : 'bg-stone-800 text-orange-300',
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
                    active ? 'bg-stone-700 text-orange-300' : 'bg-stone-800 text-orange-300',
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
          <div class="relative w-full md:w-1/3">
            <!-- Кнопка-триггер -->
            <ListboxButton
              class="w-full p-3 bg-stone-800 text-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-300 text-left appearance-none pr-10"
            >
              {{ dictionaryStore.partsOfSpeech.find(p => p.id === selectedPartOfSpeech)?.name || 'Все части речи' }}
              <!-- Стрелка -->
              <span class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                <svg class="w-5 h-5 text-orange-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </span>
            </ListboxButton>

            <!-- Выпадающий список -->
            <ListboxOptions
              class="absolute z-10 w-full mt-1 bg-stone-800 rounded-lg shadow-lg focus:outline-none max-h-60 overflow-auto"
            >
              <!-- Опция "Все части речи" -->
              <ListboxOption
                :value="null"
                v-slot="{ active }"
                class="cursor-default"
              >
                <li
                  :class="[
                    active ? 'bg-stone-700 text-orange-300' : 'bg-stone-800 text-orange-300',
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
                    active ? 'bg-stone-700 text-orange-300' : 'bg-stone-800 text-orange-300',
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
          class="p-6 bg-stone-800 rounded-lg shadow-lg flex flex-col md:flex-row justify-between items-center"
        >
          <!-- Поля для слов -->
          <div class="flex flex-grow space-x-4 w-full md:w-auto font-nunito">
            <div class="flex-1 p-2 rounded-lg bg-stone-700 text-orange-300 text-center truncate">
              {{ translation.word.text }}
            </div>
            <div class="text-orange-300 self-center">
              —
            </div>
            <div class="flex-1 p-2 rounded-lg bg-stone-700 text-orange-300 text-center truncate">
              {{ translation.text }}
            </div>
          </div>

          <!-- Кнопки -->
          <div class="flex space-x-4 mt-4 md:mt-0 md:ml-4 font-nunito">
            <button
              @click="playAudio(translation.audio)"
              class="p-2 bg-orange-300 text-stone-800 rounded-lg hover:bg-orange-400 transition duration-300"
            >
              🎧
            </button>
            <button
              v-if="isFavorite(translation.id)"
              @click="removeFromFavorites(translation.id)"
              class="p-2 bg-red-500 text-stone-800 rounded-lg hover:bg-red-600 transition duration-300"
            >
              ❌ Удалить из избранного
            </button>
            <button
              v-else
              @click="addToFavorites(translation.id)"
              class="p-2 bg-orange-300 text-stone-800 rounded-lg hover:bg-orange-400 transition duration-300"
            >
              ❤️ Добавить в избранное
            </button>
          </div>
        </div>
      </div>

      <!-- Пагинация -->
      <div class="mt-8 flex justify-center space-x-4">
        <button
          :disabled="dictionaryStore.currentPage === 1"
          @click="prevPage"
          class="p-2 bg-stone-800 text-orange-300 rounded-lg hover:bg-stone-700 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Назад
        </button>
        <span class="text-orange-300 text-xl self-center font-nunito">
          Страница {{ dictionaryStore.currentPage }} из {{ totalPages }}
        </span>
        <button
          :disabled="dictionaryStore.currentPage >= totalPages"
          @click="nextPage"
          class="p-2 bg-stone-800 text-orange-300 rounded-lg hover:bg-stone-700 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
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

const dictionaryStore = useDictionaryStore();

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
  await dictionaryStore.initialize();
});
</script>

<style>
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #1c1917;
  border-radius: 6px;
}

::-webkit-scrollbar-thumb {
  background: #fdba74;
  border-radius: 6px;
}

::-webkit-scrollbar-thumb:hover {
  background: #fb923c;
}
</style>
