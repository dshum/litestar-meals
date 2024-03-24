import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router/index.js'

export const useAuthStore = defineStore('auth', () => {
  const user = ref()

  async function register(form) {
    await axios.post('/register', {
      email: form.email,
      password: form.password,
      first_name: form.first_name,
      last_name: form.last_name
    })
    await router.push({ name: 'registered' })
  }

  async function getUser() {
    await axios.get('/users/me').then(({ data }) => {
      user.value = data
    }).catch(() => {
    })
  }

  async function login(form) {
    await axios.post('/login', {
      email: form.email,
      password: form.password
    }).then(({ data }) => {
      router.push({ name: 'home' })
    }).catch(() => {
    })
  }

  async function logout() {
    await axios.post('/logout').then(({ data }) => {
      user.value = null
      router.push({ name: 'login' })
    }).catch(() => {
    })
  }


  return { user, register, getUser, login, logout }
})

