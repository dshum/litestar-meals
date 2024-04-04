<script setup>
import { onMounted, ref } from 'vue'
import { RouterLink } from 'vue-router'
import UserLayout from '@/components/layouts/UserLayout.vue'
import AddMealForm from '@/components/AddMealForm.vue'
import { client } from '@/axios.js'


const meals = ref({ items: [], limit: 0, offset: 0, total: 0 })
const showModel = ref(false)

onMounted(async () => {
  await getMeals()
})

async function getMeals() {
  await client.get('/meals').then(({ data }) => {
    meals.value = data
  }).catch(() => {
  })
}

async function toggleModal() {
  showModel.value = !showModel.value
}

async function closeModal() {
  showModel.value = false
}
</script>

<template>
  <UserLayout>
    <div class="flex flex-row justify-between items-start mb-2">
      <div class="breadcrumbs">
        <ul>
          <li>
            <RouterLink :to="{name: 'home'}">Home</RouterLink>
          </li>
          <li>Products</li>
        </ul>
      </div>

      <div class="text-right">
        <div @click="toggleModal" class="btn btn-primary">Add meal</div>
      </div>
    </div>

    <div v-if="showModel" class="flex flex-row justify-end mb-6">
      <div class="card w-full xl:w-1/2 bg-base-100 shadow-xl">
        <div class="card-body text-left">
          <AddMealForm />
        </div>
      </div>
    </div>

    <div class=" card shadow-2xl shadow-slate-200 bg-base-100">
      <div class="card-body">
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
  </UserLayout>
</template>