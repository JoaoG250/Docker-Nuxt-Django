<template>
  <v-dialog v-model="dialog" persistent width="500">
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" color="error" class="ms-2">Excluir</v-btn>
    </template>
    <v-card>
      <v-card-title class="text-h5">
        Tem certeza que deseja excluir o item?
      </v-card-title>
      <v-divider></v-divider>
      <v-card-actions class="justify-space-around">
        <v-btn color="secondary" @click="dialog = false"> Não </v-btn>
        <v-btn
          color="primary"
          @click="
            deleteTodo();
            dialog = false;
          "
        >
          Sim
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
  props: {
    id: Number,
  },
  methods: {
    deleteTodo: async function () {
      try {
        const response = await this.$axios.delete(`/todos/${this.id}/`);
      } catch (e) {
        console.log(e);
      }
    },
  },
};
</script>
