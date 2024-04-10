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

      <ModalDialog>
        <AddMealForm />
      </ModalDialog>
    </div>

    <div class="card shadow-2xl shadow-slate-200 bg-base-100">
      <div class="card-body">
        <ProductsTable />
      </div>
    </div>
  </UserLayout>
</template>