import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../axios-api'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    trip_id: null,
  },
  mutations: {
    updateStorage (state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
    },
    getNewToken() {
      return new Promise((resolve, reject) =>{
        getAPI.post('/', {refresh: this.state.refreshToken}).then(response => {
          this.state.accessToken = response.data.tokens.access,
          this.state.refreshToken = response.data.tokens.refresh,
          resolve(response.data.tokens.access)
        }).catch((err) => {
          reject(err)
        });
      });
    }
  },
  getters: {
    loggedIn (state) {
      return state.accessToken != null
    }
  },
  actions: {
    userLogout (context) {
      if (context.getters.loggedIn) {
          context.commit('destroyToken')
      }
    },
    userLogin(context, usercredentials) {
      return new Promise((resolve, reject) => {
          getAPI.post('/login/', {
                  email: usercredentials.email,
                  password: usercredentials.password
              })
              .then(response => {
                  context.commit('updateStorage', {
                      access: response.data.tokens.access,
                      refresh: response.data.tokens.refresh
                  })
                  resolve()
              })
              .catch(err => {
                  reject(err)
              })
      })
    }
  },
  modules: {
  }
})