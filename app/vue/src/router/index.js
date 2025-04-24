import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import AlumnoDashboard from '../components/AlumnoDashboard.vue';
import ComoFunciona from '../components/ComoFunciona.vue';
import Contacto from '../components/Contacto.vue';
import DocenteDashboard from '../components/DocenteDashboard.vue';  

const routes = [
  { path: '/', component: HomePage },
  { path: '/alumno', component: AlumnoDashboard },
  { path: '/como-funciona', component: ComoFunciona},
  { path: '/contacto', component: Contacto},
  { path: '/docente', component: DocenteDashboard},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
