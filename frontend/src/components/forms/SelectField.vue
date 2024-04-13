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

  <Field as="select" v-slot="{ value }" :name="name" v-bind="$attrs" class="select select-bordered">
    <slot />
  </Field>

  <ErrorMessage :name="name" v-slot="errorMessage">
    <div class="label mt-1 py-0">
      <span class="label-text-alt text-error">{{ errorMessage.message }}</span>
    </div>
  </ErrorMessage>
</template>

<style scoped>

</style>