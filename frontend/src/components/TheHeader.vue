<template>
  <header class="sticky top-0 z-20 backdrop-blur-md bg-white/70">
    <div class="container">
      <nav class="flex justify-between items-center py-2">
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

        <div v-if="user">
          <RouterLink to="/register" class="block py-2">
            {{ user.name }}
          </RouterLink>
        </div>

        <div v-else>
          <RouterLink to="/register" class="block bg-teal-600 hover:bg-teal-700 text-white rounded-full px-6 py-2">
            Sign Up
          </RouterLink>
        </div>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'

const props = defineProps(['user'])
</script>