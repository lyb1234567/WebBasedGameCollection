import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import defaultImage from "../pages/image/default.png";
export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
    username: '',
    profilePic: defaultImage,
    games : null,
    gameCode : 0,
    userid : 0,
    collection : 0,
    community : null,
    publisher : null,
    pubDetails : null,
    pubCollection : null,
    pubGames : null ,
    gameReviews : null,
    userType : 'Game Player',
    loggedPubliserInfo : null,
    gamePrice: 0,
  },
  mutations: {
    initializedStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token');
        state.username = localStorage.getItem('username');
        state.isAuthenticated = true;
        state.profilePic = defaultImage
        // console.log("Username "+state.username + " Token "+state.token)
      } else {
        state.token = '';
        state.username = '';
        state.isAuthenticated = false;
        state.profilePic = defaultImage
        console.log("Resetting Username "+state.username + " Token "+state.token)
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
