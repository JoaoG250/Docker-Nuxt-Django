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
      todos: [],
    };
  },
  created: function () {
    this.getTodos();
  },
  computed: {
    filteredTodos: function () {
      return this.todos.filter((item) => item.concluido === this.concluidos);
    },
  },
  methods: {
    getTodos: async function () {
      try {
        const response = await this.$axios.get("/todos");
        this.todos = response.data;
      } catch (e) {
        console.log(e);
      }
    },
  },
};
</script>
