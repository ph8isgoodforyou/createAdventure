import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import IdleVue from 'idle-vue'

const eventsHub = new Vue()

Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 200000
})

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'Login' })
    } else {
      next()
    }
  } 
  else if (to.matched.some(record => record.meta.requiresVisitor)) {
    if (store.getters.loggedIn) {
      next({ path: '/' })
    } else {
      next()
    }
  }
  else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
