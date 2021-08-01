<template>
  <div>
    <create-dialog></create-dialog>
    <v-tabs>
      <v-tab @click="concluidos = false">Não Concluídos</v-tab>
      <v-tab @click="concluidos = true">Concluídos</v-tab>
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
      concluidos: false,
    };
  },
  created: function () {
    this.$store.dispatch("fetch");
  },
  computed: {
    filteredTodos: function () {
      return this.$store.state.list.filter(
        (item) => item.concluido === this.concluidos
      );
    },
  },
};
</script>
