<template>
  <div class="ensayo-container">
    <h1>Ensayo de {{ materia }}</h1>

    <div v-for="(pregunta, index) in preguntas" :key="index" class="pregunta-box">
      <p><strong>{{ index + 1 }}. {{ pregunta.texto }}</strong></p>
      <div class="alternativas">
        <label v-for="opcion in pregunta.opciones" :key="opcion">
          <input
            type="radio"
            :name="'pregunta-' + index"
            :value="opcion"
            v-model="respuestas[index]"
          />
          {{ opcion }}
        </label>
      </div>
    </div>

    <button class="boton-finalizar" @click="finalizarEnsayo">Finalizar Ensayo</button>

    <div v-if="puntaje !== null" class="resultado">
      <h2>Tu puntaje estimado: {{ puntaje }} pts</h2>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const materia = localStorage.getItem('materiaSeleccionada') || 'Materia';

const preguntas = ref([
  {
    texto: '¿Cuál es la capital de Chile?',
    opciones: ['Santiago', 'Valparaíso', 'Rancagua', 'La Serena'],
    correcta: 'Santiago',
  },
  {
    texto: '¿Cuál de las siguientes alternativas es el más grande de Chile?',
    opciones: ['El costanera', 'Arturo Vidal', 'Universidad de Chi(c)le', 'Colo-Colo'],
    correcta: 'Colo-Colo',
  },
  {
    texto: '¿Quién fundó la Universidad Técnica Federico Santa María?',
    opciones: ['Federico Santa María', 'Técnica', 'Pedro Aguirre Cerda', 'Ninguno de los anteriores'],
    correcta: 'Federico Santa María',
  },
]);

const respuestas = ref({});
const puntaje = ref(null);

function finalizarEnsayo() {
  let correctas = 0;

  preguntas.value.forEach((pregunta, index) => {
    if (respuestas.value[index] === pregunta.correcta) {
      correctas++;
    }
  });

  puntaje.value = Math.floor((correctas / preguntas.value.length) * 1000);
}
</script>

<style scoped>
.ensayo-container {
  color: white;
  padding: 40px;
  text-align: center;
}

.pregunta-box {
  margin-bottom: 30px;
  background-color: white;
  color: black;
  padding: 20px;
  border-radius: 15px;
}

.alternativas label {
  display: block;
  margin-top: 10px;
  font-weight: normal;
}

.boton-finalizar {
  margin-top: 30px;
  padding: 10px 20px;
  background-color: #2ecc71;
  border: none;
  border-radius: 8px;
  color: white;
  cursor: pointer;
  font-size: 16px;
}

.boton-finalizar:hover {
  background-color: #27ae60;
}

.resultado {
  margin-top: 30px;
  background-color: #ffffff88;
  color: black;
  padding: 20px;
  border-radius: 10px;
}
</style>
