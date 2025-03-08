<template>
  <div class="min-h-screen flex flex-col">
    <NavBar />
    <div class="container mx-auto px-4 py-8">
      <div class="max-w-md mx-auto bg-stone-800 rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold text-center mb-8 text-orange-300">Регистрация</h1>
        <form @submit.prevent="register" class="space-y-6">
          <div class="mb-4">
            <label class="block text-sm font-medium text-orange-100">Имя пользователя</label>
            <input v-model="username" type="text" class="mt-1 block w-full px-4 py-2 bg-stone-900 border border-orange-100 rounded-lg text-stone-100 focus:outline-none focus:ring-2 focus:ring-orange-300" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-orange-100">Электронная почта</label>
            <input v-model="email" type="email" class="mt-1 block w-full px-4 py-2 bg-stone-900 border border-orange-100 rounded-lg text-stone-100 focus:outline-none focus:ring-2 focus:ring-orange-300" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-orange-100">Пароль</label>
            <input v-model="password" type="password" class="mt-1 block w-full px-4 py-2 bg-stone-900 border border-orange-100 rounded-lg text-stone-100 focus:outline-none focus:ring-2 focus:ring-orange-300" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-orange-100">Подтвердите пароль</label>
            <input v-model="confirmPassword" type="password" class="mt-1 block w-full px-4 py-2 bg-stone-900 border border-orange-100 rounded-lg text-stone-100 focus:outline-none focus:ring-2 focus:ring-orange-300" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-orange-100">Выберите язык</label>
            <select v-model="selectedLanguage" class="mt-1 block w-full px-4 py-2 bg-stone-900 border border-orange-100 rounded-lg text-stone-100 focus:outline-none focus:ring-2 focus:ring-orange-300" required>
              <option v-for="language in languages" :key="language.id" :value="language.id">{{ language.name }}</option>
            </select>
          </div>
          <button type="submit" class="w-full px-4 py-2 bg-orange-300 text-stone-800 font-semibold rounded-lg hover:bg-orange-100 transition duration-300">Зарегистрироваться</button>
        </form>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'vue-router';
import axios from 'axios';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import {API_URL} from "@/services/baseURL.ts";

const username = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const selectedLanguage = ref<number | null>(null);
const languages = ref<{ id: number; name: string; flag: string }[]>([]);
const errorMessage = ref('');
const authStore = useAuthStore();
const router = useRouter();

onMounted(async () => {
  try {
    const response = await axios.get(`${API_URL}/languages/`);
    languages.value = response.data.results;
  } catch (error) {
    console.error('Ошибка при загрузке языков', error);
  }
});

const register = async () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Пароли не совпадают';
    return;
  }

  if (!selectedLanguage.value) {
    errorMessage.value = 'Пожалуйста, выберите язык';
    return;
  }

  await authStore.register({
    username: username.value,
    email: email.value,
    password: password.value,
    language: selectedLanguage.value
  });
  await router.push('/');
};
</script>
