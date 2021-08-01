<template>
  <v-form ref="form" v-model="valid" lazy-validation>
    <v-text-field v-model="form.titulo" label="Título" required></v-text-field>

    <v-text-field v-model="form.descricao" label="Descrição"></v-text-field>

    <v-checkbox
      v-model="form.concluido"
      label="Concluído?"
      required
    ></v-checkbox>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      valid: true,
      form: {
        titulo: "",
        descricao: "",
        concluido: false,
      },
    };
  },
  methods: {
    createTodo: async function () {
      console.log(this.form);
      // try {
      //   const response = await this.$axios.post("/todos", this.form);
      //   const todo = response.data;
      // } catch (e) {
      //   console.log(e);
      // }
    },
  },
};
</script>
