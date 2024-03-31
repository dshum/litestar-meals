<template>
  <UserLayout>
    <div class="breadcrumbs mb-4">
      <ul>
        <li>
          <RouterLink :to="{name: 'home'}">Home</RouterLink>
        </li>
        <li>Products</li>
      </ul>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="w-full col-span-2">
        <div class="card shadow-2xl shadow-lime-100 bg-base-100">
          <div class="card-body">
            <h2 class="text-2xl">Ozon</h2>
          </div>
        </div>
      </div>

      <div class="w-full col-span-1">
        <div class="card shadow-2xl shadow-orange-100 bg-base-100">
          <div class="card-body">
          </div>
        </div>
      </div>
    </div>
  </UserLayout>
</template>
<script setup>
import UserLayout from '@/components/layouts/UserLayout.vue'
import { RouterLink } from 'vue-router'
</script>