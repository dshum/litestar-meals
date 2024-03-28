import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router/index.js'

export const useAuthStore = defineStore('auth', () => {
  const user = ref()
  const avatarName = computed(() => {
    return user.value.first_name[0]
  })
  const error = ref()
  const returnUrl = ref(null)

  async function getUser() {
    await axios.get('/users/me').then(({ data }) => {
      user.value = data
    }).catch(() => {
    })
  }

  async function login(form) {
    errors.value = {}

    await axios.post('/login', {
      email: form.email,
      password: form.password
    }).then(({ data }) => {
      user.value = data
      if (returnUrl.value) {
        router.push(returnUrl.value)
        returnUrl.value = null
      } else {
        router.push({ name: 'home' })
      }
    }).catch(handleErrors)
  }

  async function logout() {
    await axios.post('/logout').then(() => {
      user.value = null
      router.push({ name: 'login' })
    }).catch(() => {
    })
  }

  async function handleErrors(error) {
    if (error.response.data.detail) {
      error.value = error.response.data.detail
    }
  }

  return { user, avatarName, getUser, login, logout, error, returnUrl }
})

