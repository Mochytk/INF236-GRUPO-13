<template>
  <div class="fondo-pizarra">
    <LoginForm />
    <VolverButton />
    <router-view />
  </div>
</template>


<style>
html, body {
  margin: 0;
  padding: 0;
}
</style>

<style>
.fondo-pizarra {
  min-height: 100vh;
  background-image: url('/img/fondo_pizarra.png');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
</style>

<script setup>
import VolverButton from './components/VolverButton.vue';
import LoginForm from './components/LoginForm.vue';
</script>

