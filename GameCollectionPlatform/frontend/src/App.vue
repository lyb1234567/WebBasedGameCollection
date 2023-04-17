<template>
  <!-- NavBar  -->
  <div class="container-fluid row mx-auto">
    <nav class="navbar navbar-dark navbar-expand-lg">
      <div class="container-fluid mx-auto">
        <router-link to="/" class="navbar-brand">
          <img src="./components/logos/Dark-Logo.png" width="250" height="70" class="img-fluid" />
        </router-link>
        <button
          class="navbar-toggler btn-outline-primary"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mb-4 mb-lg-0" style="margin-left: auto">
            <div class="col-mx-3" v-if="this.$store.state.isAuthenticated === true">
              <button
                class="container btn btn-outline-success dropdown-toggle"
                type="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                {{ this.username }}
              </button>
              <li class="container nav-item dropdown dropdown-menu-left">
                <ul
                  class="dropdown-menu dropdown-menu-start dropdown-menu-lg-end"
                  style="background: transparent; padding-right: 10px"
                >
                  <div class="row">
                    <li>
                      <button class="container-fluid btn btn-success disabled">Logged In</button>
                    </li>
                  </div>
                  <div class="row mt-2">
                    <form @submit.prevent="logOut">
                      <li>
                        <button class="container-fluid btn btn-outline-danger">Logout</button>
                      </li>
                    </form>
                  </div>
                </ul>
              </li>
            </div>
            <div class="col-mx-4" v-else>
              <button
                class="container btn btn-outline-danger dropdown-toggle"
                type="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                Not Logged In
              </button>
              <li class="container nav-item dropdown">
                <ul
                  class="dropdown-menu dropdown-menu-left col-mx-3"
                  style="background: transparent; padding-right: 10px"
                >
                  <router-link to="/login">
                    <li>
                      <button class="container-fluid btn btn-outline-primary">Login</button>
                    </li>
                  </router-link>
                </ul>
              </li>
            </div>
          </ul>
        </div>
      </div>
    </nav>
  </div>
  <!-- NavBar End -->
  <div id="nav">
    <router-link to="/"></router-link>
    <router-link to="/register"></router-link>
  </div>
  <router-view />
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      username: localStorage.getItem('username'),
    };
  },
  beforeCreate() {
    this.$store.commit('initializeStore');

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token;
    } else {
      axios.defaults.headers.common['Authorization'] = '';
    }
  },
  updated() {
    this.username = localStorage.getItem('username');
    console.log('Hello ' + this.username);
  },
  methods: {
    logOut() {
      console.log();
      const formData = {
        token: localStorage.getItem('token'),
      };
      console.log("Logging out ",formData.token)
      axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('token');
      axios
        .post('/api/v1/token/logout', formData)

        .then(response => {
          console.log(response);
          this.$store.commit('removeToken');
          localStorage.setItem('token', '');
          localStorage.setItem('username', '');
          this.$router.push('/')
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss">
@import './styles/theme.scss';
</style>
