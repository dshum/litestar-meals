<script setup>
import GuestLayout from '@/components/layouts/GuestLayout.vue'
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth.js'


const authStore = useAuthStore()
const form = ref({
  email: '',
  password: '',
  first_name: '',
  last_name: ''
})
</script>

<template>
  <GuestLayout>
    <div class="hero">
      <div class="hero-content flex-col lg:flex-row-reverse gap-x-[4vw]">
        <div class="min-w-96 text-center lg:text-left">
          <h1 class="mb-6 text-5xl font-bold">Join now!</h1>
          <p class="py-2">Register to get an access to your food diary.</p>
          <p class="py-2">Already have an account?
            <RouterLink to="/login" class="underline">Log In</RouterLink>
          </p>
        </div>

        <div class="card min-w-96 max-w-sm shadow-2xl shadow-sky-200 bg-base-100">
          <form class="card-body" @submit.prevent="authStore.register(form)">
            <div class="form-control">
              <label class="label">
                <span class="label-text">Email</span>
              </label>
              <input v-model="form.email" type="email"
                     placeholder="email" class="input input-bordered"
                     required autocomplete="false" />
            </div>

            <div class="form-control">
              <label class="label">
                <span class="label-text">Password</span>
              </label>
              <input v-model="form.password" type="password"
                     placeholder="password" class="input input-bordered"
                     required autocomplete="false" />
            </div>

            <div class="form-control">
              <label class="label">
                <span class="label-text">First name</span>
              </label>
              <input v-model="form.first_name" type="text"
                     placeholder="first name" class="input input-bordered"
                     required />
            </div>

            <div class="form-control">
              <label class="label">
                <span class="label-text">Last name</span>
              </label>
              <input v-model="form.last_name" type="text"
                     placeholder="last name" class="input input-bordered"
                     required />
            </div>

            <div class="form-control mt-6">
              <button class="btn btn-primary">Register</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </GuestLayout>
</template>