<template>
  <UserLayout>
    <div class="breadcrumbs mb-4">
      <ul>
        <li>Home</li>
      </ul>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="w-full lg:col-span-2">
        <RecentMeals />
      </div>
      <div class="w-full lg:col-span-1 order-first lg:order-last">
        <AddMeal />
      </div>
    </div>
  </UserLayout>
</template>

<script setup>
import UserLayout from '@/components/layouts/UserLayout.vue'
import RecentMeals from '@/components/meals/RecentMeals.vue'
import AddMeal from '@/components/meals/AddMeal.vue'
</script>