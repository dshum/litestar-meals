<script setup>
import { ErrorMessage, Field } from 'vee-validate'

defineProps({
  name: String,
  label: String,
  placeholder: String,
  rows: String,
  cols: String
})
</script>

<template>
  <label class="label">
    <span class="label-text">{{ label }}</span>
  </label>
  <Field :name="name" as="textarea" :placeholder="placeholder || label"
         class="textarea textarea-md textarea-bordered"
         :rows="rows" :cols="cols"
  />
  <div class="label">
    <span class="label-text-alt text-error"><ErrorMessage :name="name" /></span>
  </div>
</template>