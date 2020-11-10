<template>
  <footer>
    <div class="inner-footer">
      <a href="/">
        <div class="footer-logo">
        <h1><span>C</span>A</h1>
        <p>Create Adventure</p>
      </div>
      </a>
      <div class="footer_third">
        <h1>Have questions?</h1>
        <h3>Contact Us</h3>
        <h5><i class=""></i>+3705864234</h5>
        <h5><i class=""></i>info@createAdventure.com</h5>
      </div>
      <div class="footer_third">
        <h1>Follow Us</h1>
        <li><a href=""><i class="fab fa-facebook"></i></a></li>
        <li><a href=""><i class="fab fa-instagram"></i></a></li>
        <li><a href="#"><i class="fab fa-twitter"></i></a></li>
        <li><a href="#"><i class="fab fa-youtube"></i></a></li>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style scoped>
/*--------------------------------------Footer start-----------*/
footer{
    width: 100%;
    display: block;
    overflow: hidden;
    padding: 70px 0px;
    box-sizing: border-box;
    background-color: black;
    color: white;
    font-family: 'Maven Pro', sans-serif;
}
.inner-footer{
    display: block;
    margin: 0 auto;
    width: 90%;
    height: 100%;
}
.footer-logo{
    width: 35%;
    float: left;
    height: 100%;
    display: block;
}
.footer-logo img{
    /*
    width: 65px;
    height: auto;
    */
}
.footer-logo h1{
    color: rgb(133, 132, 145);
    padding-bottom: 20px;
    font-weight: 200;
}
.footer-logo h1 span{
    color: rgb(219, 219, 219);
    font-weight: 400;
}
.footer-logo p{
    color: white;
    padding-bottom: 20px;
}
.inner-footer .footer_third{
    width: calc(21.6666666667% - 20px);
    margin-right: 50px;
    float: left;
    height: 100%;
}
.inner-footer .footer_third:last-child{
    margin-right: 0px;
}
.inner-footer .footer_third h1{
    font-size: 22px;
    display: block;
    width: 100%;
    margin-bottom: 20px;
    color: rgb(133, 132, 145);
}
.inner-footer .footer_third h3{
    font-size: 18px;
    display: block;
    width: 100%;
    margin-bottom: 20px;
    color:  rgb(219, 219, 219);
}
.inner-footer .footer_third h5{
    font-size: 16px;
    display: block;
    width: 100%;
    margin-bottom: 20px;
}
.inner-footer .footer_third a{
    font-size: 18px;
    font-weight: 200;
    display: block;
    width: 100%;
    margin-bottom: 5px;
}
.inner-footer .footer_third li{
    display: inline-block;
    padding:  0 5px;
    font-size: 20px;
}
.inner-footer .footer_third li a i{
    color: white;
}
.inner-footer .footer_third li a i:hover{
    color: turquoise;
}
@media(max-width: 992px){
    footer .inner-footer{
        width: 90%;
    }
    .inner-footer .footer-logo,
    .inner-footer .footer_third{
        width: 100%;
        margin-bottom: 30px;
    }
}
/*--------------------------------------Footer end-------------*/
</style>
