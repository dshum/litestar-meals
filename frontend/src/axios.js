import axios from 'axios'
import { ref } from 'vue'

function sleep(ms = 400) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}

function isPostMethod(method) {
  return ['post', 'put', 'patch', 'delete'].includes(method)
}

function isBlocked(url) {
  return blockRequests.value[url]
}

const client = axios.create({
  baseURL: 'http://localhost:8013',
  withCredentials: true,
  withXSRFToken: true,
  xsrfHeaderName: 'x-csrftoken',
  xsrfCookieName: 'csrftoken'
})

const blockRequests = ref([])

client.interceptors.request.use(function(config) {
  const controller = new AbortController()

  if (isPostMethod(config.method)) {
    if (blockRequests.value[config.url]) {
      controller.abort()
    } else {
      blockRequests.value[config.url] = true
    }
  }

  return {
    ...config,
    signal: controller.signal
  }
}, function(error) {
  return Promise.reject(error)
})

client.interceptors.response.use(async (response) => {
  if (isPostMethod(response.config.method) && !response.config.signal.aborted) {
    if (process.env.NODE_ENV === 'development') {
      await sleep()
    }
    blockRequests.value[response.config.url] = false
  }
  return response
})

export { client, isBlocked }