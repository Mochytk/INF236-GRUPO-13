import { createRouter, createWebHistory } from 'vue-router';
import Ensayos from '../views/Ensayos.vue';

const routes = [
  { path: '/ensayos', component: Ensayos },
];

const router = createRouter({
  history: createWebHistory(),
                            routes,
});

export default router;
