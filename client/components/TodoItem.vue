<template>
  <v-expansion-panel>
    <v-expansion-panel-header>
      {{ todo.titulo }}
      <v-checkbox v-model="todo.concluido" class="ms-4" disabled></v-checkbox>
    </v-expansion-panel-header>
    <v-expansion-panel-content>
      {{ todo.descricao }}
      <v-divider class="my-2"></v-divider>
      <div class="d-flex justify-end">
        <delete-dialog :url="todo.url"></delete-dialog>
        <edit-dialog :todo="todo"></edit-dialog>
      </div>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
export default {
  props: {
    todo: Object,
  },
};
</script>
