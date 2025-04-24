<template>
  <div class="dashboard">
    <h2>Bienvenido, Alumno</h2>
    <router-link to="/materias">
    <button class="action-button">📘 Hacer un ensayo</button>
    </router-link>
    <button class="action-button">📊 Ver mis resultados</button>
  </div>
</template>

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
