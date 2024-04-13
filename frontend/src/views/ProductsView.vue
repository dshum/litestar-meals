<script setup>
import { RouterLink } from 'vue-router'
import UserLayout from '@/components/layouts/UserLayout.vue'
import ProductsTable from '@/components/meals/ProductsTable.vue'
import ModalDialog from '@/components/ModalDialog.vue'
import AddMealForm from '@/components/AddMealForm.vue'
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
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 xl:grid-cols-4 gap-y-4 md:gap-x-4">
      <div class="lg:col-span-2 xl:col-span-3 card shadow-2xl shadow-slate-200 bg-base-100">
        <div class="card-body">
          <ProductsTable />
        </div>
      </div>

      <div class="card shadow-2xl shadow-slate-200 bg-base-100">
        <div class="card-body">
          <AddMealForm />
        </div>
      </div>
    </div>
  </UserLayout>
</template>