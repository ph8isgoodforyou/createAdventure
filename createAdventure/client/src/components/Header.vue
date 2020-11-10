<template>
  <header>
    <div class="inner-header">
      <a href="/">
        <div class="header-logo">
        <h1><span>C</span>A</h1>
      </div>
      </a>
      <ul class="nav-links" id="NavLinks">
        <a href="/#About">
          <li>About</li>
        </a>
        <a href="/#Contact">
          <li>Contacts</li>
        </a>
        <a class="login" href="/login">
          <li>Log In</li>
        </a>
        <a href="javascript:void(0);" class="icon" v-on:click="openNav()">
          <li>&#9776;</li>
        </a>
      </ul>
      <div id="hamburger" class="sliding-nav">
        <a href="javascript:void(0)" class="closebtn" v-on:click="closeNav()">&times;</a>
        <div class="nav-link" >
          <a href="/#About">About</a>
          <a href="/#Contact">Contacts</a>
          <a href="/login">Log In</a>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    openNav () {
      document.getElementById('hamburger').style.width = '100%'
    },
    closeNav () {
      document.getElementById('hamburger').style.width = '0'
    }
  }
}

</script>

<style scoped>
/*--------------------------------------Header start-------------*/
header {
  background-color: black;
  height: 10vh;
  width: 100%;
  display: block;
}

.inner-header {
  width: 90%;
  height: 100%;
  display: block;
  margin: 0 auto;
}

.header-logo {
  height: 100%;
  display: table;
  float: left;
}

.header-logo h1 {
  font-family: 'Maven Pro', sans-serif;
  color: rgb(133, 132, 145);
  height: 100%;
  display: table-cell;
  vertical-align: middle;
  font-weight: 200;
}

.header-logo h1 span {
  color: rgb(219, 219, 219);
  font-weight: 400;
}

.nav-links {
  float: right;
  height: 100%;
}

.nav-links a {
  height: 100%;
  display: table;
  float: left;
  padding: 0px 40px;
}

.nav-links a li:hover {
  color: turquoise;
  font-size: 20px;
}

.nav-links a:last-child {
  padding-right: 0px;
  display: none;
}

.nav-links .login li {
  color: #a07028;
}

.nav-links li {
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  display: table-cell;
  vertical-align: middle;
  height: 100%;
  color: white;
}

.sliding-nav {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 5;
  top: 0;
  left: 0;
  background-color: #f3ab3e;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 15px;
  text-align: center;
}

.nav-link {
  padding-top: 250px;
  width: 200px;
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.sliding-nav a {
  padding: 8px 8px 8px 8px;
  text-decoration: none;
  font-size: 2rem;
  color: white;
  display: block;
  transition: 0.3s;
  font-family: "Heebo", sans-serif;
}

.nav-link a:hover {
  color: #f3ab3e;
  background: #DFE0DF;
  margin: 20px 0px 20px 0px;
  border-radius: 12px;
}

.sliding-nav .closebtn {
  cursor: pointer;
  padding: 10px;
  margin: -10px;
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
}

@media screen and (max-width: 600px) {
  .nav-links a {
    display: none;
  }

  .nav-links a.icon {
    height: 100%;
    display: table;
    float: left;
    padding: 0px 40px;
  }
}

/*--------------------------------------Header end-------------*/
</style>
