<template >
  <div class="col-sm-12" v-if="this.userType === 'Game Publisher'">
    <div class="mb-3 row">
            <h1 class="text-center text-secondary">Hello Please Enter Details of the New Game</h1>
        </div>
        <form @submit.prevent="submitForm" id="myform">
            <div class="container-fluid row mx-auto col-12 col-md-10 col-lg-8" id="App">
                <div class="container-fluid mb-3 row">
                    <div class="col-sm-1"></div>
                    <div class="col-sm-2">
                        <button type="button" class="btn btn-outline" data-bs-toggle="modal"
                            data-bs-target="#fileUpoadModal">
                            <img src="../components/logos/initialUpload.png" alt="" class="image-preview" v-if="
                                this.uploading === false || this.cancelFileUpload === true
                            " />
                            <img v-bind:src="this.imagePreview" alt="" class="image-preview" v-else
                                style="background-color: transparent" />
                        </button>
                    </div>
                    <div class="col-sm-4">
                        <div class="row pt-4 mt-4 mb-4">
                            <div class="col-sm-12">
                                <input type="text" class="form-control border-secondary bg-dark text-secondary"
                                    id="firstName" placeholder="Game Label" v-model="gameLabel" required/>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12">
                                <input type="text" class="form-control border-secondary bg-dark text-secondary"
                                    id="lastName" placeholder="Game Name" v-model="gameName" required />
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-4">
                        <div class="row pt-4 mt-4 mb-2">
                            <div class="col-sm-12">
                                <textarea class="form-control border-secondary bg-dark text-secondary" rows="4"
                                    placeholder="Game Description" v-model="gameDescription"
                                    style="height: 100px;" required></textarea>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="mb-3 mt-4 pt-4 row">
                    <div class="col-sm-1"></div>
                    <label for="staticEmail" class="col-sm-1 col-form-label border-dark text-secondary">Game Price</label>
                    <div class="col-sm-3">
                      
                        <input type="number" class="form-control border-secondary bg-dark text-secondary" id="username"
                            placeholder="Price after discount in USD" v-model="gamePrice" required step="0.01"/>
                    </div>

                    <label for="staticEmail" class="col-sm-1 col-form-label border-dark text-secondary">Game Discount</label>
                    <div class="col-sm-2">
                      
                        <input type="number" class="form-control border-secondary bg-dark text-secondary" id="username"
                            placeholder="Discount percentage" v-model="gameDiscount" required min="0" max="20" step="0.1"/>
                    </div>

                    <label for="staticEmail" class="col-sm-1 col-form-label border-dark text-secondary">Game Rating </label>
                    <div class="col-sm-2">
                      
                        <input type="number" class="form-control border-secondary bg-dark text-secondary" id="username"
                            placeholder="Out of 10" v-model="gameRate" required min="0" max="10" step="0.1"/>
                    </div>
                </div>
                <div class="mb-3 row">
                    <div class="col-sm-1"></div>
                    <label for="inputPassword" class="col-sm-2 col-form-label text-secondary">Game Publish Date</label>
                    <div class="col-sm-4 pt-2">
                        <Datepicker v-model="gamePublishDate" :enable-time-picker="false" :max-date="new Date()"
                            placeholder="Select Date" />
                    </div>
                    <label for="staticEmail" class="col-sm-1 col-form-label border-dark text-secondary">Age Restrictions</label>
                    <div class="col-sm-2">
                      
                        <input type="number" class="form-control border-secondary bg-dark text-secondary" id="username"
                            placeholder="Min Age" v-model="gameAge" required min="0" max="18" />
                    </div>
                </div>
                <div class="mb-3 row">
                    <div class="mb-3 col-sm-9"></div>
                    <div class="mb-3 col-sm-2">
                        <button class="btn btn-outline-success" type="submit" form="myform">
                            Add Game 
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
import Datepicker from '@vuepic/vue-datepicker';
import initialUpload from "../components/logos/initialUpload.png";
let userName1
let Email1
let userType1
let collectionCode
let gameCode
let found = false
export default {
  components: {Datepicker},
  name: "addCollections",
  async mounted() {
      await  this.createCollections()
      console.log("CC " ,collectionCode,this.pubCode,this.userid)
      console.log("Collection Exists ",found)
  },
  methods: {
    async createCollections() {
      await this.fetchUserInfo()
      console.log(userName1)
      console.log(Email1)
      console.log(userType1)
            const formData = {
              username: this.username,
              email: this.email,
              publisher: this.pubCode,
            }
            axios.defaults.headers.common["Authorization"] = "";
                await axios
                    .get("/api/v1/game-collections/")
                    .then((response) => {
                      console.log(response,this.pubCode)
                      for( var i=0;i<response.data.length;i++)
                      {
                        // console.log(response.data[i]['publisher'], this.pubCode)
                        if(this.pubCode===response.data[i]['publisher'])
                        {
                          found = true
                          this.collectionCode = response.data[i]['collectionCode']
                          collectionCode = this.collectionCode
                          break
                        }
                          
                      }
                        
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            console.log(found)
            if(userType1 ==='Game Publisher' && found === false)
            {
                console.log("INSEDE USerTu")
                let form_data1 = new FormData()
                form_data1.append('collectionName',formData.username+" Collection")
                form_data1.append('user',formData.username)
                form_data1.append('publisher',formData.email)
                console.log(form_data1)

                axios.defaults.headers.common["Authorization"] = "";
                axios
                    .post("/api/v1/game-collections/create/", form_data1)
                    .then((response) => {
                        console.log(response);
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            }
        },
        onDone() {
            this.uploading = true;
            this.fileName = this.profilePic["name"];
        },
        onCancel() {
            this.uploading = false;
            this.profilePic = initialUpload;
            this.imagePreview = "../components/logos/initialUpload.png";
        },
        openUpload() {
            document.getElementById("file-field").click();
        },
        fileUpload(e) {
            this.profilePic = e.target.files[0];
            var reader,
                files = e.target.files;
            reader = new FileReader();
            reader.onload = (e) => {
                this.imagePreview = e.target.result;
            };
            reader.readAsDataURL(files[0]);
            console.log(this.profilePic);
            this.uploading = true;
        },
        preview() {
            console.log(this.profilePic);
            var reader = new FileReader();
            reader.readAsDataURL(this.profilePic);
        },
        async submitForm() {
            const formData = {             
              publisher : this.pubCode,
              collection : this.collectionCode,
              gameName : this.gameName,
              gameRate : this.gameRate,
              gamePrice : this.gamePrice,
              gameDiscount : this.gameDiscount,
              gameLabel : this.gameLabel,
              gamePublishDate : this.gamePublishDate,
              gameDescription : this.gameDescription,
              gameAge : this.gameAge,
              gameicon : this.profilePic

            };
            if(this.userType ==='Game Publisher')
            {
            console.log("Adding Game to collection",this.collectionCode);          
            let form_data = new FormData()
            form_data.append('publisher',formData.publisher)
            form_data.append('collection',formData.collection)
            form_data.append('gameName',formData.gameName)
            form_data.append('gameRate',formData.gameRate)
            form_data.append('gamePrice',formData.gamePrice)
            form_data.append('gameDiscount',formData.gameDiscount)
            form_data.append('gameLabel',formData.gameLabel)
            form_data.append('gamePublishDate',formData.gamePublishDate.toISOString().split('T')[0])
            form_data.append('gameDescription',formData.gameDescription)
            form_data.append('gameAge',formData.gameAge)
            form_data.append('gameicon',formData.gameicon)
            console.log(form_data)
            console.log(formData)
            axios.defaults.headers.common["Authorization"] = "";
            await axios
                .post("/api/v1/game/create/", form_data)

                .then((response) => {
                    // this.$router.push("/login");
                    gameCode = response.data['gameCode']
                    console.log(response.data['gameCode']);
                })
                .catch((error) => {
                    console.log(error);
                });
                
            axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('token');
            let form_data1 = new FormData()
            form_data1.append('game',gameCode)
            await axios
                .put("/api/v1/game-collections/"+collectionCode+"/add/ ", form_data1)

                .then((response) => {
                    this.$router.push("/");
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
                axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem('token');
            let form_data2 = new FormData()
            console.log("Creating Community ",this.pubCode,gameCode )
            form_data2.append('game',gameCode)
            form_data2.append('gamePublisher',this.pubCode)
            await axios
                .post("/api/v1/community/create/", form_data2)

                .then((response) => {
                    this.$router.push("/");
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
            }
        },
    async fetchUserInfo() {
      if (this.$store.state.isAuthenticated) {
        console.log("Fetching data  ")
        await axios.get('/api/v1/users/me')

          .then(response => {
            console.log(response.data)
            this.userid = response.data['id']
            this.username = response.data['username']
            userName1 = this.username
            this.email = response.data['email']
            Email1 = this.email
            if (null === this.profilePic) {
              console.log("No DP")
              this.profilePic = "../components/logos/initialUpload.png"
            }
            this.userType = response.data['userType']
            userType1 = this.userType
            if (response.data['userType'] === 'Game Publisher') {
              axios
                .get('api/v1/publishers/')
                .then(response => {
                  
                  for (var i = 0; i < response.data.length; i++) {
                    if (this.email === response.data[i]['pubEmail']) {
                      localStorage.setItem('userType','Game Publisher')
                      localStorage.setItem('loggedPubliserInfo',JSON.stringify(response.data[i]))
                      this.pubCode = response.data[i]['publisherCode']
                      break
                    }
                  }
                  console.log(this.pubCode)
                  axios.get('api/v1/publishers/' + String(this.pubCode))
                    .then(response => {
                      console.log(response.data)
                      this.pubDesc = response.data['publisherDescription']
                      this.pubDescOg = this.pubDesc
                    })
                    .catch(error => {
                      console.log(error)
                    })
                })
                .catch(error => {
                  console.log(error)
                })
            }
            console.log(this.username)
          })
          .catch(error => {
            console.log(error)
          })


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
      email: '',
      userType: '',
      pubCode: 0,
      collectionCode : 0,
      userid: 0,
      gameName : '',
      gameRate: null,
      gamePrice: null,
      gameDiscount: null,
      gameAge: null,
      gameLabel : '',
      gamePublishDate: null,
      gameDescription :  '',       
      profilePic: initialUpload,


      uploadedPic: '',
      userInfo: '',
      userInfoOg: '',

      location: '',
      uploading: false,
      imagePreview: null,
      fileName: "",
      cancelFileUpload: false,
      updateInfoFlag: false,
      
      pubDesc: '',
      pubDescOg: '',
      
      
    };
  }
}
</script>
  
<style lang = "scss">
@import '../styles/theme.scss';
@import '../styles/styles.css';
</style>
  