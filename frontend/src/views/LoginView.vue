<script setup>
import { RouterLink } from 'vue-router'
import { Form } from 'vee-validate'
import * as yup from 'yup'
import { useAuthStore } from '@/stores/auth.js'
import GuestLayout from '@/components/layouts/GuestLayout.vue'
import InputField from '@/components/forms/InputField.vue'

const authStore = useAuthStore()
const schema = yup.object({
  email: yup.string().email('Email must a valid email').required('Email is required'),
  password: yup.string().required('Password is required')
})
</script>

<template>
  <GuestLayout>
    <div class="hero w-full">
      <div class="hero-content w-full flex flex-col lg:flex-row-reverse justify-center gap-x-[4vw]">
        <div class="text-center lg:text-left">
          <h1 class="mb-6 text-5xl font-bold">Login now!</h1>
          <p class="py-2">Log in to access your food diary.</p>
          <p class="py-2">Haven't registered yet?
            <RouterLink to="/register" class="underline">Create an account</RouterLink>
          </p>
        </div>

        <div class="shrink-0 w-full max-w-sm card shadow-2xl shadow-sky-200 bg-base-100">
          <div class="card-body">
            <ul v-if="authStore.errorMessage" class="text-error">
              <li>{{ authStore.errorMessage }}</li>
            </ul>

            <Form :validation-schema="schema" @submit="authStore.login">
              <div class="grid grid-cols-1 gap-y-4">
                <div class="form-control">
                  <InputField type="email" name="email" label="Email"
                              placeholder="Email"
                              autocomplete="true" />
                </div>

                <div class="form-control">
                  <InputField type="password" name="password" label="Password"
                              placeholder="Password"
                              autocomplete="true" />
                </div>

                <div class="form-control mt-4">
                  <button class="btn btn-primary max-w-xs">
                    <span v-if="authStore.logging" class="loading loading-ring loading-lg"></span>
                    <span v-else>Login</span>
                  </button>
                </div>
              </div>
            </Form>
          </div>
        </div>
      </div>
    </div>
  </GuestLayout>
</template>