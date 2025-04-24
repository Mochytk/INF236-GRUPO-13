<script setup>
import { RouterLink } from 'vue-router';
</script>


<template>
  <div class="home-container">
    <h1 class="title">Plataforma Ensayos PAES</h1>

    <div class="button-group">
      <router-link to="/alumno">
        <button class="main-button">Iniciar sesión como Alumno</button>
      </router-link>
      <router-link to="/docente">
        <button class="main-button">Iniciar sesión como Docente</button>
      </router-link>
      <button class="main-button">Iniciar sesión como Visualizador</button>
    </div>

    <div class="info-buttons">
      <button class="secondary-button">Ver ejemplo de ensayo</button>
      <router-link to="/como-funciona">
        <button class="secondary-button">Cómo funciona la plataforma</button>
      </router-link>
      <router-link to="/contacto">
        <button class="secondary-button">Contáctanos</button>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  text-align: center;
  padding: 50px 20px;
  font-family: 'Segoe UI', sans-serif;
}

.title {
  font-size: 3em;
  margin-bottom: 40px;
  color: #2c3e50;
}

.button-group, .info-buttons {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin: 20px auto;
  max-width: 300px;
}

.main-button, .secondary-button {
  padding: 12px 20px;
  font-size: 1em;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.main-button {
  background-color: #3498db;
  color: white;
}

.secondary-button {
  background-color: #ecf0f1;
  color: #2c3e50;
}
</style>
