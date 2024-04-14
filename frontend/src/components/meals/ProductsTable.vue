<script setup>
import { client } from '@/axios.js'
import { computed, onMounted, ref, watch } from 'vue'

const props = defineProps({
  addedProduct: Object
})

watch(
  () => props.addedProduct,
  () => {
    getProducts()
  }
)

const products = ref([])
const totalPages = ref(1)
const currentPage = ref(1)

const pages = computed(() => {
  return Array.from({ length: totalPages.value }, (x, i) => i + 1)
})

async function getProducts(page = 1) {
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
  await getProducts()
})
</script>

<template>
  <div v-if="products.length">
    <div class="overflow-x-auto">
      <table class="table table-zebra">
        <thead>
        <tr>
          <th class="w-[40%]">Name</th>
          <th class="w-[10%]">Calories/100 g</th>
          <th class="w-[10%]">Weight, g</th>
          <th class="w-[20%]">Brand</th>
          <th class="w-[20%]">Store</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.name }}</td>
          <td>{{ product.calories }}</td>
          <td>{{ product.weight }}</td>
          <td>
            <span v-if="product.brand">{{ product.brand.name }}</span>
            <span v-else class="text-gray-400">—</span>
          </td>
          <td>
            <span v-if="product.store">{{ product.store.name }}</span>
            <span v-else class="text-gray-400">—</span>
          </td>
        </tr>
        </tbody>
      </table>
    </div>

    <div v-if="pages.length > 1" class="flex flex-row justify-end">
      <div class="join mt-8">
        <template v-for="page in pages" :key="page">
          <button @click="getProducts(page)" class="join-item btn"
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