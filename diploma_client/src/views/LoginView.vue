<template>
  <div class="min-h-screen flex flex-col">
    <NavBar />
    <div class="flex-grow container mx-auto px-4 py-8">
      <div class="max-w-md mx-auto bg-background-two rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold text-center mb-8 text-font-colored">Авторизация</h1>
        <form @submit.prevent="login" class="space-y-6">
          <div class="mb-4">
            <label class="block text-sm font-medium text-font-main">Имя пользователя</label>
            <input v-model="username" type="text" class="mt-1 block w-full px-4 py-2 bg-background-three border border-font-main rounded-lg text-font-main focus:outline-none focus:ring-2 focus:ring-button-main" required />
          </div>
          <div class="mb-4">
            <label class="block text-sm font-medium text-font-main">Пароль</label>
            <input v-model="password" type="password" class="mt-1 block w-full px-4 py-2 bg-background-three border border-font-main rounded-lg text-font-main focus:outline-none focus:ring-2 focus:ring-button-main" required />
          </div>
          <button type="submit" class="w-full px-4 py-2 bg-button-main text-button-text font-semibold rounded-lg hover:bg-button-mainhover transition duration-300">Войти</button>
        </form>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import { useRouter } from 'vue-router';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';

const username = ref('');
const password = ref('');
const authStore = useAuthStore();
const router = useRouter();

const login = async () => {
  await authStore.login({ username: username.value, password: password.value });
  router.push('/');
};
</script>
