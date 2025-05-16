<template>
    <div class="crear_ensayos">
        <h1>Crear Ensayos</h1>
        <form @submit.prevent="crearEnsayo">
            <div>
                <label for="nombre">Nombre del ensayo:</label>
                <input type="text" id="nombre" v-model="ensayo.nombre" required />
            </div>
            <div>
                <label for="materia">Materia:</label>
                <select id="materia" v-model="ensayo.materia" required>
                    <option value="" disabled selected>Selecciona una materia</option>
                    <option value="Matematicas">Matemáticas</option>
                    <option value="Lenguaje">Lenguaje</option>
                    <option value="Ciencias">Ciencias</option>
                    <option value="Historia">Historia</option>
                </select>
            </div>
            <button type="submit">Crear Ensayo</button>
        </form>
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
        crearEnsayo() {
            console.log('Ensayo creado:', this.ensayo);
        },
        obtenerCreador() {
            return localStorage.getItem('username') || materia;
        }
    }
};
</script>