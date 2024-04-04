<script setup>
import { ref } from 'vue'
import { Form } from 'vee-validate'
import * as yup from 'yup'
import InputField from '@/components/forms/InputField.vue'
import AutoComplete from 'primevue/autocomplete'

const loading = ref(false)
const selectedBrand = ref()

const schema = yup.object({
  name: yup.string().required('Name is required'),
  weight: yup.number().required('Weight is required')
    .moreThan(0, 'Weight must be greater than 0')
    .max(10000, 'Weight may not be greater than 10000'),
  calories: yup.number().required('Calories content is required')
    .moreThan(0, 'Calories must be greater than 0')
    .max(10000, 'Calories may not be greater than 10000'),
  brand: yup.string()
})

const error = ref()

const brands = [
  'Creative Kitchen',
  'Danissimo',
  'Miratorg'
]
const stores = [
  'Ozon',
  'Vkusvill',
  'Various'
]

async function register(form) {
  console.log(form)
}

async function onSelectBrand() {
  console.log(selectedBrand.value)
}
</script>

<template>
  <ul v-if="error" class="text-error">
    <li>{{ error }}</li>
  </ul>

  <Form :validation-schema="schema" @submit="register">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-4">
      <div class="form-control md:col-span-2 mb-3">
        <InputField type="text" name="name" label="Name" placeholder="Meal name" />
      </div>

      <div class="form-control mb-3">
        <InputField type="number" name="weight" label="Weight" placeholder="Weight in grams"
                    min="0" max="10000" step="1" />
      </div>

      <div class="form-control mb-3">
        <InputField type="number" name="calories" label="Calories" placeholder="Calories per 100 g"
                    min="0" max="10000" step="1" />
      </div>

      <div class="form-control mb-3">
        <label class="label">
          <span class="label-text">Brand</span>
        </label>
        <AutoComplete v-model="selectedBrand" :suggestions="brands" @complete="onSelectBrand"
                      class="input input-bordered" />
      </div>
    </div>

    <div class="form-control max-w-xs mt-3">
      <button class="btn btn-primary">
        <span v-if="loading" class="loading loading-ring loading-lg"></span>
        <span v-else>Save</span>
      </button>
    </div>
  </Form>
</template>

<style scoped>

</style>