<template>
  <div>
    <h1>Todos</h1>
    <p>your todo list.</p>
    <v-btn href="/todos">View todos</v-btn>
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
