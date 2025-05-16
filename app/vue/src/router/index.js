import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
//import Dashboard from '../components/DocenteDashboard.vue';
import ComoFunciona from '../components/ComoFunciona.vue';
import About from '../components/About.vue';
import SeleccionarMateria from '../components/SeleccionarMateria.vue'; 
import Historial from '../components/Historial.vue';
import Ranking from '../components/Ranking.vue';
import ResultadosAlumno from '../components/ResultadosAlumno.vue';
import AlumnoDashboard from '../components/AlumnoDashboard.vue';
import DocenteDashboard from '../components/DocenteDashboard.vue';
import LoginForm from '../components/LoginForm.vue';

const routes = [
  { path: '/materias', component: SeleccionarMateria },
  { path: '/', component: HomePage },
  { path: '/login', component: LoginForm },
  //{ path: '/:rol', component: Dashboard },
  { path: '/como-funciona', component: ComoFunciona},
  { path: '/about', component: About},
  { path: '/docente/historial', component: Historial},
  { path: '/docente/ranking', component: Ranking},
  { path: '/alumno/resultados', component: ResultadosAlumno},
  //{ path: '/', component: LoginForm },
  { path: '/alumno', component: AlumnoDashboard},
  { path: '/docente', component: DocenteDashboard},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
