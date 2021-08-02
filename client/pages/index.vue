<template>
  <div>
    <h1 class="text-h1 mb-3">Pendências</h1>
    <p class="text-h4 mb-5">
      Mais um aplicativo para guardar suas tarefas pendentes
    </p>
    <v-btn href="/todos" color="teal" x-large nuxt>Ver Pendências</v-btn>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: "Home",
    };
  },
};
</script>
