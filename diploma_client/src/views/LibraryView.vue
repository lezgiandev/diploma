<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <!-- Добавленный блок с названием языка -->
      <div class="mb-6">
        <h1 class="text-font-main text-xl md:text-2xl font-normal font-main">
          Библиотека для языка: {{ userStore.language?.name }}
        </h1>
      </div>

      <!-- Список книг -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div
          v-for="book in libraryStore.books"
          :key="book.id"
          class="p-4 bg-background-two rounded-lg"
        >
          <img :src="book.logo" class="w-full h-48 object-cover mb-4 rounded-lg"  alt=""/>
          <h3 class="text-font-colored text-xl font-main">{{ book.title }}</h3>
          <p class="text-font-main font-main">{{ book.author }}</p>

          <div class="mt-4 flex justify-between items-center gap-4 font-main">
            <button
              @click="$router.push({ name: 'book', params: { bookId: book.id } })"
              class="flex-grow py-2 px-4 bg-button-main text-button-text rounded-lg hover:bg-button-mainhover"
            >
              Читать
            </button>

            <button
              v-if="isFavorite(book.id)"
              @click="removeFromFavorites(book.id)"
              class="p-2 bg-button-cancel text-button-text rounded-lg hover:bg-button-cancelhover transition duration-300 flex flex-row"
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
              @click="addToFavorites(book.id)"
              class="p-2 bg-button-main text-button-text rounded-lg hover:bg-button-mainhover transition duration-300 flex flex-row"
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
          :disabled="libraryStore.currentPage === 1"
          @click="prevPage"
          class="p-2 bg-background-two text-font-main rounded-lg hover:bg-background-three transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Назад
        </button>
        <span class="text-font-main text-base self-center font-main">
          Страница {{ libraryStore.currentPage }} из {{ totalPages }}
        </span>
        <button
          :disabled="libraryStore.currentPage >= totalPages"
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
import { useLibraryStore } from '@/stores/libraryStore';
import {computed, onMounted} from 'vue';
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import {useUserStore} from "@/stores/userStore.ts";

const libraryStore = useLibraryStore();
const userStore = useUserStore();

const totalPages = computed(() => Math.ceil(libraryStore.totalCount / libraryStore.pageSize));

const fetchBooks = async () => {
  await libraryStore.fetchBooks();
};

const addToFavorites = async (translationId: number) => {
  await libraryStore.addFavorite(translationId);
};

const removeFromFavorites = async (translationId: number) => {
  await libraryStore.removeFavorite(translationId);
};

const isFavorite = (translationId: number) => {
  return libraryStore.favoriteBooks.some((fav) => fav.id === translationId);
};

const nextPage = () => {
  libraryStore.currentPage += 1;
  fetchBooks();
};

const prevPage = () => {
  if (libraryStore.currentPage > 1) {
    libraryStore.currentPage -= 1;
    fetchBooks();
  }
};

onMounted(async () => {
  await userStore.fetchUserLanguage();
  await libraryStore.fetchBooks();
  await libraryStore.fetchFavorites();
});
</script>
