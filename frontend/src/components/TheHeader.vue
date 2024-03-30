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

        <ul class="flex items-center gap-[4vw]">
          <li>
            <RouterLink :to="{name: 'about'}" class="hover:text-gray-500">Calories</RouterLink>
          </li>
        </ul>

        <button class="btn btn-accent rounded-full">Add meal</button>

        <div class="dropdown dropdown-end">
          <div tabindex="0" role="button"
               class="w-12 h-12 rounded-full bg-amber-300 flex flex-col items-center justify-center">
            <div>{{ authStore.avatarName }}</div>
          </div>
          <ul tabindex="0" class="dropdown-content mt-3 z-[1] bg-base-100 rounded-box shadow w-52 p-2 menu">
            <li class="menu-title">
              <div class="text-accent">{{ authStore.userName }}</div>
              <div class="text-sm font-normal text-secondary-content">{{ authStore.user?.email }}</div>
            </li>
            <li>
              <RouterLink :to="{name: 'profile'}">Profile</RouterLink>
            </li>
            <li><a>Settings</a></li>
            <li><a @click.prevent="authStore.logout">Logout</a></li>
          </ul>
        </div>
      </nav>
    </div>
  </header>
</template>