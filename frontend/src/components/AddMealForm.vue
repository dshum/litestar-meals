<script setup>
import { onMounted, ref } from 'vue'
import { Form } from 'vee-validate'
import * as yup from 'yup'
import InputField from '@/components/forms/InputField.vue'
import { client } from '@/axios.js'
import SelectField from '@/components/forms/SelectField.vue'

const loading = ref(false)
const schema = yup.object({
  name: yup.string().required('Name is required'),
  weight: yup.number().required('Weight is required')
    .moreThan(0, 'Weight must be greater than 0')
    .max(10000, 'Weight may not be greater than 10000'),
  calories: yup.number().required('Calories content is required')
    .moreThan(0, 'Calories must be greater than 0')
    .max(10000, 'Calories may not be greater than 10000'),
  brand_name: yup.string(),
  store_name: yup.string()
})
const error = ref()

const brands = ref([])
const stores = ref([])

const getBrands = async () => {
  await client.get('/brands', {
    params: { pageSize: 100 }
  }).then(({ data: { items } }) => {
    brands.value = items
  })
}

const getStores = async () => {
  await client.get('/stores', {
    params: { pageSize: 100 }
  }).then(({ data: { items } }) => {
    stores.value = items
  })
}

const onSubmit = async (form) => {
  error.value = null

  await client.post('/products', form).then(() => {

  }).catch(({ response }) => {
    if (response.data.detail) {
      error.value = response.data.detail
    }
  })
}

onMounted(() => {
  getBrands()
  getStores()
})
</script>

<template>
  <ul v-if="error" class="text-error">
    <li>{{ error }}</li>
  </ul>

  <Form :validation-schema="schema" @submit="onSubmit">
    <div class="grid grid-cols-1 gap-y-4 md:gap-x-4">
      <div class="form-control">
        <InputField type="text" name="name" label="Name" placeholder="Meal name" />
      </div>

      <div class="form-control">
        <InputField type="number" name="weight" label="Weight" placeholder="Weight in grams"
                    min="0" max="10000" step="1" />
      </div>

      <div class="form-control">
        <InputField type="number" name="calories" label="Calories" placeholder="Calories per 100 g"
                    min="0" max="10000" step="1" />
      </div>

      <div class="form-control">
        <SelectField name="brand" label="Brand">
          <option value="">Select brand</option>
          <option v-for="brand in brands" :value="brand.id">{{ brand.name }}</option>
        </SelectField>
      </div>

      <div class="form-control">
        <SelectField name="store" label="Store" placeholder="Select store">
          <option value="">Select store</option>
          <option v-for="store in stores" :value="store.id">{{ store.name }}</option>
        </SelectField>
      </div>

      <div class="form-control mt-2">
        <button class="btn btn-primary">
          <span v-if="loading" class="loading loading-ring loading-lg"></span>
          <span v-else>Save</span>
        </button>
      </div>
    </div>
  </Form>
</template>