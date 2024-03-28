<script setup>
import { ErrorMessage, Field } from 'vee-validate'

defineProps({
  name: String,
  type: String,
  as: String,
  label: String,
  placeholder: String,
  readonly: Boolean
})
</script>

<template>
  <label class="label">
    <span class="label-text">{{ label }}</span>
  </label>
  <Field :name="name" :type="type" :as="as" :placeholder="placeholder || label"
         class="input input-bordered" autocomplete="false"
         :readonly="readonly"
  />
  <div class="label">
    <span class="label-text-alt text-error"><ErrorMessage :name="name" /></span>
  </div>
</template>