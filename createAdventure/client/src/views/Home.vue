<template>
  <div>
    <Header/>
  <Intro/>
  <div class="content">
    <About/>
    <Contact/>
  </div>
  <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '../components/Header'
import Intro from '../components/Intro'
import About from '../components/About'
import Contact from '../components/Contact'
import Footer from '../components/Footer'

export default {
  name: 'Home',
  components: {
    Contact,
    About,
    Intro,
    Footer,
    Header
  }
}
</script>

<style scoped>
.content{
    padding-top: 100vh;
    text-align: center;
    background: #0c0b0c;
    width: 100%;
    z-index: 2;
}
</style>
