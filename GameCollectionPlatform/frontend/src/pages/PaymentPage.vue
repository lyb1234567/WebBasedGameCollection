<template>
  <!-- <div class="contaier-fluid bg_image" style="height: 100vh"> -->
  <div class="col-sm-12">
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
        <input type="text" style="width: 800px; margin-left: 10px;"/>
      </form>
      <br><br>
      <form>
        <label class="text-center text-primary">Pin Code:   </label>
        <input type="text" style="width: 100px; margin-left: 10px; margin-right: 190px;"/>
        <label class="text-center text-primary">Expiry Date:   </label>
        <input type="text" style="width: 100px; margin-left: 10px; margin-right: 283px;"/>
      </form>
      <br><br>
      <form>
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
  </div>
  <!-- </div> -->

</template>

