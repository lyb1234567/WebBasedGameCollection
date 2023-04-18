import { createRouter, createWebHistory } from 'vue-router';
// import Home from '../pages/Home.vue';
import RegisterPage from '../pages/RegisterPage.vue';
import LoginPage from '../pages/LoginPage.vue';
import UserInfoPage from '../pages/UserInfoPage.vue';
import HomePage from '../pages/HomePage.vue';
import communityPage from '../pages/communityPage.vue';
import InfoPage from '../pages/InfoPage.vue'
import addCollection from '../pages/addCollections.vue';
import PaymentPage from '../pages/PaymentPage.vue';
import publisherInfoPage from '../pages/publisherInfoPage.vue';
const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home,
  //   meta: {
  //     title: 'Board Game Saga | Home',
  //   },
  // },
  {
    path: '/register',
    name: 'RegisterPage',
    component: RegisterPage,
    meta: {
      title: 'Board Game Saga | Register',
    },
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage,
    meta: {
      title: 'Board Game Saga | Login',
    },
  },
  {
    path: '/userInfo',
    name: 'UserInfoPage',
    component: UserInfoPage,
    meta: {
      title: 'Board Game Saga | Your Info',
    },
  },
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
    meta: {
      title: 'Board Game Saga | Your Info',
    },
  },
  {
    path: '/logout',
    name: 'LogOut',
    component: HomePage,
    meta: {
      title: 'Board Game Saga | Your Info',
    },
  },
  {
    path: '/communityPage',
    name: 'communityPage',
    component: communityPage,
    meta: {
      title: 'Board Game Saga | Community Page',
    },
  },
  {
    path: '/infopage',
    name: 'InfoPage',
    component: InfoPage,
    meta: {
      title: 'Board Game Saga | Your Info',
    },
  },
  {
    path: '/addCollection',
    name: 'CollectionPage',
    component: addCollection,
    meta: {
      title: 'Board Game Saga | Your Info',
    },
  },
  {
    path: '/paymentPage',
    name: 'PaymentPage',
    component: PaymentPage,
    meta: {
      title: 'Board Game Saga | Payment',
    },
  },
  {
    path: '/publisherInfoPage',
    name: 'PublisherInfoPage',
    component: publisherInfoPage,
    meta: {
      title: 'Board Game Saga | Publisher Info',
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = `${to.meta.title}`;
  next();
});

export default router;
