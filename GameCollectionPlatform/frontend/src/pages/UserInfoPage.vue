<template >
  <div class="col-sm-12">
    <div class="mb-3 row">
      <h1 class="text-center text-secondary">User Information</h1>
    </div>
    <form @submit.prevent="submitForm" id="myform">
      <div class="container-fluid row mx-auto col-12 col-md-10 col-lg-8" id="App">
        <div class="container-fluid mb-3 row">
          <div class="col-sm-1"></div>
          <div class="col-sm-2">
            <button type="button" class="btn btn-outline" data-bs-toggle="modal" data-bs-target="#fileUpoadModal">
              <img v-bind:src="this.profilePic" alt="" class="image-preview" v-if="
                                this.uploading === false || this.cancelFileUpload === true
                            " @change="checkUpdateUserInfo" />
              <img v-bind:src="this.imagePreview" alt="" class="image-preview" style="background-color: transparent"  v-else @change="checkUpdateUserInfo"/>
            </button>
          </div>
          <!-- <div class="col-sm-1"></div> -->
          <div class="col-sm-4">
            <div class="row pt-4 mt-4 mb-4">
              <div class="col-sm-12">
                <input type="text" class="form-control border-secondary bg-dark text-secondary" id="firstName"
                  placeholder="First Name" v-model="firstName" disabled />
              </div>
            </div>
            <div class="row">
              <div class="col-sm-12">
                <input type="text" class="form-control border-secondary bg-dark text-secondary" id="lastName"
                  placeholder="Last Name" v-model="lastName" disabled />
              </div>
            </div>
          </div>
          <div class="col-sm-4">
            <div class="row pt-4 mt-4 mb-4">
              <div class="col-sm-12">
                <textarea class="form-control border-secondary bg-dark text-secondary" rows="4"
                  placeholder="Short introduction about you" v-model="userInfo" style="height: 100px;" @change="checkUpdateUserInfo"></textarea>
              </div>
            </div>
          </div>
        </div>
        <div class="mb-3 row">
          <div class="col-sm-1"></div>
          <label for="staticEmail" class="col-sm-1 col-form-label border-dark text-secondary">Username</label>
          <div class="col-sm-4">
            <input type="text" class="form-control border-secondary bg-dark text-secondary" id="username"
              placeholder="This will be visible to all players" v-model="username" disabled />
          </div>
          <!-- <div class="col-sm-1"></div> -->
          <label for="staticEmail" class="col-sm-1 col-form-label text-secondary">Email</label>
          <div class="col-sm-4">
            <input type="email" class="form-control border-secondary bg-dark text-secondary" id="email"
              placeholder="name@example.com" v-model="email" disabled />
          </div>
        </div>
        <div class="mb-3 row">

        </div>
        <div class="mb-3 row">
          <div class="col-sm-1"></div>
          <label for="inputPassword" class="col-sm-1 col-form-label text-secondary">Birthday</label>
          <div class="col-sm-4 pt-2">
            <input v-model="dateOfBirth" class="form-control border-secondary bg-dark text-secondary" disabled />
          </div>
          <div class="col-sm-1 col-form-label text-secondary">
            You are a
          </div>
          <div class="btn-group col-sm-4" role="group" aria-label="Basic radio toggle button group">
            <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" value="Game Player"
              v-model="this.userType" v-if="this.userType === 'Game Player'" diabled>
            <label class="btn btn-outline-primary col-sm-2 mt-2" for="btnradio1"
              v-if="this.userType === 'Game Player'">Game
              Player</label>

            <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off" value="Game Publisher"
              v-model="this.userType" v-if="this.userType === 'Game Publisher'" diabled>
            <label class="btn btn-outline-primary col-sm-2 mt-2" for="btnradio2"
              v-if="this.userType === 'Game Publisher'">Game Publisher</label>
            <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off" value="Game Publisher"
              v-model="this.userType" v-if="this.userType === 'Admin'" diabled>
            <label class="btn btn-outline-primary col-sm-2 mt-2" for="btnradio2"
              v-if="this.userType === 'Admin'">Admin</label>
          </div>
        </div>
        <div class="mb-3 row">
          <div class="mb-3 col-sm-9"></div>
          <div class="mb-3 col-sm-2">
            <button class="btn btn-outline-success" type="submit" form="myform" @click="updateInfo" v-if="this.updateInfoFlag">
              Update Info
            </button>
          </div>
        </div>
      </div>
    </form>
  </div>
  <!-- Modal -->
  <div class="modal fade bg-blur" id="fileUpoadModal" tabindex="-1" aria-labelledby="exampleModalLabel"
    aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content bg-dark">
        <div class="modal-header mb-3" style="border-color: #a39f60;">
          <h5 class="col-sm-10 modal-title text-center text-primary" id="exampleModalLabel" style="margin-left: 5%;">
            Image Upload
          </h5>
          <button type="button" class="btn btn-outline-danger col-sm-1" data-bs-dismiss="modal" aria-label="Close"
            style="margin-right: 10 %;">X</button>
        </div>
        <div class="modal-body" style="align-content: center; border-color: #a39f60;">
          <div class="mb-3 row">
            <div class="col-sm-4 text-primary">Click on image to upload</div>
            <div class="col-sm-4">
              <img src="../components/logos/initialUpload.png" alt="" class="btn btn-outline-secondary image-preview"
                v-on:click="openUpload" v-if="
                  this.uploading === false || this.cancelFileUpload === true
                " style="border-radius: 50px; border: 2px solid #a39f60;" />
              <img v-bind:src="this.imagePreview" alt="" class="btn btn-outline-secondary image-preview"
                v-on:click="openUpload" v-else style="border-radius: 50px;  border: 2px solid #a39f60;" />
              <div class="form-group">
                <input name="image" type="file" id="file-field" accept="image/*" v-on:change="fileUpload"
                  style="display: none;" />
              </div>
            </div>
            <div class="col-sm-4"></div>
          </div>
        </div>
        <div class="modal-footer" style="border-color: #a39f60;">
          <button type="button" class="btn btn-outline-success" v-bind:disabled="
            this.uploading === false || this.cancelFileUpload === true
          " @click="onDone" data-bs-dismiss="modal">
            Done
          </button>
          <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal" @click="onCancel">
            Clear Image
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>

