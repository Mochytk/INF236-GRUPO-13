<template>
    <div class="editor">
        <h1>Editor de Ensayos</h1>
        <p>Nota: la funcionalidad para editar ensayos está en desarrollo.</p>
        <button class="boton" @click="mostrar">Mostrar Ensayos</button>
        <p>Haz clic en el botón para mostrar los ensayos disponibles.</p>
        <p>Recuerda que esta funcionalidad está en desarrollo y puede no estar completamente implementada.</p>

        <div v-if="mostrarTabla">
            <table class="tabla-ensayos">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Materia</th>
                        <th>Creador</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="ensayo in ensayos" :key="ensayo.id">
                        <td>{{ ensayo.nombre }}</td>
                        <td>{{ ensayo.materia }}</td>
                        <td>{{ ensayo.creador }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            ensayo: {
                nombre: '',
                materia: '',
                creador: this.obtenerCreador(),
            }
        };
    },
    methods: {
        async crearEnsayo() {
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/', this.ensayo, {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
            alert("Ensayo creado exitosamente.");
            // Opcional: limpiar el formulario o redirigir
            this.ensayo.nombre = '';
            this.ensayo.materia = '';
        } catch (error) {
            alert("Error al crear el ensayo.");
            console.error(error);
        }
    },
        obtenerCreador() {
            return localStorage.getItem('username') || 'Docente';
        }
    },
    mounted() {
        // Protección: si no está logeado, redirige
        if (!localStorage.getItem('token')) {
            this.$router.push('/acceso-restringido');
        }
    }
};

function alerta() {
    alert("Ensayo creado exitosamente.");
}
</script>

<style scoped>
.crear_ensayos {
    font-family: 'Segoe UI', sans-serif;
    color: #ffffff;
    padding: 20px;
}
h1 {
    color: #ffffff;
    text-align: center;
    margin-top: 80px;
    font-family: 'Segoe UI', sans-serif;
}
p {
    color: #ffffff;
    line-height: 1.6;
    font-family: 'Segoe UI', sans-serif;
}
.boton {
    background-color: #3498db;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
</style>