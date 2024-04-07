<script setup>
import { onMounted, ref } from 'vue'
import { client } from '@/axios.js'

const meals = ref({ items: [], limit: 0, offset: 0, total: 0 })

onMounted(async () => {
  await getMeals()
})

async function getMeals() {
  await client.get('/meals').then(({ data }) => {
    meals.value = data
  }).catch(() => {
  })
}
</script>

<template>
  <div class="card shadow-2xl shadow-slate-200 bg-base-100">
    <div class="card-body">
      <h1 class="card-title mb-2 font-normal">Today</h1>

      <div v-if="meals.total" class="overflow-x-auto">
        <table class="table table-zebra">
          <!-- head -->
          <thead>
          <tr>
            <th>Name</th>
            <th>Calories/100 g</th>
            <th>Weight, g</th>
            <th>Brand</th>
            <th>Store</th>
          </tr>
          </thead>
          <tbody>

          <tr v-for="meal in meals.items">
            <td>{{ meal.product.name }}</td>
            <td>{{ meal.product.calories }}</td>
            <td>{{ meal.weight }}</td>
            <td>{{ meal.product.brand?.name || '&#151;' }}</td>
            <td>{{ meal.product.store?.name || '&#151;' }}</td>
          </tr>
          </tbody>
        </table>
      </div>

      <div v-else>
        No meals added yet.
      </div>
    </div>
  </div>
</template>