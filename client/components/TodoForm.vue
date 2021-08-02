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
  props: {
    instance: {
      type: Object,
      default: null,
      required: false,
    },
  },
  data() {
    const form = {
      titulo: "",
      descricao: "",
      concluido: false,
    };
    if (this.instance) {
      Object.assign(form, this.instance);
    }
    return {
      valid: true,
      form: form,
    };
  },
  methods: {
    reset() {
      this.$refs.form.reset();
    },
    onErrors(errors) {
      const data = errors.response.data;
      console.log(data);
    },
    create: function () {
      const action = this.$store.dispatch("create", this.form);
      action
        .then((resp) => {
          this.reset();
          this.$store.dispatch("fetch");
        })
        .catch((e) => {
          this.onErrors(e);
        });
    },
    update: function () {
      this.$store.dispatch("update", { url: this.form.url, todo: this.form });
    },
  },
};
</script>
