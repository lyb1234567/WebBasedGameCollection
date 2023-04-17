<template>
  <!-- <div class="contaier-fluid bg_image" style="height: 100vh"> -->
  <!-- <div class="col-sm-12">
    <div class="mb-3 row">
      <h1 class="text-center text-primary">Choose your payment</h1>
    </div>
    <div align="center">
      <form action="">
        <input type="radio" name="pay" value="visa">
        <img src="./image/payment/Visa.png" style="width: 125px; height: 75px; margin: 30px;">
        <input type="radio" name="pay" value="mastercard">
        <img src="./image/payment/mastercard.png" style="width: 125px; height: 75px; margin: 30px;">
        <input type="radio" name="pay" value="paypal">
        <img src="./image/payment/PayPal.png" style="width: 250px; height: 75px; margin: 30px;">
        <input type="radio" name="pay" value="americanExpress">
        <img src="./image/payment/American-Express.png" style="width: 75px; height: 75px; margin: 30px;"><br>
        <input type="radio" name="pay" value="JCB">
        <img src="./image/payment/JCB.png" style="width: 100px; height: 75px; margin: 30px; margin-right: 55px;">
        <input type="radio" name="pay" value="applePay">
        <img src="./image/payment/applePay.png" style="width: 125px; height: 75px; margin: 30px;">
        <input type="radio" name="pay" value="googlePay">
        <img src="./image/payment/googlePay.png" style="width: 150px; height: 75px; margin: 30px; margin-right: 275px;">
      </form>
    </div>
    
    <div align="center">
      <form>
        <label class="text-center text-primary">Card Number:</label>
        <input class="form-control border-secondary bg-dark text-secondary col-mx-2 " type="text" style="width: 800px; margin-left: 10px;"/>
        <label class="text-center text-primary">Pin Code:   </label>
        <input type="text" style="width: 100px; margin-left: 10px; margin-right: 190px;"/>
        <label class="text-center text-primary">Expiry Date:   </label>
        <input type="text" style="width: 100px; margin-left: 10px; margin-right: 283px;"/>
        <label class="text-center text-primary" style="margin-right: 800px;">Contact Details</label>
        <br><br>
        <label class="text-center text-primary" style="margin-left: 50px;">Name: </label>
        <input type="text" style="width: 800px; margin-left: 10px;"/>
        <br><br>
        <label class="text-center text-primary" style="margin-left: 30px;">Address: </label>
        <input type="text" style="width: 800px; margin-left: 10px;"/>
      </form>
      <br><br>
      <input type="submit" value="Submit" style="width: 100px; height: 35;">
      <a href="/">
        <input type="submit" value="Cancel" style="width: 100px; height: 35; margin-left: 200px;">
      </a>
    </div>
  </div> -->
  <!-- </div> -->
  <div class="container p-0">
        <div class="card px-4 bg-dark">
            <p class="h8 py-3 text-primary">Payment Details</p>
            <div class="row gx-3">
                <div class="col-12">
                    <div class="d-flex flex-column">
                        <p class="text mb-1 text-primary">Person Name</p>
                        <input class="form-control mb-3 text-secondary border-secondary bg-transparent" type="text" placeholder="John Doe" value="" required>
                    </div>
                </div>
                <div class="col-12">
                    <div class="d-flex flex-column">
                        <p class="text mb-1 text-primary">Card Number</p>
                        <input class="form-control mb-3 text-secondary border-secondary bg-transparent" type="text" placeholder="1234 5678 435678" required maxlength="19" v-model="creditCardNumber">
                    </div>
                </div>
                <div class="col-6">
                    <div class="d-flex flex-column">
                        <p class="text mb-1 text-primary">Expiry</p>
                        <input class="form-control mb-3 text-secondary border-secondary bg-transparent" type="text" placeholder="MM/YYYY" required>
                    </div>
                </div>
                <div class="col-6">
                    <div class="d-flex flex-column">
                        <p class="text mb-1 text-primary">CVV/CVC</p>
                        <input class="form-control mb-3 pt-2 text-secondary border-secondary bg-transparent" type="password" placeholder="***" required>
                    </div>
                </div>
                <div class="col-12 row">
                    <button class="btn btn-outline-primary mb-3 ">
                        Pay ${{this.gamePrice}}
                    </button>
                </div>
                <div class="container-fluid row">
                  <div class="col-sm-4"><img src="./image/payment/Visa.png" style="width:90%; height: 75px; margin: 30px;"></div>
                  <div class="col-sm-4"><img src="./image/payment/mastercard.png" style="width: 90%; height: 75px; margin: 30px;"></div>
                  <div class="col-sm-4"><img src="./image/payment/American-Express.png" style="width: 90%; height: 75px; margin: 30px;"></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
  mounted(){
    this.gamePrice=localStorage.getItem('gamePrice')
  },
  data() {
    return {
      creditCardNumber: '',
      gamePrice: 0,
    }
  },
  watch: {
    creditCardNumber() {
      // Card number without dash (-)
        let realNumber = this.creditCardNumber.replace(/-/gi, '')
        
        // Generate dashed number
        let dashedNumber = realNumber.match(/.{1,4}/g)

        // Replace the dashed number with the real one
        this.creditCardNumber = dashedNumber.join('-')
    }
  }
};
</script>
<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Montserrat', sans-serif;
}

/* body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #0C4160;

    padding: 30px 10px;
} */

.card {
    max-width: 500px;
    margin: auto;
    color: black;
    border-radius: 20 px;
}

p {
    margin: 0px;
}

.container .h8 {
    font-size: 30px;
    font-weight: 800;
    text-align: center;
}

.btn.btn-primary {
    width: 100%;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 15px;
    background-image: linear-gradient(to right, #77A1D3 0%, #79CBCA 51%, #77A1D3 100%);
    border: none;
    transition: 0.5s;
    background-size: 200% auto;

}


.btn.btn.btn-primary:hover {
    background-position: right center;
    color: #fff;
    text-decoration: none;
}



.btn.btn-primary:hover .fas.fa-arrow-right {
    transform: translate(15px);
    transition: transform 0.2s ease-in;
}

.form-control {
    color: white;
    background-color: #223C60;
    border: 2px solid transparent;
    height: 60px;
    padding-left: 20px;
    vertical-align: middle;
}

.form-control:focus {
    color: white;
    background-color: #0C4160;
    border: 2px solid #2d4dda;
    box-shadow: none;
}

.text {
    font-size: 14px;
    font-weight: 600;
}

::placeholder {
    font-size: 14px;
    font-weight: 600;
}
</style>