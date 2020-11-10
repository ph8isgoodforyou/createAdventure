import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login'
import Trips from '../views/Trips'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
        path: '/',
        name: 'home',
        component: Home,
        meta: {
            requiresLogin: true
          }
        },
        {
        path: '/login',
        name: 'login',
        component: Login,
        },
        // {
        // path: '/logout',
        // name: 'logout',
        // component: Logout,
        // },
        {
        path: '/trips',
        name: 'trips',
        component: Trips,
        }
    ]
})
