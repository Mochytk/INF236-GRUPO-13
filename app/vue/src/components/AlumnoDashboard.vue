<template>
    <div class="dashboard-container">
    <h1>Bienvenido, Alumno {{ nombreUsuario }}</h1>

        <div class="botones">
            <button @click="hacerEnsayo">Realizar Ensayo</button>
            <button @click="verResultados">Ver Resultados</button>
            <button @click="logout">Cerrar Sesión</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nombreUsuario: localStorage.getItem('username') || 'Alumno'
        }
    },
    methods: {
        hacerEnsayo() {
        // Aquí irá navegación o funcionalidad real
            alert("Funcionalidad para hacer ensayos próximamente.");
        },
        verResultados() {
            alert("Aquí se mostrarán tus resultados.");
        },
        logout() {
            localStorage.clear();
            this.$router.push('/');
        }
    },
    mounted() {
      // Protección: si no está logeado, redirige
    if (!localStorage.getItem('token')) {
        this.$router.push('/');
        }
    }
}
</script>

<style scoped>
.dashboard-container {
    text-align: center;
    padding: 40px;
    color: white;
}

.botones button {
    margin: 10px;
    padding: 10px 20px;
    font-size: 18px;
    background-color: #2ecc71;
    border: none;
    border-radius: 10px;
    cursor: pointer;
}

.botones button:hover {
    background-color: #27ae60;
}
</style>  