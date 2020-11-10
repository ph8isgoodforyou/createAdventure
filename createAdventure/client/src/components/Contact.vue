<template>
  <div id="Contact" class="contact">
    <div class="title">
      <h1>Contact Us</h1>
    </div>
    <div class="border"></div>
    <form action="" method="POST" class="contact-form">
      <input type="text" class="contact-form-text" placeholder="Your name">
      <input type="email" class="contact-form-text" placeholder="Your email">
      <input type="text" class="contact-form-text" placeholder="Your phone">
      <textarea name="" id="" class="contact-form-text" placeholder="Enter your message here.."></textarea>
      <input type="submit" class="contact-form-btn" value="Send">
    </form>
    <div class="border"></div>
  </div>
</template>

<script>
export default {
  name: 'Contact'
}
</script>

<style scoped>
/*--------------------------------------Contact start----------*/
.content .contact{
    /*background: url() no-repeat center;*/
    background-size: cover;
    padding: 40px 0;
    height: 100%;
    font-family: "montserrat", sans-serif;
}
.contact .title h1{
    text-align: center;
    color: #8d5603;

}
.border{
    width: 80%;
    height: 10px;
    background: #8d5603;
    margin: 40px auto;
}
.contact-form{
    max-width: 600px;
    margin: auto;
    padding: 0 10px;
    overflow: hidden;
}
.contact-form-text{
    display: block;
    width: 100%;
    box-sizing: border-box;
    margin: 16px 0;
    border: 0;
    background-color: turquoise;
    padding: 20px 40px;
    outline: none;
    color: white;
    border-radius: 12px;
}
.contact-form-text:focus{
    box-shadow: 0 0 10px 4px #34495e;
}
.contact-form-text:hover{
    background-color: #f3ab3e;
}
::placeholder{
    color: black;
    opacity: 1;
    font-family: "montserrat", sans-serif;
    font-size: 15px;
}
.contact textarea{
    resize: none;
    height: 120px;
}
.contact-form-btn{
    float:right;
    border: 0;
    background: #8d5603;
    color: #fff;
    padding: 12px 50px;
    cursor: pointer;
    transition: 0.5s;
    border-radius: 12px;
}
.contact-form-btn:hover{
    background: #f3ab3e;
}

/*--------------------------------------Contact end------------*/
</style>
