import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { client, isBlocked } from '@/axios.js'
import router from '@/router/index.js'
import { getCookie } from '@/utils/cookie.js'

export const useAuthStore = defineStore('auth', () => {
  const csrf_cookie_set = ref(false)
  const user = ref()
  const userName = computed(() => {
    return user.value ? user.value.first_name + ' ' + user.value.last_name : ''
  })
  const avatarName = computed(() => {
    return user.value ? user.value.first_name[0] + user.value.last_name[0] : ''
  })
  const errorMessage = ref()
  const returnUrl = ref()
  const logging = computed(() => {
    return isBlocked('/login')
  })

  async function setCSRFCookie() {
    if (getCookie('csrftoken')) {
      csrf_cookie_set.value = true
    } else {
      await client.get('/csrf-cookie').then(() => {
        csrf_cookie_set.value = true
      })
    }
  }

  async function getUser() {
    await client.get('/users/me').then(({ data }) => {
      user.value = data
    }).catch(() => {
    })
  }

  async function login(form) {
    errorMessage.value = null

    await client.post('/login', {
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
    await client.post('/logout').then(() => {
      user.value = null
      router.push({ name: 'login' })
    }).catch(() => {
    })
  }

  async function handleErrors(error) {
    if (error.response && error.response.data.detail) {
      errorMessage.value = error.response.data.detail
    } else {
      errorMessage.value = 'Something wrong happened'
    }
  }

  return {
    setCSRFCookie,
    getUser,
    login,
    logout,
    csrf_cookie_set,
    user,
    userName,
    avatarName,
    logging,
    errorMessage,
    returnUrl
  }
})

