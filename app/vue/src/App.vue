<template>
  <router-view />
</template>

<style scoped>
  :global(body) {
    background: -moz-radial-gradient(center, ellipse cover,  #63856a 1%, #3c5a40 100%); /* FF3.6+ */
    background: -webkit-radial-gradient(center, ellipse cover,  #63856a 1%,#3c5a40 100%); /* Chrome10+,Safari5.1+ */
    background: -o-radial-gradient(center, ellipse cover,  #63856a 1%,#3c5a40 100%); /* Opera 12+ */
    background: radial-gradient(ellipse at center,  #63856a 1%,#3c5a40 100%); /* W3C */
    color: white;
    font-family: 'Segoe UI', sans-serif;
  }
</style>