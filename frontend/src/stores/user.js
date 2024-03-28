import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router/index.js'
import { useAuthStore } from '@/stores/auth.js'

export const useUserStore = defineStore('user', () => {
  const error = ref()

  async function register(form) {
    error.value = null

    await axios.post('/register', {
      email: form.email,
      password: form.password,
      first_name: form.first_name,
      last_name: form.last_name
    }).then(() => {
      router.push({ name: 'registered' })
    }).catch(handleErrors)
  }

  async function update(form) {
    await axios.patch('/users/me', {
      first_name: form.first_name,
      last_name: form.last_name
    }).then(({ data }) => {
      const authStore = useAuthStore()
      authStore.user = data
    }).catch(handleErrors)
  }


  async function handleErrors(error) {
    if (error.response.data.detail) {
      error.value = error.response.data.detail
    }
  }

  return { register, update, error }
})

