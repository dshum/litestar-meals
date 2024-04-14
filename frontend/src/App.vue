<script setup>
import { RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth.js'

const authStore = useAuthStore()

onMounted(() => {
  if (!authStore.csrf_cookie_set) {
    authStore.setCSRFCookie()
  }
})
</script>

<template>
  <RouterView />
</template>
