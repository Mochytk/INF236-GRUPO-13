<template>
    <div class="dashboard">
        <h2>Bienvenido, {{ rol === 'alumno' ? 'Alumno' : 'Docente' }}</h2>
        <router-link v-if="rol === 'alumno'" to="/materias">
        <button class="action-button">📘 Hacer un ensayo</button>
        </router-link>
        <router-link v-if="rol === 'alumno'" to="/alumno/resultados">
        <button class="action-button">📊 Ver mis resultados</button>
        </router-link>
        <router-link v-if="rol === 'docente'" to="/docente/historial">
        <button class="action-button">📘 Ver historial de ensayos</button>
        </router-link>
        <router-link v-if="rol === 'docente'" to="/docente/ranking">
        <button class="action-button">📊 Ver ránking de ensayos</button>
        </router-link>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();
const rol = route.params.rol;
</script>

<style scoped>
.dashboard {
    text-align: center;
    margin-top: 80px;
    font-family: 'Segoe UI', sans-serif;
}

.action-button {
    margin: 20px;
    padding: 15px 25px;
    font-size: 1.2em;
    border: none;
    border-radius: 10px;
    background-color: #27ae60;
    color: white;
    cursor: pointer;
}
</style>