<template>
  <main class="flex flex-col flex-grow">
    <div class="container my-auto py-4">
      <slot />
    </div>
  </main>

  <TheFooter />
</template>

<script setup>
import { RouterLink } from 'vue-router'
import TheFooter from '@/components/TheFooter.vue'
</script>