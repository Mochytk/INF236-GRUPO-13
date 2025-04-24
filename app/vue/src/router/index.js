import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import AlumnoDashboard from '../components/AlumnoDashboard.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/alumno', component: AlumnoDashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
