import {createRouter , createWebHistory } from 'vue-router'
import Home from  '../pages/Home.vue'
import RegisterPage from '../pages/RegisterPage.vue'
import LoginPage from '../pages/LoginPage.vue'
import UserInfoPage from '../pages/UserInfoPage.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            title : 'Board Game Saga | Home',
        }

    },
    {
        path: '/register',
        name: 'RegisterPage',
        component: RegisterPage,
        meta: {
            title : 'Board Game Saga | Register',
        }
     },
     {
        path: '/login',
        name: 'LoginPage',
        component: LoginPage,
        meta: {
            title : 'Board Game Saga | Login',
        }
     },
     {
        path: '/userInfo',
        name: 'UserInfoPage',
        component: UserInfoPage,
        meta: {
            title : 'Board Game Saga | Your Info',
        }
     },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from ,next) => {
    document.title = `${to.meta.title}`;
    next()
})

export default router