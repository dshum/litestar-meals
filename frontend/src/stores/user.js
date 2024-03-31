import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import router from '@/router/index.js'
import { client, isBlocked } from '@/axios.js'
import { useAuthStore } from '@/stores/auth.js'
import { CanceledError } from 'axios'

export const useUserStore = defineStore('user', () => {
  const error = ref()
  const registering = computed(() => {
    return isBlocked('/register')
  })
  const updating = computed(() => {
    return isBlocked('/users/me')
  })

  async function register(form) {
    error.value = null

    await client.post('/register', form).then(() => {
      router.push({ name: 'registered' })
    }).catch(handleErrors)
  }

  async function update(form) {
    error.value = null

    await client.patch('/users/me', form).then(({ data }) => {
      const authStore = useAuthStore()
      authStore.user = data
    }).catch(handleErrors)
  }


  async function handleErrors(error) {
    if (error instanceof CanceledError) {

    } else if (error.response.data.detail) {
      error.value = error.response.data.detail
    }
  }

  return { register, update, registering, updating, error }
})

