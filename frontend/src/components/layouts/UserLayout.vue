<template>
  <TheHeader :user="false" />

  <main class="flex flex-col flex-grow">
    <div class="container py-4">
      <slot />
    </div>
  </main>

  <TheFooter />
</template>

<script setup>
import { RouterLink } from 'vue-router'
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'
</script>