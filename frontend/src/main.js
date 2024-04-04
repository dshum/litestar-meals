import './style.css'
import './axios'

import { createApp, markRaw } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'

import App from './App.vue'
import router from './router'

const pinia = createPinia()
pinia.use(({ store }) => {
  store.router = markRaw(router)
})

const app = createApp(App)
app.use(pinia)
app.use(router)
app.use(PrimeVue)

app.mount('#app')
