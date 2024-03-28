import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router/index.js'

export const useUserStore = defineStore('user', () => {
  const error = ref()

  async function register(form) {
    errors.value = {}

    await axios.post('/register', {
      email: form.email,
      password: form.password,
      first_name: form.first_name,
      last_name: form.last_name
    }).then(() => {
      router.push({ name: 'registered' })
    }).catch(handleErrors)
  }


  async function handleErrors(error) {
    if (error.response.data.detail) {
      error.value = error.response.data.detail
    }
  }

  return { register, error }
})

