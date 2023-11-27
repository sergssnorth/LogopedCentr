import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Specialists from '../views/Specialists.vue'
import Record from '../views/Search.vue'
import MyAccount from '../views/MyAccount.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
