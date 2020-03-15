import Vuelidate from 'vuelidate'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'

// scss style
import './assets/scss/index.scss'

Vue.config.productionTip = false

Vue.use(Vuelidate)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
