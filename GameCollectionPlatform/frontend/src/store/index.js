import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
    username: '',
  },
  mutations: {
    initializedStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token');
        state.username = localStorage.getItem('username');
        state.isAuthenticated = true;
        // console.log("Username "+state.username + " Token "+state.token)
      } else {
        state.token = '';
        state.username = '';
        state.isAuthenticated = false;
        // console.log("Resetting Username "+state.username + " Token "+state.token)
      }
    },
    setToken(state, token, username) {
      state.token = token;
      state.username = username;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = '';
      state.username = '';
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
  plugins: [createPersistedState()],
});
