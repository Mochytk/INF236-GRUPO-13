<template>
  <div class="login-container">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Usuario:</label>
        <input type="text" id="username" v-model="username" required>
      </div>

      <div>
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="password" required>
      </div>

      <button type="submit">Ingresar</button>

      <div v-if="error" style="color: red;">{{ error }}</div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', {
          username: this.username,
          password: this.password
        })

        console.log('Login exitoso', response.data)
        // Aquí podrías guardar el token o el usuario en localStorage o Vuex si quieres
      } catch (err) {
        console.error('Error de login', err)
        this.error = 'Usuario o contraseña incorrectos'
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
}
</style>
