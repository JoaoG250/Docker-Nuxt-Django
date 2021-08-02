<template>
  <div>
    <div class="text-h2 mb-5 text-center">Pendências</div>
    <create-dialog></create-dialog>
    <v-tabs>
      <v-tab @click="done = false">Não Concluídas</v-tab>
      <v-tab @click="done = true">Concluídas</v-tab>
    </v-tabs>
    <v-expansion-panels>
      <template v-for="todo in filteredTodos">
        <todo-item :key="todo.id" :todo="todo" />
      </template>
    </v-expansion-panels>
  </div>
</template>

<script>
export default {
  data() {
    return {
      done: false,
    };
  },
  created: function () {
    this.$store.dispatch("fetch");
  },
  computed: {
    filteredTodos: function () {
      return this.$store.state.list.filter(
        (item) => item.concluido === this.done
      );
    },
  },
};
</script>
