<template>
  <div>
    <Header/>
    <div class="content">
      <ListOfTrips/>
    </div>
    <Footer/>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '../components/Header'
import ListOfTrips from '../components/ListOfTrips'
import Footer from '../components/Footer'

export default {
  name: 'Trips',
  components: {
    ListOfTrips,
    Footer,
    Header
  }
}
</script>

<style scoped>

</style>
