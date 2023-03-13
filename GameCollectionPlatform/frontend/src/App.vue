<template>
  <div class = "container-fluid row mx-auto " >
        <nav class="navbar navbar-expand-lg bg-body-primary">
        <div class="container-fluid mx-auto">
            <router-link  to="/" class="navbar-brand">
                <img src="./pages/PlatformLogo.png" width="260" height="70" >
            </router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <!-- <div class ="col-mx-3">
                <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>
              </div>
              <div class ="col-mx-3">
                <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
                </li>
              </div>
              <div class ="col-mx-3">
                <li class="nav-item">
                <a class="nav-link disabled">Disabled</a>
                </li>
              </div> -->
             
            <div class ="col-mx-3" v-if="this.$store.state.isAuthenticated=== true">
                <button class="container btn btn-outline-success dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    {{this.username}}
                </button>
                <li class="container nav-item dropdown">
                <ul class="dropdown-menu dropdown-menu-left">
                    <li><button class = "container-fluid btn btn-success disabled">Logged In</button></li>
                    <form @submit.prevent="logOut">
                    <li><button class = "container-fluid btn btn-outline-danger">Logout</button></li>
                  </form>
                </ul>
              </li>
            </div>
            <div class ="col-mx-3 " v-else>
                <button class="container btn btn-outline-danger dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Not Logged In
                </button>
                <li class="container nav-item dropdown">
                <ul class="dropdown-menu dropdown-menu-left">
                  <router-link to = "/login">
                    <li><button class = "container-fluid btn btn-outline-success">Login</button></li>
                  </router-link>
                </ul>
              </li>
            </div>
            </ul>
                
      
            </div>
        </div>
        </nav>
    </div>
  <!-- <div id="nav">  
    <router-link to = "/"></router-link>
    <router-link to = "/register"></router-link>
  </div> -->
  <router-view/>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return {
      username : null,
    }
  },
  beforeCreate()
  {
     this.$store.commit('initializeStore')

     const token = this.$store.state.token

     if(token)
     {
        axios.defaults.headers.common['Authorization'] = 'Token '+token
     }
     else{
      axios.defaults.headers.common['Authorization'] = ''
     }
     
  },
  updated()
  {
    this.username = localStorage.getItem('username')
    console.log("Hello "+ this.username)
  },
  methods :
  {
    logOut()
        {
            console.log()
            const formData = {
                token : localStorage.getItem('token'),
            }
            
            axios
                .post('/api/v1/token/logout',formData)
                
                .then(response => {
                    console.log(response)
                    //const token = response.data.auth_token
                    //console.log(token)
                    this.$store.commit('removeToken')
                    //axios.defaults.headers.common['Authorization'] = "Token "+token
                    //localStorage.setItem('token',token)
                    //localStorage.setItem('username',this.username)
                    //onsole.log(localStorage.getItem('username'))
                    localStorage.setItem('token','')
                    localStorage.setItem('username','')
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                })  
        }
  }
}
</script>

<style lang="scss">
@import './styles/theme.scss';
</style>
