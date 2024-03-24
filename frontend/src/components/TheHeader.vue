<script setup>
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'

const props = defineProps(['user'])
const authStore = useAuthStore()
</script>

<template>
  <header class="sticky top-0 z-20 backdrop-blur-md bg-white/70">
    <div class="container">
      <nav class="flex justify-between items-center h-16 py-2">
        <div class="text-xl">
          <RouterLink to="/">Meals</RouterLink>
        </div>

        <div v-if="user">
          <ul class="flex items-center gap-[4vw]">
            <li>
              <RouterLink to="/" class="hover:text-gray-500">Meals</RouterLink>
            </li>
            <li>
              <RouterLink to="/about" class="hover:text-gray-500">Calories</RouterLink>
            </li>
          </ul>
        </div>

        <div v-if="user" class="flex flex-row items-center space-x-2">
          <RouterLink :to="{name: 'home'}">
            <div class="w-12 h-12 rounded-full bg-amber-300 flex flex-col items-center justify-center">
              <div>DS</div>
            </div>
          </RouterLink>

          <a href="#" class="" @click.prevent="authStore.logout">Logout</a>
        </div>
      </nav>
    </div>
  </header>
</template>