<script setup>
import { RouterLink } from 'vue-router'
import { Form } from 'vee-validate'
import * as yup from 'yup'
import GuestLayout from '@/components/layouts/GuestLayout.vue'
import InputField from '@/components/forms/InputField.vue'
import TextareaField from '@/components/forms/TextareaField.vue'

const onSubmit = async (values) => {
  console.log(values)
}

const schema = yup.object({
  email: yup.string().email().required(),
  name: yup.string().required(),
  message: yup.string().required()
})
</script>

<template>
  <GuestLayout>
    <div class="hero w-full">
      <div class="hero-content w-full flex-col lg:flex-row-reverse gap-x-[4vw]">
        <div class="flex-1 w-full text-center lg:text-left">
          <h1 class="mb-6 text-5xl font-bold">Feedback</h1>
          <p class="py-2">Here you can ask questions and leave suggestions.</p>
          <p class="py-2">
            <RouterLink :to="{name: 'home'}" class="underline">Return to the main page</RouterLink>
          </p>
        </div>

        <div class="flex-1 w-full card shadow-2xl shadow-sky-200 bg-base-100">
          <div class="card-body">
            <Form :validation-schema="schema" @submit="onSubmit">
              <div class="form-control">
                <InputField type="email" name="email" label="Email" />
              </div>

              <div class="form-control">
                <InputField type="text" name="name" label="Name" />
              </div>

              <div class="form-control">
                <TextareaField name="message" label="Message" rows="10" />
              </div>

              <div class="form-control max-w-xs mt-6">
                <button class="btn btn-primary">Submit</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </GuestLayout>
</template>