<template>
  <UserLayout>
    <div class="breadcrumbs mb-4">
      <ul>
        <li>Home</li>
      </ul>
    </div>

    <div class="xl:w-1/2 card shadow-2xl shadow-emerald-200 bg-emerald-300">
      <div class="card-body">
        <h1 class="card-title mb-2 font-normal">Today</h1>
        <div v-for="meal in meals.items" :key="meal.id">
          {{ meal.brand.name }} {{ meal.name }} {{ meal.weight }} g
        </div>
        <div>Totally: {{ meals.total }}</div>
      </div>
    </div>
  </UserLayout>
</template>

<script setup>
import UserLayout from '@/components/layouts/UserLayout.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { RouterLink } from 'vue-router'

const meals = ref({ items: [], limit: 0, offset: 0, total: 0 })

onMounted(async () => {
  await getMeals()
})

async function getMeals() {
  await axios.get('/meals').then(({ data }) => {
    meals.value = data
  }).catch(() => {
  })
}
</script>