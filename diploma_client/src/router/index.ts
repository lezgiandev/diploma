import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import { useAuthStore } from '@/stores/authStore';
import DictionaryView from "@/views/DictionaryView.vue";
import LibraryView from "@/views/LibraryView.vue";
import BookView from "@/views/BookView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomeView, meta: { requiresAuth: true } },
    { path: '/dictionary', component: DictionaryView, meta: { requiresAuth: true } },
    { path: '/library', component: LibraryView, meta: { requiresAuth: true } },
    { path: '/library/:bookId', component: BookView, meta: { requiresAuth: true }, name: 'book' },
    { path: '/login', component: LoginView },
    { path: '/register', component: RegisterView },
  ],
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;
