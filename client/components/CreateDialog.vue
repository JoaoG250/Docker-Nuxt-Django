<template>
  <v-dialog v-model="dialog" persistent width="600">
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" color="primary" class="mb-2"
        >Criar Todo</v-btn
      >
    </template>
    <v-card>
      <v-card-title class="text-h5"> Criar todo </v-card-title>
      <v-card-text>
        <todo-form ref="todoForm"></todo-form>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="secondary" @click="dialog = false"> Fechar </v-btn>
        <v-btn
          color="primary"
          @click="
            $refs.todoForm.create();
            dialog = false;
          "
        >
          Salvar
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
    };
  },
};
</script>
