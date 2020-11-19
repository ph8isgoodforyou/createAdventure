import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Contact from '../views/Contact.vue'
import Trips from '../views/Trips.vue'
import CreateTrip from '../views/CreateTrip.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import CreateCity from '../views/CreateCity.vue'
import CreateCountry from '../views/CreateCountry.vue'
import CreatePointOfInterest from '../views/CreatePointOfInterest.vue'
import TripView from '../views/TripView.vue'
import UpdatePointOfInterest from '../views/UpdatePointOfInterest.vue'
import UpdateCity from '../views/UpdateCity.vue'
import UpdateTrip from '../views/UpdateTrip.vue'
import UpdateCountry from '../views/UpdateCountry.vue'
import Logout from '../views/Logout.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about/',
    name: 'About',
    component: About
  },
  {
    path: '/contact/',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/trips/',
    name: 'Trips',
    component: Trips,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/TripView/:id',
    name: 'TripView',
    component: TripView,
    meta: {
      requiresLogin: true,
    }
  },
  {
    path: '/create/trip/',
    name: 'CreateTrip',
    component: CreateTrip,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/update/trip/:id',
    name: 'UpdateTrip',
    component: UpdateTrip,
    meta: {
      requiresLogin: true
    }
  },
    {
    path: '/trip/:id/create/country/',
    name: 'CreateCountry',
    component: CreateCountry,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/trip/:id/update/country/:id',
    name: 'UpdateCountry',
    component: UpdateCountry,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/trip/:id/country/:id/create/city',
    name: 'CreateCity',
    component: CreateCity,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/trip/:id/country/:id/update/city/:id',
    name: 'UpdateCity',
    component: UpdateCity,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/trip/:id/country/:id/city/:id/create/pointofinterest/',
    name: 'CreatePointOfInterest',
    component: CreatePointOfInterest,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/trip/:id/country/:id/city/:id/update/pointofinterest/:id',
    name: 'UpdatePointOfInterest',
    component: UpdatePointOfInterest,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login,
    meta: {
      requiresVisitor: true
    }
  },
  {
    path: '/logout/',
    name: 'Logout',
    component: Logout,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/register/',
    name: 'Register',
    component: Register,
    meta: {
      requiresVisitor: true
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
