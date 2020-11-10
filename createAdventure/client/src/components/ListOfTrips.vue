<template>
  <div class="trips-container">
    <div class="trips-inner-container">
      <!--        <h1>Where are you going today?</h1>-->
      <div class="trips-content">
        <h1 v-if="role === 'user'">Currently You Have {{ APIData.length }} Trips</h1>
        <h1 v-if="role === 'admin'">Currently Site Has {{ APIData.length }} Trips</h1>
        <h1>Currently Site Has {{ APIData.length }} Trips</h1>

        <input type="submit" value="Add Trip">
        <p v-if="APIData.length === 0">No Trips History</p>

        <div v-for="trip in APIData" :key="trip.id" class="inner-content">
          <div class="section1">
            <!--            <a href="">{{ trip.title }}</a>-->
            <h3>{{ trip.title }}</h3>
          </div>
          <div class="section2">
            <div class="section2-1">
              <h5>Created at:</h5>
            </div>
            <div class="section2-2">
              <p>{{ trip.date_published }}</p>
            </div>
            <div class="section2-3">
              <h5>Last Update:</h5>
            </div>
            <div class="section2-4">
              <p>{{ trip.date_updated }}</p>
            </div>
          </div>
          <div class="section3">
            <input type="button" value="View Details">
            <input type="button" value="Delete Trip">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {getAPI} from '../axios-api'
import {mapState} from 'vuex'

export default {
  name: 'ListOfTrips',
  onIdle() {
    this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({name: 'login'})
        })
  },
  components: {},
  computed: mapState(['APIData']),
  created() {
    getAPI.get('/trips/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
        .then(response => {
          this.$store.state.APIData = response.data
        })
        .catch(err => {
          console.log(err)
        })
  },
  methods: {}
}
</script>

<style scoped>
.trips-container {
  background: #170000;
  min-height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-content: center;
  font-family: 'Poppins', sans-serif;
  color: white;
}

.trips-inner-container {
  width: 100%;
  height: 95%;
  display: flex;
  justify-content: center;
}

.content-title {
  /*border: 5px solid red;*/
  background: #170000;
  padding: 20px;
}

.trips-content {
  /*border: 5px solid blue;*/
  background: #170000;
  display: grid;
  place-items: center;
  grid-template-columns: 1fr;
  padding: 20px;
  height: 100%;
  width: 90%;
  overflow: scroll;
  overflow-x: hidden;

}

.trips-content p {
  text-align: center;
  font-size: 30px;
  margin: 20px;
}

.trips-content h1 {
  text-align: center;
  margin-bottom: 30px;
  font-size: 50px;
  font-weight: 100;
  opacity: 0.5;
}

.trips-content input {
  background: #f3ab3e;
  color: white;
  height: 45px;
  width: 200px;
  margin: 10px;
  border-radius: 12px;
  font-size: 20px;
  display: block;
}

.trips-content input:hover {
  color: #170000;
  background: white;
}

.inner-content {
  /*overflow-y: scroll;*/
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  height: 200px;
  width: 100%;
  justify-content: center;
  align-content: center;
  padding-top: 30px;
}

.section1 {
  display: flex;
  justify-content: center;
  align-self: center;
  text-align: center;
}

.section1 h3 {
  margin: 20px;
  font-weight: 10;
}

.section2 {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 1fr 1.5fr;
}

.section2-1 {
  display: block;
  align-self: center;
}

.section2-1 h5 {
  font-size: 15px;
  margin: 5px;
  font-weight: 10;
}

.section2-2 {
  display: block;
  align-self: center;
  justify-self: left;
}

.section2-2 p {
  font-size: 15px;
  margin: 5px;
  font-weight: 10;
}

.section2-3 {
  display: block;
  align-self: center;
}

.section2-3 h5 {
  font-size: 15px;
  margin: 5px;
  font-weight: 10;
}

.section2-4 {
  display: block;
  align-self: center;
  justify-self: left;
}

.section2-4 p {
  font-size: 15px;
  margin: 5px;
  font-weight: 10;
}

.section3 {
  display: block;
  align-self: center;
  justify-self: center;
  height: auto;
}

.section3 input {
  background: #f3ab3e;
  color: white;
  height: 40px;
  width: 150px;
  margin: 10px;
  border-radius: 12px;
  font-size: 15px;
  display: block;
}

.section3 input:hover {
  color: #170000;
  background: white;
}

::-webkit-scrollbar {
  width: 0px; /* Remove scrollbar space */
  background: transparent;
}

@media (max-width: 500px) {
  .inner-content {
    height: auto;
  }

  .section2 {
    display: block;
    text-align: center;
  }
}

@media (max-width: 992px) {
  .inner-content {
    grid-template-columns: 1fr;
    margin-bottom: 30px;

  }

  .section2 {
    grid-template-columns: 1fr 1.3fr;
  }

  .section2-1 {
    display: block;
    align-self: center;
    justify-self: right;
  }

  .section2-3 {
    display: block;
    align-self: center;
    justify-self: right;
  }
}
</style>
