<template>
  <div class="info-box">
    <div class="box-left">
      <div class="name-pic">
        <div class="pic-box">
          <img src="../assets/images/pic.png" alt="" />
        </div>
        <div class="name">Username</div>
      </div>
      <div class="box-item">Public profile</div>
      <div class="box-item">Game collections</div>
      <div class="box-item">Wish list</div>
      <div class="box-item">Favourites</div>
      <div class="box-item">Friend list</div>
      <div class="box-item">Wallet</div>
      <div class="box-item">Notifications</div>
      <div class="box-item">Settings</div>
    </div>
    <div class="box-right">
      <div class="back" @click="$router.push('/homepage')">Back to main page</div>
      <div class="form-box">
        <div class="input-item">
          <div class="item-tit">
            Name
            <div class="btn-icon"></div>
          </div>
          <input type="text" v-model="form.name" />
        </div>
        <div class="input-item">
          <div class="item-tit">
            Email
            <div class="btn-icon"></div>
          </div>
          <input type="text" v-model="form.email" />
        </div>
        <div class="input-item">
          <div class="item-tit">
            Telephone
            <div class="btn-icon"></div>
          </div>
          <input type="text" v-model="form.telephone" />
        </div>
        <div class="input-item">
          <div class="item-tit">
            Introduction
            <div class="btn-icon"></div>
          </div>
          <textarea name="" id="" cols="30" rows="10" v-model="form.introduction"></textarea>
        </div>
        <div class="input-item">
          <div class="item-tit">Game collections</div>
          <div class="txt-box" v-for="(item, index) in form.game_collections" :key="index">
            {{ item }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: 'Lorem ipsum',
        email: 'abcde@fgh.ac.uk',
        telephone: '+44 (0)123 4567 890',
        introduction: '',
        game_collections: ['Collection 1', 'Collection 2'],
      },
    };
  },
};
</script>

<style lang="scss" scoped>
.info-box {
  width: 80%;
  margin: 0 auto;
  border: 1px solid #a39f60;
  display: flex;
  justify-content: flex-start;
  // background: #fff;
  height: 700px;
  .box-left {
    width: 300px;
    text-align: center;
    border-right: 1px solid #a39f60;
    > div {
      border-bottom: 1px solid #a39f60;
      height: 40px;
      line-height: 40px;
      cursor: pointer;
      color: #a39f60;
    }
    .name-pic {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 160px;
      border-bottom: 1px solid #a39f60;
      .pic-box {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        overflow: hidden;
        margin-right: 20px;
        border: 1px solid #a39f60;
        img {
          width: 100%;
          height: 100%;
        }
      }
    }
  }
  .box-right {
    width: 100%;
    padding: 10px 20px 20px 40px;
    overflow-y: auto;
    position: relative;
    .back {
      border: 1px solid #a39f60;
      border-radius: 5px;
      text-align: center;
      height: 50px;
      position: absolute;
      right: 20px;
      top: 20px;
      line-height: 50px;
      padding: 0 10px;
      cursor: pointer;
      color: #95bf9b;
    }
    .form-box {
      margin-top: 60px;
      width: 100%;
      input {
        width: 100%;
        height: 50px;
        padding-left: 10px;
        background: transparent;
        color: #a39f60;
        outline: 0;
        border: 1px solid #a39f60;
      }
      textarea {
        width: 100%;
        height: 150px;
        padding: 10px;
        background: transparent;
        min-height: 150px;
        min-width: 100%;
        border: 1px solid #a39f60;
        outline: 0;
      }
      .input-item {
        margin-top: 20px;
        .item-tit {
          display: flex;
          justify-content: flex-start;
          align-items: center;
          margin-bottom: 15px;
          padding-left: 20px;
          color: #a39f60;
          .btn-icon {
            width: 28px;
            height: 28px;
            background: url('../assets/images/edit.png') no-repeat center/cover;
            margin-left: 5px;
          }
        }
        .txt-box {
          width: 100%;
          height: 50px;
          border: 1px solid #a39f60;
          padding-left: 20px;
          line-height: 50px;
          color: #a39f60;
        }
      }
    }
  }
}
</style>
