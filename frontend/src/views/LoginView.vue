<script setup>
import GuestLayout from '@/components/layouts/GuestLayout.vue'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth.js'
import Alert from '@/components/Alert.vue'

const authStore = useAuthStore()
const form = ref({
  email: '',
  password: ''
})
let message = ''
</script>

<template>
  <GuestLayout>
    <div class="hero">
      <div class="hero-content flex-col lg:flex-row-reverse gap-x-[4vw]">
        <div class="min-w-96 text-center lg:text-left">
          <h1 class="mb-6 text-5xl font-bold">Login now!</h1>
          <p class="py-2">Log in to access your food diary.</p>
          <p class="py-2">Haven't registered yet?
            <RouterLink to="/register" class="underline">Create an account</RouterLink>
          </p>
        </div>

        <div class="card min-w-96 max-w-sm shadow-2xl shadow-sky-200 bg-base-100">
          <Alert class="alert-warning" :open="false">{{ message }}</Alert>

          <form class="card-body" @submit.prevent="authStore.login(form)">
            <div class="form-control">
              <label class="label">
                <span class="label-text">Email</span>
              </label>
              <input type="email" v-model="form.email"
                     placeholder="email" class="input input-bordered" required
                     autocomplete="true" />
            </div>

            <div class="form-control">
              <label class="label">
                <span class="label-text">Password</span>
              </label>
              <input type="password" v-model="form.password"
                     placeholder="password" class="input input-bordered" required
                     autocomplete="true" />
              <label class="label">
                <a href="#" class="label-text-alt link link-hover">Forgot password?</a>
              </label>
            </div>

            <div class="form-control mt-6">
              <button class="btn btn-primary">Login</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </GuestLayout>
</template>