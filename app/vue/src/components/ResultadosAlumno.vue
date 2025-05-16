<template>
    <div class="resultados-alumno">
        <h1>Resultados del Alumno</h1>
        <p>Ensayos realizados: 0</p>
    </div>
</template>

<script>
export default {
data() {
    return {
        nombreUsuario: localStorage.getItem('username') || 'Docente'
    }
},

mounted() {
    // Protección: si no está logeado, redirige
    if (!localStorage.getItem('token')) {
        this.$router.push('/acceso-restringido');
    }
}
}
</script>

<style scoped>
h1 {
    color: white;
    text-align: center;
    margin-top: 80px;
    font-family: 'Segoe UI', sans-serif;
}
p {
    color: white;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    margin-top: 20px;
}
</style>