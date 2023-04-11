<template>
    <div class="col-sm-12">
        <div class="mb-3 row">
            <h1 class="text-center text-secondary">Hello Please Enter Details</h1>
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
                    <!-- <div class="col-sm-1"></div> -->
                    <div class="col-sm-4">
                        <div class="row pt-4 mt-4 mb-4">
                            <div class="col-sm-12">
                                <input type="text" class="form-control border-secondary bg-dark text-secondary"
                                    id="firstName" placeholder="First Name" v-model="firstName" />
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-sm-12">
                                <input type="text" class="form-control border-secondary bg-dark text-secondary"
                                    id="lastName" placeholder="Last Name" v-model="lastName" />
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-4">
                        <div class="row pt-4 mt-4 mb-4">
                            <div class="col-sm-12">
                                <textarea class="form-control border-secondary bg-dark text-secondary" rows="4"
                                    placeholder="Short introduction about you" v-model="userInfo"
                                    style="height: 100px;"></textarea>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="mb-3 row">
                    <div class="col-sm-1"></div>
                    <label for="staticEmail" class="col-sm-1 col-form-label border-dark text-secondary">Username</label>
                    <div class="col-sm-9">
                        <input type="text" class="form-control border-secondary bg-dark text-secondary" id="username"
                            placeholder="This will be visible to all players" v-model="username" />
                    </div>
                </div>
                <div class="mb-3 row">
                    <div class="col-sm-1"></div>
                    <label for="staticEmail" class="col-sm-1 col-form-label text-secondary">Email</label>
                    <div class="col-sm-9">
                        <input type="email" class="form-control border-secondary bg-dark text-secondary" id="email"
                            placeholder="name@example.com" v-model="email" />
                    </div>
                </div>
                <div class="mb-3 row">
                    <div class="col-sm-1"></div>
                    <label for="inputPassword" class="col-sm-1 col-form-label text-secondary">Password</label>
                    <div class="col-sm-4 pt-2">
                        <input type="password" class="form-control border-secondary bg-dark text-secondary" id="password"
                            v-model="password" />
                    </div>
                    <label for="inputPassword" class="col-sm-1 col-form-label text-secondary">Confirm Password</label>
                    <div class="col-sm-4 pt-2">
                        <input type="password" class="form-control border-secondary bg-dark text-secondary" id="password2"
                            v-model="passwordVerify" />
                    </div>
                </div>
                <div class="mb-3 row">
                    <div class="col-sm-1"></div>
                    <label for="inputPassword" class="col-sm-1 col-form-label text-secondary">Birthday</label>
                    <div class="col-sm-4 pt-2">
                        <Datepicker v-model="dateOfBirth" :enable-time-picker="false" :max-date="new Date()"
                            placeholder="Select Date" />
                    </div>
                    <div class="col-sm-1 col-form-label text-secondary">
                        You are a
                    </div>
                    <div class="btn-group col-sm-4" role="group" aria-label="Basic radio toggle button group">
                        <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked value="Game Player" v-model="this.userType">
                        <label class="btn btn-outline-primary col-sm-2 mt-2" for="btnradio1">Game Player</label>

                        <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off" value="Game Publisher" v-model="this.userType">
                        <label class="btn btn-outline-secondary col-sm-2 mt-2" for="btnradio2">Game Publisher</label>
                    </div>
                </div>
                <div class="mb-3 row">
                    <div class="mb-3 col-sm-9"></div>
                    <div class="mb-3 col-sm-2">
                        <button class="btn btn-outline-success" type="submit" form="myform">
                            Register Now!
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
                    <h5 class="col-sm-10 modal-title text-center text-primary" id="exampleModalLabel"
                        style="margin-left: 5%;">
                        Image Upload
                    </h5>
                    <button type="button" class="btn btn-outline-danger col-sm-1" data-bs-dismiss="modal" aria-label="Close"
                        style="margin-right: 10 %;">X</button>
                </div>
                <div class="modal-body" style="align-content: center; border-color: #a39f60;">
                    <div class="mb-3 row">
                        <div class="col-sm-4 text-primary">Click on image to upload</div>
                        <div class="col-sm-4">
                            <img src="../components/logos/initialUpload.png" alt=""
                                class="btn btn-outline-secondary image-preview" v-on:click="openUpload" v-if="
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
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import axios from "axios";
import initialUpload from "../components/logos/initialUpload.png";
export default {
    name: "RegisterPage",
    data() {
        return {
            username: "",
            email: "",
            password: "",
            firstName: "",
            lastName: "",
            profilePic: initialUpload,
            userInfo: "",
            dateOfBirth: new Date(),
            userType: "Game Player",
            location: "",
            uploading: false,
            imagePreview: null,
            fileName: "",
            cancelFileUpload: false,
        };
    },
    methods: {
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
        submitForm() {
            console.log(this.profilePic);
            const formData = {
                username: this.username,
                password: this.password,
                email: this.email,
                firstName: this.firstName,
                lastName: this.lastName,
                profilePic: this.profilePic,
                userInfo: this.userInfo,
                dateOfBirth: this.dateOfBirth,
                userType: this.userType,
                location: "",
            };
            let form_data = new FormData()
            console.log(formData.dateOfBirth.toISOString().split('T')[0])
            form_data.append('username',formData.username)
            form_data.append('password',formData.password)
            form_data.append('email',formData.email)
            form_data.append('firstName',formData.firstName)
            form_data.append('lastName',formData.lastName)
            form_data.append('profilePic',formData.profilePic)
            form_data.append('userInfo',formData.userInfo)
            form_data.append('dateOfBirth',formData.dateOfBirth.toISOString().split('T')[0])
            form_data.append('userType',formData.userType)
            form_data.append('location',formData.location)

            console.log(form_data)
            console.log(formData)
            axios.defaults.headers.common["Authorization"] = "";
            axios
                .post("/api/v1/users/", form_data)

                .then((response) => {
                    this.$router.push("/login");
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    components: { Datepicker }
};
</script>

<style lang="scss">
@import "../styles/theme.scss";
@import "../styles/styles.css";


.custom-file-upload {
    // border: 1px solid #ccc;
    display: inline-block;
    padding: 0px 0px;
    align-content: end;
    height: 0;
    display: none;
    cursor: pointer;
}

.align-center {
    align-content: center;
    align-items: center;
}

.bg-blur {
    backdrop-filter: blur(10px);
    justify-content: center;
}

.image-preview {
    width: 150px;
    height: 150px;
    border: 2px solid $secondary;
    padding: 10px;
    border-radius: 50px;
    position: relative;
    background: transparent;
    // padding-top:66.59%;
}

.modal_border_color {
    border-color: $secondary;
}

.modal-footer {
    border-top: 1px solid $secondary;
}

// DatePicker Style
.dp__theme_light {
    --dp-background-color: #0e0e0e;
    --dp-text-color: #95bf9b;
    --dp-hover-color: #4e4e4e;
    --dp-hover-text-color: #a39f60;
    --dp-hover-icon-color: #959595;
    --dp-primary-color: #a39f60;
    --dp-primary-text-color: #95bf9b;
    --dp-secondary-color: #a39f60;
    --dp-border-color: #a39f60;
    --dp-menu-border-color: #95bf9b;
    --dp-border-color-hover: #95bf9b;
    --dp-disabled-color: #4e4e4e;
    --dp-scroll-bar-background: #0e0e0e;
    --dp-scroll-bar-color: #a39f60;
    --dp-success-color: #95bf9b;
    --dp-success-color-disabled: #a3d9b1;
    --dp-icon-color: #a39f60;
    --dp-danger-color: #ff6f60;
    --dp-highlight-color: rgba(25, 118, 210, 0.1);

}
</style>
