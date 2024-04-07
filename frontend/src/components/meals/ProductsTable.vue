<script setup>
import { client } from '@/axios.js'
import { computed, onMounted, ref } from 'vue'


const products = ref([])
const totalPages = ref(1)
const currentPage = ref(1)
const pages = computed(() => {
  return Array.from({ length: totalPages.value }, (x, i) => i + 1)
})

async function getItems(page = 1) {
  await client.get('/products', {
    params: {
      page: page,
      pageSize: 10
    }
  }).then(({ data: { items, total_pages, current_page } }) => {
    products.value = items
    totalPages.value = total_pages
    currentPage.value = current_page
  }).catch(() => {
  })
}

onMounted(async () => {
  await getItems()
})
</script>

<template>
  <div v-if="products.length">
    <div class="overflow-x-auto">
      <table class="table table-zebra">
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
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.name }}</td>
          <td>{{ product.calories }}</td>
          <td>{{ product.weight }}</td>
          <td>{{ product.brand?.name || '—' }}</td>
          <td>{{ product.store?.name || '—' }}</td>
        </tr>
        </tbody>
      </table>
    </div>

    <div v-if="pages.length > 1" class="flex flex-row justify-end">
      <div class="join mt-8">
        <template v-for="page in pages" :key="page">
          <button @click="getItems(page)" class="join-item btn"
                  :class="{'btn-active': currentPage === page}">
            {{ page }}
          </button>
        </template>
      </div>
    </div>
  </div>

  <div v-else>
    No products added yet.
  </div>
</template>

<style scoped>

</style>