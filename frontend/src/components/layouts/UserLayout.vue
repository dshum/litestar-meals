<template>
  <TheHeader />

  <main class="flex flex-col flex-grow">
    <div class="container py-4">
      <slot />
    </div>
  </main>

  <TheFooter />
</template>

<script setup>
import TheHeader from '@/components/TheHeader.vue'
import TheFooter from '@/components/TheFooter.vue'
</script>