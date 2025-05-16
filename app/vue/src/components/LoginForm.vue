<template>
  <div class="login-container">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">Emaaaail:</label>
        <input type="email" v-model="email" required />
      </div>

      <div>
        <label for="password">Contraseña:</label>
        <input type="password" v-model="contraseña" required />
      </div>

      <button type="submit">Ingresar</button>

      <div v-if="error" style="color: red;">{{ error }}</div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      email: '',
      contraseña: '',
      error: ''
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', {
          email: this.email,
          contraseña: this.contraseña
        });

        const { token, rol, username } = response.data;

        // Guardamos token y rol (puedes usar localStorage o Vuex)
        localStorage.setItem('token', token);
        localStorage.setItem('rol', rol);

        // Redirigir según el rol
        if (rol.toLowerCase() === 'alumno') {
          this.$router.push('/alumno');
        } else if (rol.toLowerCase() === 'docente') {
          this.$router.push('/docente');
        }
        else{
          console.warn('Rol no reconocido:', rol);
          this.error = 'Rol no reconocido. Contacte al administrador.';
        }

      } catch (err) {
        console.error('Error de login', err.response?.data || err.message);
        this.error = err.response?.data?.error || 'Ocurrió un error al iniciar sesión';
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
