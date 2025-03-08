<template>
  <div class="min-h-screen flex flex-col bg-stone-800">
    <NavBar />
    <main class="flex-grow">
      <!-- Герой-секция -->
      <div class="bg-stone-900 py-24">
        <div class="container mx-auto px-4 text-center">
          <h1 class="text-9xl font-fleur text-orange-300 mb-6">Lexify</h1>
          <p class="font-nunito text-xl text-orange-300 mb-8">
            Откройте для себя богатство языков коренных народов России.
          </p>
          <div class="space-x-4">
            <router-link to="/register" class="font-nunito text-xl px-6 py-3 bg-orange-300 text-stone-900 font-normal rounded-lg transition duration-300">
              Начать изучение
            </router-link>
            <router-link to="/about" class="font-nunito text-xl px-6 py-3 bg-transparent border border-orange-300 text-orange-300 font-normal rounded-lg hover:bg-orange-300 hover:text-stone-900 transition duration-300">
              Узнать больше
            </router-link>
          </div>
        </div>
      </div>

      <!-- Секция "Почему Lexify?" -->
      <div class="container mx-auto px-4 py-16">
        <h2 class="font-nunito text-3xl font-bold text-orange-300 text-center mb-12">Почему стоит выбрать нас</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Карточка 1 -->
          <div class="bg-stone-900 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
            <div class="text-orange-300 mb-4">
              <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Уникальные материалы</h3>
            <p class="text-orange-100 text-center text-xl">
              Доступ к редким учебным материалам по языкам коренных народов России.
            </p>
          </div>

          <!-- Карточка 2: Книги билингва -->
          <div class="bg-stone-900 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
            <div class="text-orange-300 mb-4">
              <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <!-- Иконка с буквами на разных языках -->
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l3 3m0 0l3-3m-3 3v14" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Книги билингва</h3>
            <p class="text-orange-100 text-center text-xl">
              Читайте книги на двух языках, чтобы улучшить свои навыки и погрузиться в культуру.
            </p>
          </div>

          <!-- Карточка 3 -->
          <div class="bg-stone-900 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
            <div class="text-orange-300 mb-4">
              <svg class="w-12 h-12 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Интерактивные уроки</h3>
            <p class="text-orange-100 text-center text-xl">
              Учите языки с помощью интерактивных упражнений и тестов.
            </p>
          </div>
        </div>
      </div>

      <!-- Секция "Языки" -->
      <div class="bg-stone-900 py-16">
        <div class="container mx-auto px-4">
          <h2 class="text-3xl font-bold text-orange-300 text-center mb-12 font-nunito">Языки, которые мы поддерживаем</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <!-- Язык 1: Татарский -->
            <div class="bg-stone-800 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
              <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Татарский</h3>
              <p class="text-orange-100 text-center text-xl">
                Изучайте язык татар, один из самых распространённых тюркских языков России.
              </p>
            </div>

            <!-- Язык 2: Башкирский -->
            <div class="bg-stone-800 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
              <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Башкирский</h3>
              <p class="text-orange-100 text-center text-xl">
                Погрузитесь в культуру башкир через их язык, богатый традициями и историей.
              </p>
            </div>

            <!-- Язык 3: Чеченский -->
            <div class="bg-stone-800 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
              <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Чеченский</h3>
              <p class="text-orange-100 text-center text-xl">
                Изучайте чеченский язык, один из самых сложных и красивых языков Кавказа.
              </p>
            </div>

            <!-- Язык 4: Лезгинский -->
            <div class="bg-stone-800 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
              <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Лезгинский</h3>
              <p class="text-orange-100 text-center text-xl">
                Откройте для себя язык лезгин, коренных жителей Дагестана.
              </p>
            </div>

            <!-- Язык 5: Якутский -->
            <div class="bg-stone-800 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
              <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Якутский</h3>
              <p class="text-orange-100 text-center text-xl">
                Изучайте якутский язык, один из самых древних языков Сибири.
              </p>
            </div>

            <!-- Язык 6: Аварский -->
            <div class="bg-stone-800 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
              <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Аварский</h3>
              <p class="text-orange-100 text-center text-xl">
                Познакомьтесь с языком аварцев, крупнейшего народа Дагестана.
              </p>
            </div>

            <!-- Язык 7: Осетинский -->
            <div class="bg-stone-800 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
              <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Осетинский</h3>
              <p class="text-orange-100 text-center text-xl">
                Изучайте осетинский язык, сохранивший древние иранские корни.
              </p>
            </div>

            <!-- Язык 8: Чувашский -->
            <div class="bg-stone-800 p-6 rounded-lg shadow-lg font-nunito transition duration-300 hover:scale-105">
              <h3 class="text-2xl font-bold text-orange-300 text-center mb-4">Чувашский</h3>
              <p class="text-orange-100 text-center text-xl">
                Погрузитесь в культуру чувашей через их уникальный язык.
              </p>
            </div>
          </div>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
</script>
