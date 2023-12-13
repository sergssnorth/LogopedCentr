import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import AboutUs from '../views/AboutUs.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Specialists from '../views/Specialists.vue'
import Record from '../views/Record.vue'
import MyRecords from '../views/MyRecords.vue'
import Directions from '../views/Directions.vue'
import DirectionSpecialists from '../views/DirectionSpecialists.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about-us',
    name: 'AboutUs',
    component: AboutUs
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount
  },
  {
    path: '/specialists',
    name: 'Specialists',
    component: Specialists
  },
  {
    path: '/records',
    name: 'Record',
    component: Record
  },
  {
    path: '/my-records',
    name: 'MyRecords',
    component: MyRecords
  },
  {
    path: '/directions',
    name: 'Directions',
    component: Directions
  },
  {
    path: '/directions/:direction_slug',
    name: 'DirectionSpecialists',
    component: DirectionSpecialists
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
