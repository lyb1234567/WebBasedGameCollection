<template >
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <div class ="col-sm-12">
        <div class="mb-3 row" >
            
            <h1 class="text-center primary">Home Page</h1>

        </div>
        <form @submit.prevent="logOut">
        <div class ="mb-3 row">
            <div class="mb-3 col-sm-4"> </div>
            <div class="mb-3 col-sm-3" v-if="this.$store.state.isAuthenticated">           
                <button class="container-fluid btn btn-outline-success disabled">Logged In</button>
                
            </div>        
            <div class="mb-3 col-sm-3" v-if="this.$store.state.isAuthenticated"> 
                <button class="container-fluid btn btn-outline-danger" >Log Out</button>
            </div>
            <div class="mb-3 col-sm-4" v-else>
                <router-link to = "/login">
                    <button class="container-fluid btn btn-outline-success">Login</button>
                </router-link>
            </div>
        </div>
        </form>
        
    </div>

    
  </template>
  
  <script>  

  import axios from 'axios'
  
  export default {
    name: "HomePage",
    mounted() {
      this.checkAutentication();
    },
    methods: {
      checkAutentication() {
        if(this.$store.state.isAuthenticated)
        {
          this.username = localStorage.getItem('username')
          console.log(this.$store.state.isAuthenticated)
          console.log(this.username)
        }
        else{
          this.username = ''
          console.log(this.$store.state.isAuthenticated)
          console.log(this.username)
        }
        
      },
      logOut()
        {
            console.log()
            const formData = {
                token : localStorage.getItem('token'),
            }
            axios.defaults.headers.common['Authorization'] = "Token "+formData.token
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
                    this.$router.push('/')
                })
                .catch(error => {
                    console.log(error)
                })  
        }
    },
    data() {
        return {
            message: "Hello"
        };
    }
}
  </script>
  
  <style lang = "scss">
  @import '../assets/theme.scss';
  </style>
  