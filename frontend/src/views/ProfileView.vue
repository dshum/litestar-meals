<script setup>
import { RouterLink } from 'vue-router'
import { Form } from 'vee-validate'
import * as yup from 'yup'
import { useUserStore } from '@/stores/user.js'
import { useAuthStore } from '@/stores/auth.js'
import UserLayout from '@/components/layouts/UserLayout.vue'
import InputField from '@/components/forms/InputField.vue'

const authStore = useAuthStore()
const userStore = useUserStore()
const schema = yup.object({
  first_name: yup.string().required('First name is required')
    .min(1, 'First name must be at least 1 character'),
  last_name: yup.string().required('Last name is required')
    .min(1, 'Last name must be at least 1 character')
})
</script>

<template>
  <UserLayout>
    <div class="breadcrumbs mb-4">
      <ul>
        <li>
          <RouterLink :to="{name: 'home'}">Home</RouterLink>
        </li>
        <li>Profile</li>
      </ul>
    </div>

    <div class="lg:max-w-xl card shadow-2xl shadow-sky-200 bg-base-100">
      <div class="card-body">
        <ul v-if="userStore.error" class="text-error">
          <li>{{ userStore.error }}</li>
        </ul>

        <Form :validation-schema="schema" :initial-values="authStore.user" @submit="userStore.update">
          <div class="form-control">
            <InputField type="email" name="email" label="Email" :readonly="true" />
          </div>

          <div class="form-control">
            <InputField type="text" name="first_name" label="First name" />
          </div>

          <div class="form-control">
            <InputField type="text" name="last_name" label="Last name" />
          </div>

          <div class="form-control mt-4">
            <button class="btn btn-primary max-w-xs">
              <span v-if="userStore.updating" class="loading loading-ring loading-lg"></span>
              <span v-else>Save</span>
            </button>
          </div>
        </Form>
      </div>
    </div>
  </UserLayout>
</template>