<template>
  <div>
    <div class="container text-dark">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">Please sign in</h1>

          <p v-if="incorrectAuth">Incorrect username or password entered - please try again</p>
          <form v-on:submit.prevent="login">
            <div class="form-group">
              <input type="text" name="email" id="user" v-model="email" class="form-control"
                     placeholder="email">
            </div>
            <div class="form-group">
              <input type="password" name="password" id="pass" v-model="password" class="form-control"
                     placeholder="Password">
            </div>
            <button type="submit" class="btn btn-lg btn-primary btn-block">Login</button>
          </form>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import Header from '../components/Header'
// import Footer from '../components/Footer'

export default {
  name: 'Login',
  components: {
    // Footer,
    // Header
  },
  data () {
    return {
      email: '',
      password: '',
      role: '',
      incorrectAuth: false
    }
  },
  methods: {
    login () {
      this.$store.dispatch('userLogin', {
        email: this.email,
        password: this.password
      })
        .then(() => {
          this.$router.push({ name: 'trips' })
        })
        .catch(err => {
          console.log(err)
          this.incorrectAuth = true
        })
    }
  }
}
</script>

<style scoped>
p {
  color: black;
}

.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 90vh;
  font-family: 'Courier New', Courier, monospace;
}

.main {
  width: 350px;
  height: 500px;
  background: black;
  overflow: hidden;
  /*background: url('./img/about-img.jpg');*/
  border-bottom: 10px;
  box-shadow: 5px 20px 50px black;
  z-index: 3;
}

#chk {
  display: none;
}

.register {
  position: relative;
  width: 100%;
  height: 65%;
}

label {
  color: white;
  font-size: 2.3em;
  justify-content: center;
  display: flex;
  margin: 60px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.5s ease-in-out;
}

input {
  width: 60%;
  height: 30px;
  background: white;
  justify-content: center;
  display: flex;
  margin: 20px auto;
  padding: 10px;
  border: none;
  outline: none;
  border-radius: 5px;
}

button {
  width: 60%;
  height: 40px;
  margin: 10px auto;
  justify-content: center;
  display: block;
  color: white;
  background: blue;
  font-size: 1em;
  font-weight: bold;
  margin-top: 20px;
  outline: none;
  border: none;
  border-radius: 5px;
  transition: 0.2s ease-in;
  cursor: pointer;
}

button:hover {
  background: rgb(11, 72, 92);
}

.login {
  height: 460px;
  border-radius: 60%/10%;
  transition: 0.8s ease-in-out;
}

.login label {
  color: lightblue;
  transform: scale(0.6);
}

#chk:checked ~ .login {
  transform: translateY(-325px);
}

#chk:checked ~ .login label {
  transform: scale(1);
}

#chk:checked ~ .register label {
  transform: scale(0.6);
}
</style>
