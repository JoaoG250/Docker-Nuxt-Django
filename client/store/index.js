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
    async create({ commit }, todo) {
        const response = await this.$axios.post("/todos/", todo);
        return response;
    },
    async update({ commit }, { url, todo }) {
        const response = await this.$axios.put(url, todo);
        return response;
    },
    async delete({ commit }, url) {
        const response = await this.$axios.delete(url);
        return response;
    }
};
