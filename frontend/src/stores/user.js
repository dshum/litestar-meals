import { ref } from 'vue'
import { defineStore } from 'pinia'
import router from '@/router/index.js'
import { client, sleep } from '@/axios.js'
import { useAuthStore } from '@/stores/auth.js'

// client.interceptors.response.use(async (response) => {
//   if (process.env.NODE_ENV === 'development') {
//     await sleep();
//   }
//   return response.data;
// });

export const useUserStore = defineStore('user', () => {
  const error = ref()
  const loading = ref(false)

  async function register(form) {
    error.value = null
    loading.value = true

    await client.post('/register', {
      email: form.email,
      password: form.password,
      first_name: form.first_name,
      last_name: form.last_name
    }).then(() => {
      router.push({ name: 'registered' })
    }).catch(handleErrors).finally(() => {
      loading.value = false
    })
  }

  async function update(form) {
    if (loading.value) {
      return
    }
    loading.value = true

    await client.patch('/users/me', {
      first_name: form.first_name,
      last_name: form.last_name
    }).then(({ data }) => {
      const authStore = useAuthStore()
      authStore.user = data
    }).catch(handleErrors).finally(() => {
      return new Promise((resolve) => setTimeout(resolve, 400))
    }).then(() => {
      loading.value = false
    })
  }


  async function handleErrors(error) {
    if (error.response.data.detail) {
      error.value = error.response.data.detail
    }
  }

  return { register, update, loading, error }
})

