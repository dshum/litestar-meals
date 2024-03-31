<script setup>
import { ErrorMessage, Field } from 'vee-validate'

defineOptions({
  inheritAttrs: false
})

defineProps({
  name: String,
  label: String
})
</script>

<template>
  <label class="label">
    <span class="label-text">{{ label }}</span>
  </label>
  <Field v-bind="$attrs" :name="name" class="input input-bordered" autocomplete="false" />
  <div class="label">
    <span class="label-text-alt text-error"><ErrorMessage :name="name" /></span>
  </div>
</template>