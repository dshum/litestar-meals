<template>
  <UserLayout>
    <div class="home">
      <h1 class="text-3xl my-2">Today</h1>
      <div v-for="meal in meals.items">
        {{ meal.brand.name }} {{ meal.name }} {{ meal.weight }} g
      </div>
      <div>Totally: {{ meals.total }}</div>
    </div>
  </UserLayout>
</template>

<script setup>
import UserLayout from '@/components/layouts/UserLayout.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'


const meals = ref({ items: [], limit: 0, offset: 0, total: 0 })

onMounted(async () => {
  const response = await axios.get('/meals')
  meals.value = response.data
})
</script>