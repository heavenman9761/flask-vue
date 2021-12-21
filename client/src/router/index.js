import Vue from 'vue';
import VueRouter from 'vue-router';

import Ping from '@/views/Ping.vue';
import Books from '@/views/Books.vue';
import Jumbotron from '@/views/Jumbotron.vue';
import Login from '@/views/Login.vue';
import UserRegi from '@/views/UserRegi.vue';
import Profile from '@/views/Profile.vue';
import DayMaeChul from '@/views/DateMaeChul.vue'
import VueChartJs from '@/views/VueChartJs.vue'

// import store from '../store';

Vue.use(VueRouter);
// const rejectAuthUser = (to, from, next) => {
//   if (store.state.isLogin === true) {
//     alert('이미 로그인 했습니다.');
//     next('/');
//   } else {
//     next();
//   }
// };

// const onlyAuthUser = (to, from, next) => {
//   if (store.state.isLogin === false) {
//     alert('로그인이 필요합니다.');
//     next('/');
//   } else {
//     next();
//   }
// };

const rejectAuthUser = (to, from, next) => {
  let token = '';
  token = localStorage.getItem('access_token');
  console.log('rejectAuthUser()', token);
  if (token !== null) {
    alert('로그인이 필요합니다.');
    next('/');
  } else {
    next();
  }
};

const onlyAuthUser = (to, from, next) => {
  let token = '';
  token = localStorage.getItem('access_token');
  console.log('onlyAuthUser()', token);
  if (token === null) {
    alert('로그인이 필요합니다.');
    next('/');
  } else {
    next();
  }
};

const routes = [
  // {
  //   path: '/',
  //   name: 'Books',
  //   component: Books,
  // },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/',
    name: 'Jumbotron',
    component: Jumbotron,
  },
  {
    path: '/',
    name: 'Home',
    component: Jumbotron,
  },
  {
    path: '/books',
    name: 'Books',
    beforeEnter: onlyAuthUser,
    component: Books,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/user_regi',
    name: 'UserRegi',
    beforeEnter: rejectAuthUser,
    component: UserRegi,
  },
  {
    path: '/profile',
    name: 'Profile',
    beforeEnter: onlyAuthUser,
    component: Profile,
  },
  {
    path: '/daemaechul',
    name: 'DayMaeChul',
    // beforeEnter: onlyAuthUser,
    component: DayMaeChul,
  },
  {
    path: '/chart',
    name: 'VueChartJs',
    // beforeEnter: onlyAuthUser,
    component: VueChartJs,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
