<script setup>
import { RouterLink } from 'vue-router'
import { Form } from 'vee-validate'
import * as yup from 'yup'
import { useUserStore } from '@/stores/user.js'
import GuestLayout from '@/components/layouts/GuestLayout.vue'
import InputField from '@/components/forms/InputField.vue'

const userStore = useUserStore()
const schema = yup.object({
  email: yup.string().email('Email must a valid email').required('Email is required'),
  password: yup.string().required('Password is required')
    .min(6, 'Password must be at least 6 characters'),
  password_confirmation: yup.string().required('Password confirmation is required')
    .oneOf([yup.ref('password')], 'Passwords do not match'),
  first_name: yup.string().required('First name is required')
    .min(1, 'First name must be at least 1 character'),
  last_name: yup.string().required('Last name is required')
    .min(1, 'Last name must be at least 1 character')
})
</script>

<template>
  <GuestLayout>
    <div class="hero w-full">
      <div class="hero-content w-full flex-col lg:flex-row-reverse gap-x-[4vw]">
        <div class="flex-1 w-full text-center lg:text-left">
          <h1 class="mb-6 text-5xl font-bold">Join now!</h1>
          <p class="py-2">Register to get an access to your food diary.</p>
          <p class="py-2">Already have an account?
            <RouterLink to="/login" class="underline">Log In</RouterLink>
          </p>
        </div>

        <div class="flex-1 w-full card shadow-2xl shadow-sky-200 bg-base-100">
          <div class="card-body">
            <ul v-if="userStore.error" class="text-error">
              <li>{{ userStore.error }}</li>
            </ul>

            <Form :validation-schema="schema" @submit="userStore.register">
              <div class="form-control">
                <InputField type="email" name="email" label="Email" />
              </div>

              <div class="form-control">
                <InputField type="password" name="password" label="Password" />
              </div>

              <div class="form-control">
                <InputField type="password" name="password_confirmation" label="Password confirmation" />
              </div>

              <div class="form-control">
                <InputField type="text" name="first_name" label="First name" />
              </div>

              <div class="form-control">
                <InputField type="text" name="last_name" label="Last name" />
              </div>

              <div class="form-control mt-6">
                <button class="btn btn-primary">Register</button>
              </div>
            </Form>
          </div>
        </div>
      </div>
    </div>
  </GuestLayout>
</template>