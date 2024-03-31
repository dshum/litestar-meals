<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'

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

<template>
  <div class="card shadow-2xl shadow-emerald-200 bg-base-100">
    <div class="card-body">
      <h1 class="card-title mb-2 font-normal">Today</h1>

      <div v-if="meals.total">
        <div v-for="meal in meals.items" :key="meal.id">
          {{ meal.brand.name }} {{ meal.name }} {{ meal.weight }} g
        </div>
        <div>Totally: {{ meals.total }}</div>
      </div>

      <div v-else>
        No meals added yet.
      </div>
    </div>
  </div>
</template>