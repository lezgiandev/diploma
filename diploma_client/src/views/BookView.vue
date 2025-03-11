<template>
  <div class="min-h-screen flex flex-col bg-background-one">
    <NavBar />
    <main class="flex-grow container mx-auto px-4 py-8">
      <button
        @click="$router.go(-1)"
        class="mb-4 p-2 bg-button-main text-button-text rounded-lg hover:bg-button-mainhover transition-colors"
      >
        Назад
      </button>

      <div class="p-4 bg-background-two rounded-lg">
        <h2 class="text-font-main text-2xl mb-4 font-medium">{{ currentBook?.title }}</h2>

        <div class="mt-6 space-y-4">
          <div
            v-for="sentence in libraryStore.currentBookSentences"
            :key="sentence.id"
            class="p-4 bg-background-three rounded-lg transition-all duration-300"
          >
            <div class="flex flex-wrap items-center justify-between gap-2">
              <p class="text-font-main text-xl font-medium break-words flex-1 min-w-[200px]">
                {{ sentence.text }}
              </p>

              <div class="flex items-center gap-4">
                <button
                  @click="toggleTranslate(sentence.id)"
                  class="p-2 bg-button-main text-button-text rounded-lg hover:bg-button-mainhover transition-colors"
                >
                  {{ showTranslate[sentence.id] ? 'Скрыть' : 'Показать' }}
                </button>

                <button
                  @click="playAudio(sentence.audio)"
                  class="p-2 bg-button-main text-button-text rounded-lg hover:bg-button-mainhover transition-colors"
                >
                  <svg
                    class="w-6 h-6"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"
                    />
                  </svg>
                </button>
              </div>
            </div>

            <transition
              enter-active-class="transition-all duration-300 ease-out"
              leave-active-class="transition-all duration-200 ease-in"
              enter-from-class="opacity-0 max-h-0"
              enter-to-class="opacity-100 max-h-40"
              leave-from-class="opacity-100 max-h-40"
              leave-to-class="opacity-0 max-h-0"
            >
              <p
                v-if="showTranslate[sentence.id]"
                class="text-font-main mt-3 pl-2 border-l-4 border-font-colored break-words whitespace-pre-line"
              >
                {{ sentence.translate }}
              </p>
            </transition>
          </div>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import { useLibraryStore } from '@/stores/libraryStore';
import { computed, onMounted, ref } from 'vue';
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";

const libraryStore = useLibraryStore();
const route = useRoute();
const showTranslate = ref<Record<number, boolean>>({});

const currentBook = computed(() =>
  libraryStore.books.find(b => b.id === Number(route.params.bookId))
);

const playAudio = (audioUrl: string) => {
  if (audioUrl) new Audio(audioUrl).play();
};

const toggleTranslate = (sentenceId: number) => {
  showTranslate.value = {
    ...showTranslate.value,
    [sentenceId]: !showTranslate.value[sentenceId]
  };
};

onMounted(async () => {
  await libraryStore.fetchBookSentences(Number(route.params.bookId));
});
</script>
