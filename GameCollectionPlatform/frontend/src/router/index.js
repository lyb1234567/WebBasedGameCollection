import {createRouter , createWebHistory } from 'vue-router'
import Home from  '../pages/Home.vue'
import RegisterPage from '../pages/RegisterPage.vue'
import LoginPage from '../pages/LoginPage.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home

    },
    {
        path: '/register',
        name: 'RegisterPage',
        component: RegisterPage
     },
     {
        path: '/login',
        name: 'LoginPage',
        component: LoginPage
     }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router