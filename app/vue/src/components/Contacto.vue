<template>
    <div class="contacto">
        <h1>Contacto</h1>
        <form @submit.prevent="enviarFormulario">
            <div class="form-group">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" v-model="form.nombre" required />
            </div>
            <div class="form-group">
                <label for="email">Correo Electrónico:</label>
                <input type="email" id="email" v-model="form.email" required />
            </div>
            <div class="form-group">
                <label for="mensaje">Mensaje:</label>
                <textarea id="mensaje" v-model="form.mensaje" required></textarea>
            </div>
            <button type="submit">Enviar</button>
        </form>
    </div>
</template>

<script>
export default {
    name: "Contacto",
    data() {
        return {
            form: {
                nombre: "",
                email: "",
                mensaje: "",
            },
        };
    },
    methods: {
        enviarFormulario() {
            console.log("Formulario enviado:", this.form);
            alert("Gracias por contactarnos. Te responderemos pronto.");
            this.form.nombre = "";
            this.form.email = "";
            this.form.mensaje = "";
        },
    },
};
</script>

<style scoped>
.contacto {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input,
textarea {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
}

button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>