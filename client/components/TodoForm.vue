<template>
  <v-form ref="form" v-model="valid">
    <v-text-field
      v-model="form.titulo"
      label="Título"
      :rules="required"
      :error-messages="errors.titulo"
      required
    ></v-text-field>

    <v-text-field
      v-model="form.descricao"
      label="Descrição"
      :rules="required"
      :error-messages="errors.descricao"
      required
    ></v-text-field>

    <v-checkbox v-model="form.concluido" label="Concluída?"></v-checkbox>
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
      errors: {},
      required: [(v) => !!v || "Este campo não pode ser em branco."],
    };
  },
  methods: {
    reset() {
      this.$refs.form.reset();
    },
    validate() {
      this.$refs.form.validate();
    },
    onErrors(err) {
      this.errors = err.response.data;
    },
    create: function () {
      if (this.valid) {
        const action = this.$store.dispatch("create", this.form);
        action
          .then((resp) => {
            this.reset();
            this.$store.dispatch("fetch");
            this.$emit("success");
          })
          .catch((e) => {
            this.onErrors(e);
          });
      } else {
        this.validate();
      }
    },
    update: function () {
      if (this.valid) {
        const action = this.$store.dispatch("update", {
          url: this.form.url,
          todo: this.form,
        });
        action
          .then((resp) => {
            this.$store.dispatch("fetch");
            this.$emit("success");
          })
          .catch((e) => {
            this.onErrors(e);
          });
      } else {
        this.validate();
      }
    },
  },
};
</script>
