// import { createRouter, createWebHistory } from 'vue-router'

// const routes = [
//   {
//     path: '/',
//     name: 'Home',
//     component: () => import('@/pages/Home.vue'),
//   },
// ]

// let router = createRouter({
//   history: createWebHistory('/frontend'),
//   routes,
// })

// export default router

import { createRouter, createWebHistory } from 'vue-router';
import store from './store';

// Pages
import Login from './pages/Login.vue';
import Home from './pages/Home.vue';
import Expenses from './pages/Expenses.vue';
import ExpenseCategories from './pages/ExpenseCategories.vue';
import ExpenseReports from './pages/ExpenseReports.vue';

const routes = [
  { path: '/login', component: Login },
  { path: '/home', component: Home },
  { path: '/expenses', component: Expenses },
  { path: '/expense-categories', component: ExpenseCategories },
  { path: '/expense-reports', component: ExpenseReports },
  { path: '/:catchAll(.*)', redirect: '/login' }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Protect routes
router.beforeEach((to, from, next) => {
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = store.getters.isLoggedIn;

  if (authRequired && !loggedIn) next('/login');
  else next();
});

export default router;





