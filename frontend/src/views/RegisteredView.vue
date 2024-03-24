<script setup>
import GuestLayout from '@/components/layouts/GuestLayout.vue'
import { RouterLink } from 'vue-router'
</script>

<template>
  <GuestLayout>
    <div class="hero">
      <div class="hero-content flex-col">
        <p>You have successfully registered!</p>
        <p>An email has been sent to you with a link to verify your account.</p>
        <p><RouterLink :to="{name: 'login'}" class="btn btn-info">Log In</RouterLink></p>
      </div>
    </div>
  </GuestLayout>
</template>