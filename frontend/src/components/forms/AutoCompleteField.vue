<script setup>
import AutoComplete from 'primevue/autocomplete'
</script>

<template>
  <AutoComplete v-model="value" :suggestions="items" @complete="search" />
</template>

<style scoped>

</style>