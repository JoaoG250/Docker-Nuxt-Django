export const state = () => ({
    list: []
});

export const mutations = {
    SET_TODOS(state, todos) {
        state.list = todos;
    }
};

export const actions = {
    async fetch({ commit }) {
        try {
            const response = await this.$axios.get("/todos/");
            commit("SET_TODOS", response.data);
        } catch (e) {
            console.log(e);
        }
    },
    async create({ dispatch, commit }, todo) {
        try {
            await this.$axios.post("/todos/", todo);
            await dispatch("fetch");
        } catch (e) {
            console.log(e);
        }
    },
    async update({ dispatch, commit }, { url, todo }) {
        try {
            await this.$axios.put(url, todo);
            await dispatch("fetch");
        } catch (e) {
            console.log(e);
        }
    },
    async delete({ dispatch, commit }, url) {
        try {
            await this.$axios.delete(url);
            await dispatch("fetch");
        } catch (e) {
            console.log(e);
        }
    }
};
