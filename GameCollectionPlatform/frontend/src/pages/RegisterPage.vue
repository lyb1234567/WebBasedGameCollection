<template >
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <div class ="col-sm-12">
        <div class="mb-3 row" >
            
            <h1 class="text-center text-primary">Hello Please Enter Details</h1>

        </div>
        <form @submit.prevent="submitForm">
        <div class = "container-fluid row mx-auto col-10 col-md-8 col-lg-6 " id ="App">
        <div class="mb-3 row  ">
            <label for="staticEmail" class="col-sm-2 col-form-label text-dark">Name</label>
            <div class="col-sm-4">
            <input type="text" class="form-control border-dark " id="name" placeholder="First Name" v-model="firstName">
            </div>
            <div class="col-sm-4">
            <input type="text" class="form-control border-dark " id="name" placeholder="Last Name" v-model="lastName">
            </div>
        </div>
        <div class="mb-3 row">
            <label for="staticEmail" class="col-sm-2 col-form-label border-dark">Username</label>
            <div class="col-sm-8">
            <input type="text" class="form-control border-dark" id="username" placeholder="This will be visible to all players" v-model="username">
            </div>
        </div>
        <div class="mb-3 row">
            <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
            <div class="col-sm-8">
            <input type="email" class="form-control border-dark" id="email" placeholder="name@example.com" v-model="email">
            </div>
        </div>
        <div class="mb-3 row">
            <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
            <div class="col-sm-8">
            <input type="password" class="form-control border-dark" id="password" v-model="password">
            </div>
        </div>
        <div class="mb-3 row">
            <label for="inputPassword" class="col-sm-2 col-form-label">Confirm Password</label>
            <div class="col-sm-8">
            <input type="password" class="form-control border-dark" id="password2" v-model="pass2">
            </div>
        </div>
        <div class ="mb-3 row">
        <div class="mb-3 col-sm-8"> </div>
        <div class="mb-3 col-sm-2">
            <button class="btn btn-outline-success">Register Now!</button>
        </div>
    </div>
    </div>
    </form>
    </div>
    
    
    
    
  </template>
  
  <script>
  import axios from 'axios'
// import { response } from 'express'
  
  export default {
    name: 'RegisterPage',
    data () {
      return {
        username : '',
        email: '',
        password : '',
        firstName : '',
        lastName : '',
        profilePic : null,
        userInfo : '',
        dateOfBirth : null,
        userType : '',
        location : '',
      }
     
    },
    methods: {
        submitForm()
        {
            console.log()
            const formData = {
                username : this.username,
                password : this.password,
                email : this.email,
                firstName : this.name,
                lastName : '',
                profilePic : null,
                userInfo : '',
                dateOfBirth : null,
                userType : '',
                location : '',

            }
            axios.defaults.headers.common['Authorization'] = ""
            axios
                .post('/api/v1/users/',formData)
                
                .then(response => {
                    this.$router.push('/login')
                    console.log(response)
                })
                .catch(error => {
                    console.log(error)
                })  
        }
    }
  }
 
  </script>
  
  <style lang = "scss">
  @import '../assets/theme.scss';
  </style>
  