import axios from 'axios'

export default {
  name: "UserInfoPage",
  mounted() {
    this.fetchUserInfo();
    console.log(this.profilePic)
  },
  methods: {
    checkUpdateUserInfo(){
      if(this.userInfo === this.userInfoOg || (this.profilePic === this.uploadedPic))
      {
        this.updateInfoFlag = false
      }
      else
      {
        this.updateInfoFlag = true
      }
    },
    updateInfo() {
      console.log("Updaating Profile Pic")
        console.log(this.profilePic)
        console.log(this.uploadedPic)
        console.log(this.userInfo)
          const formData = {
                username: this.username,
                profilePic: this.uploadedPic,
                userInfo: this.userInfo,
            };
            let form_data = new FormData()
            form_data.append('username',formData.username)
            form_data.append('profilePic',formData.profilePic)
            form_data.append('userInfo',formData.userInfo)
            console.log(form_data)
            console.log(formData)
            axios
                .post("/api/v1/user/update/", form_data)

                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
    },
    onDone() {
      this.uploading = true;
      this.fileName = this.profilePic["name"];
    },
    onCancel() {
      this.uploading = false;
      this.uploadedPic = this.profilePic;
    },
    openUpload() {
      document.getElementById("file-field").click();
    },
    fileUpload(e) {
      this.uploadedPic = e.target.files[0];
      var reader,
        files = e.target.files;
      reader = new FileReader();
      reader.onload = (e) => {
        this.imagePreview = e.target.result;
      };
      reader.readAsDataURL(files[0]);
      console.log(this.uploadedPic);
      this.uploading = true;
    },
    preview() {
      console.log(this.uploadedPic);
      var reader = new FileReader();
      reader.readAsDataURL(this.uploadedPic);
    },
    formatDate() {
      const day = this.dateOfBirth.getDate();
      const monthIndex = this.dateOfBirth.getMonth();
      const year = this.dateOfBirth.getFullYear();
      const monthNames = ["Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"];
      const monthName = monthNames[monthIndex];
      this.dateOfBirth = `${day}-${monthName}-${year}`;
    },
    fetchUserInfo() {
      if (this.$store.state.isAuthenticated) {
        console.log("Fetching data  ")
        
        axios
          .get('/api/v1/users/me')

          .then(response => {
            this.username = response.data['username']
            this.firstName = response.data['firstName']
            this.lastName = response.data['lastName']
            this.email = response.data['email']
            this.profilePic = response.data['profilePic']
            if (null === this.profilePic) {
              console.log("No DP")
              this.profilePic = "../components/logos/initialUpload.png"
            }
            this.uploadedPic = this.profilePic
            this.imagePreview=this.profilePic
            this.dateOfBirth = new Date(response.data['dateOfBirth'])
            this.formatDate()


            this.userInfo = response.data['userInfo']
            this.userInfoOg = this.userInfo
            this.userType = response.data['userType']
            this.location = response.data['location']
            console.log(this.profilePic)

          })
          .catch(error => {
            console.log(error)
          })
        //   this.username = localStorage.getItem('username')
        //   console.log(this.$store.state.isAuthenticated)
        //   console.log("Hello Checking Auth "+this.username)
        //   console.log("Auth Token : "+axios.defaults.headers.common['Authorization'])
      }
      else {
        this.username = ''
        console.log(this.$store.state.isAuthenticated)
        console.log("Hello Checking Auth " + this.username)
      }

    },
  },
  data() {
    return {
      username: '',
      firstName: '',
      lastName: '',
      email: '',
      profilePic: "../components/logos/initialUpload.png",
      uploadedPic: '',
      dateOfBirth: null,
      userInfo: '',
      userInfoOg: '',
      userType: '',
      location: '',
      uploading: false,
      imagePreview: null,
      fileName: "",
      cancelFileUpload: false,
      updateInfoFlag: false,


    };
  }
}
</script>
  
<style lang = "scss">
@import '../styles/theme.scss';
@import '../styles/styles.css';
</style>
  