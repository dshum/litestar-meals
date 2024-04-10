<script setup>
import { ref } from 'vue'
import { Form } from 'vee-validate'
import * as yup from 'yup'
import InputField from '@/components/forms/InputField.vue'
import { client } from '@/axios.js'
import ComboboxField from '@/components/forms/ComboboxField.vue'

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

const onSubmit = async (form) => {
  error.value = null

  await client.post('/products', form).then(({ data }) => {

  }).catch(({ response }) => {
    if (response.data.detail) {
      error.value = response.data.detail
    }
  })
}
</script>

<template>
  <ul v-if="error" class="text-error">
    <li>{{ error }}</li>
  </ul>

  <Form :validation-schema="schema" @submit="onSubmit">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-y-4 md:gap-x-4">
      <div class="form-control md:col-span-2">
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
        <label class="label">
          <span class="label-text">Brand</span>
        </label>

        <ComboboxField />
      </div>

      <div class="form-control">
        <InputField type="text" name="store_name" label="Store" placeholder="Store name" />
      </div>

      <div class="form-control col-span-2 mt-2">
        <button class="btn btn-primary">
          <span v-if="loading" class="loading loading-ring loading-lg"></span>
          <span v-else>Save</span>
        </button>
      </div>
    </div>
  </Form>
</template>