<template >
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <div class ="col-sm-12">
        <div class="mb-3 row" >
            
            <h1 class="text-center">Login</h1>

        </div>
        <form @submit.prevent="submitForm">
        <div class = "container-fluid row mx-auto col-10 col-md-8 col-lg-6 " id ="App">
        <div class="mb-3 row">
            <label for="staticEmail" class="col-sm-2 col-form-label">Username</label>
            <div class="col-sm-10">
            <input type="text" class="form-control border-dark" id="staticEmail" placeholder="" v-model = "username">
            </div>
        </div>
        <div class="mb-3 row">
            <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
            <div class="col-sm-10">
            <input type="password" class="form-control border-dark" id="inputPassword" v-model = "password">
            </div>
        </div>
        <div class ="mb-3 row"></div>
        <div class ="mb-3 row">
        <div class="mb-3 col-sm-4"> </div>
        <div class="mb-3 col-sm-4">
            <button class="container btn btn-outline-success">Login Now!</button>
        </div>
        <div class="mb-3 col-sm-4">
            <router-link to="/register">
                <button class="container btn btn-outline-primary">New User? Click here to Register.</button>
            </router-link>
        </div>
        
    </div>
    <div class = "container-fluid row text-end" v-if="this.isLoggedIn === false">
        <div class = "text-danger">Invalid Credentials</div>
    </div> 
    </div>
    </form>
    </div>
    
    
    
    
  </template>
  
  <script>
import axios from 'axios'


  
  export default {
    name: 'RegisterPage',
    data () {
      return {
        username : '',
        email: '',
        isLoggedIn : true
      }
     
    },
    
    methods: {
        submitForm()
        {
            console.log()
            const formData = {
                username : this.username,
                password : this.password
            }
            
            axios.defaults.headers.common['Authorization'] = ""
            axios
                .post('/api/v1/token/login',formData)
                
                .then(response => {
                    console.log(response)
                    const token = response.data.auth_token
                    console.log(token)
                    this.$store.commit('setToken',token,this.username)
                    axios.defaults.headers.common['Authorization'] = "Token "+token
                    localStorage.setItem('token',token)
                    localStorage.setItem('username',this.username)
                    console.log(localStorage.getItem('username'))
                    this.isLoggedIn = true
                    console.log(this.isLoggedIn)
                    console.log(this.$store.state.username)
                    this.$router.push('/')
                })
                .catch(error => {
                    this.isLoggedIn = false
                    console.log(this.isLoggedIn)
                    console.log(error)
                })  
        }
    }
  }
  </script>
  
  <style lang = "scss">
  @import '../assets/theme.scss';
  </style>
  