<script setup>
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth.js'

const authStore = useAuthStore()
</script>

<template>
  <header class="sticky top-0 z-20 backdrop-blur-md bg-white/70">
    <div class="container">
      <nav class="flex justify-between items-center h-16 py-2">
        <div class="text-xl">
          <RouterLink to="/">Meals</RouterLink>
        </div>

        <div v-if="authStore.user">
          <ul class="flex items-center gap-[4vw]">
            <li>
              <RouterLink to="/" class="hover:text-gray-500">Meals</RouterLink>
            </li>
            <li>
              <RouterLink to="/about" class="hover:text-gray-500">Calories</RouterLink>
            </li>
          </ul>
        </div>

        <div v-if="authStore.user" class="dropdown dropdown-end">
          <div tabindex="0" role="button"
               class="w-12 h-12 rounded-full bg-amber-300 flex flex-col items-center justify-center">
            <div>{{ authStore.avatarName }}</div>
          </div>
          <ul tabindex="0" class="menu dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
            <li><a>Profile</a></li>
            <li><a>Settings</a></li>
            <li><a @click.prevent="authStore.logout">Logout</a></li>
          </ul>
        </div>
      </nav>
    </div>
  </header>
</template>