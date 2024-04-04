<script setup>
import { computed, ref } from 'vue'
import { ErrorMessage, Field } from 'vee-validate'

const props = defineProps({
  name: String,
  label: String,
  values: Array
})
const focus = ref(false)
const searchTerm = ref('')
const selectedValue = ref('')
const searchValues = computed(() => {
  if (searchTerm.value === '' && !focus.value) {
    return []
  }

  let matches = 0

  return props.values.filter(value => {
    if (
      (searchTerm.value === ''
        || value.toLowerCase().includes(searchTerm.value.toLowerCase()))
      && matches < 10
    ) {
      matches++
      return value
    }
  })
})

function selectValue(value) {
  selectedValue.value = value
  searchTerm.value = ''
}

function selectSelfValue() {
  selectedValue.value = searchTerm.value
  searchTerm.value = ''
}

function onFocus() {
  focus.value = true
}

function onBlur() {
  focus.value = false
}
</script>

<template>
  <label class="label">
    <span class="label-text">{{ label }}</span>
  </label>

  <Field :name="name" v-bind="$attrs" v-model="searchTerm"
         @click="onFocus" v-click-outside="onBlur" @keydown.enter="selectSelfValue"
         class="input input-bordered" />

  <div v-if="selectedValue" class="label">
    <span class="label-text">You selected: {{ selectedValue }}</span>
  </div>

  <ErrorMessage :name="name" v-slot="errorMessage">
    <div class="label mt-1 py-0">
      <span class="label-text-alt text-error">{{ errorMessage.message }}</span>
    </div>
  </ErrorMessage>

  <ul v-if="searchValues.length" class="w-52 bg-base-100 rounded-box shadow menu p-2">
    <li class="menu-title">
      Showing {{ searchValues.length }} of {{ values.length }} results
    </li>
    <li v-for="value in searchValues"><a @click="selectValue(value)">{{ value }}</a></li>
  </ul>
</template>

<style scoped>

</style>