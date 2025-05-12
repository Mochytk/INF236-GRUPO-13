<template>
  <div class="home-container">
    <h1 class="titulo">Bienvenido</h1>

    <div class="contenido">
      <div class="materias">
        <img :src="imgs.lenguaje" alt="Lenguaje" />
        <img :src="imgs.matematicas" alt="Matemáticas" />
        <img :src="imgs.historia" alt="Historia" />
        <img :src="imgs.ciencias" alt="Ciencias" />
      </div>

      <div class="login">
        <p class="login-label">Login</p>
        <input type="text" class="login-input" placeholder="Correo" v-model="email"/>
        <input type="password" class="login-input" placeholder="Contraseña" v-model="password"/>
        <button class="login-input" @click="handleLogin">Iniciar sesión</button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        <RouterLink to="/alumno">
        <button class="acceso-provisorio">Acceder como Alumno (provisorio)</button>
        </RouterLink>
        <RouterLink to="/docente">
        <button class="acceso-provisorio">Acceder como Docente (provisorio)</button>
        </RouterLink>
      </div>
    </div>

    <div class="info-botones">
      <router-link to="/como-funciona">
        <button class="secondary-button">Cómo funciona la plataforma</button>
      </router-link>
      <router-link to="/about">
        <button class="secondary-button">Sobre nosotros</button>
      </router-link>
    </div>
  </div>
</template>
<script setup>

import { RouterLink } from 'vue-router';
import { ref } from 'vue';
import { login } from '@/api/auth';
import axios from 'axios';

const email = ref('');
const password = ref('');
const errorMessage = ref('');

const handleLogin = async () => {
  try {
    const response = await axios.post('/api/usuarios/login/', {
      email: email.value,
      password: password.value,
    });
    localStorage.setItem('token', response.data.token);
    alert(`Inicio de sesión exitoso. Rol: ${response.data.role}`);
    if (response.data.role === 'alumno') {
      window.location.href = '/alumno';
    } else if (response.data.role === 'docente') {
      window.location.href = '/docente';
    }
  } catch (error) {
    errorMessage.value = error.response?.data?.error || 'Inicio de sesión fallido';
  }
};

const imgs = {
  lenguaje: '/img/lenguaje.jpg',
  matematicas: '/img/matematicas.jpg',
  historia: '/img/historia.jpg',
  ciencias: '/img/ciencias.jpg',
};
</script>

<style scoped>
.home-container {
  color: white;
  padding: 40px 20px;
  min-height: 100vh;
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
}

.titulo {
  font-size: 3em;
  margin-bottom: 40px;
}

.contenido {
  display: flex;
  justify-content: center;
  gap: 60px;
  flex-wrap: wrap;
  align-items: center;
}

.materias {
  display: grid;
  grid-template-columns: repeat(2, 130px);
  gap: 20px;
}

.materias img {
  width: 130px;
  height: 130px;
  border-radius: 12px;
  object-fit: cover;
  box-shadow: 0 0 10px #00000044;
}

.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

.login-label {
  font-size: 1.4em;
  font-weight: bold;
  margin-bottom: 10px;
}

.login-input {
  width: 200px;
  height: 45px;
  font-size: 1.1em;
  background-color: #145a32;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
}

.info-botones {
  margin-top: 50px;
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
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

.acceso-provisorio {
  margin-top: 10px;
  background-color: #2ecc71;
  color: white;
  padding: 10px 18px;
  border: none;
  border-radius: 10px;
  font-size: 1em;
  cursor: pointer;
}

</style>
