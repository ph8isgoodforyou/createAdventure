<template>
<div>
    <div v-if="trips.length < 1">
        <div class="container">
            <div class="inner-container">
                <div class="text">
                    <h1>No <span>adventures</span> planed at the moment</h1>
                    <h3>Start living your life now!</h3>
                    <a v-on:click="$router.push({ path: `/create/trip/` })">Create Trip</a>
                </div>
                <div class="video">
                    <video id="videoBG" poster="poster.JPG" autoplay muted loop>
                        <source src="../assets/videos/noTrips.mp4" type="video/mp4">
                    </video>
                </div>
            </div>
        </div>
    </div>
    <div v-if="trips.length > 0">
        <div class="createTrip">
            <button v-on:click="$router.push({ path: `/create/trip/` })">Create Trip</button>
        </div>
        <div class="trips-list-container">
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/all.css" integrity="sha384-vp86vTRFVJgpjF9jiIGPEEqYqlDwgyBgEF109VFjmqGmIY/Y4HV4d3Gp2irVfcrp" crossorigin="anonymous">
            <div class="inner-trips-list-container">
                <div v-for="trip in trips" :key="trip.id" class="trip-container">
                    <div class="inner-trip-container">
                        <div class="trip-img"></div>
                        <h5>{{ trip.title }}</h5>
                        <p>{{ trip.description }}</p>
                        <p><i class="fas fa-euro-sign"></i> Price: <span class="red">{{ trip.trip_overall_price }}</span></p>
                        <p class="departure">Created: <br>{{ trip.date_published }} <span>{{ trip.time_published }}</span></p>
                        <p class="departure">Updated: <br>{{ trip.date_updated }} <span>{{ trip.time_updated }}</span></p>
                        <input v-on:click="$router.push({ path: `/TripView/${trip.id}` })" class="readMore" type="button" value="View trip">
                        <input v-on:click="deleteTrip(trip)" class="delete_btn" type="button" value="Delete trip">
                    </div>
                </div>

            </div>
        </div>
    </div>
</div>
</template>

<script>
import {
    getAPI
} from '../axios-api'

export default {
    name: 'Trips',
    data() {
        return {
            trips: [],
        };
    },
    components: {},
    async created() {
        return new Promise((resolve, reject) => {
            getAPI.get('/trips/', {
                    headers: {
                        'Authorization': `Bearer ${this.$store.state.accessToken}`
                    }
                })
                .then(response => {
                    if (response.data == '404') {
                        this.$router.push({
                            path: `/trips/`
                        })
                    } else {
                        resolve(this.trips = response.data),
                            this.$router.push({
                                path: `/trips/`
                            })
                    }
                })
                .catch(err => {
                    reject(err)
                    console.log(err)
                })
        });
    },
    methods: {
        deleteTrip: function (trip) {
            if (confirm('Delete ' + trip.title)) {
                getAPI.delete(`/trips/${trip.id}`, {
                        headers: {
                            'Authorization': `Bearer ${this.$store.state.accessToken}`
                        }
                    })
                    .then(
                        this.created(),
                        this.$router.push({
                            path: `/`
                        }),
                        this.$router.push({
                            path: `/trips/`
                        }),
                    );
            }
        },
        getTripData: function () {
            getAPI
                .get(`/trips/`, {
                    headers: {
                        'Authorization': `Bearer ${this.$store.state.accessToken}`
                    }
                })
                .then((response) => {
                    this.trips = response.data
                })
                .catch((err) => {
                    console.log(err);
                });
        },
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400&family=Poppins:wght@200;400&display=swap');
/*
font-family: 'Lato', sans-serif;
font-family: 'Poppins', sans-serif;
*/

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;

}

/*----------------------------------------------------------No trips section start*/
.container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Poppins', sans-serif;
}

.inner-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 30px;
    justify-content: center;
    align-items: center;
    width: 80%;
}

.container .inner-container .text {
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.container .inner-container .text h1 {
    font-size: 5vh;
    font-weight: 400;
    padding: 10px;
    margin-bottom: 20px;
    text-transform: uppercase;
}

.container .inner-container .text h1 span {
    color: rgb(41, 105, 187);
}

.container .inner-container .text h3 {
    font-size: 3vh;
    font-weight: 100;
}

.container .inner-container .video {
    padding: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container .inner-container .video video {
    background-size: cover;
    height: 600px;
    width: 400px;
    object-fit: cover;
}

.container .inner-container .text a {
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    text-align: center;
    background: rgb(41, 105, 187);
    color: white;
    border: 3px solid;
    border-radius: 12px;
    margin-top: 20px;
    height: 50px;
    width: 200px;
}

.container .inner-container .text a:hover {
    background-color: rgb(146, 114, 9);
}

@media (max-width: 1024px) {
    .inner-container {
        display: block;
    }
}

@media (max-width: 280px) {
    .container .inner-container .video {
        padding: 0px;
        padding-bottom: 10px;
    }

    .container .inner-container .video video {
        width: 100%;

    }
}

/*----------------------------------------------------------------No trips section end*/

/*----------------------------------------------------------------If there is some trips section start*/
.createTrip {
    display: grid;
    justify-content: center;
    align-self: center;
}

.createTrip button {
    margin-top: 40px;
    margin-bottom: 5px;
    background: #a0801f;
    color: black;
    border: solid 4px;
    width: 200px;
    height: 60px;
    display: flex;
    justify-self: center;
    justify-content: center;
    align-items: center;
}

.createTrip button:hover {
    color: white;
    background: #a0801f;
}

.trips-list-container {
    font-family: "montserrat", sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.inner-trips-list-container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    justify-content: center;
    align-items: center;
    width: 70%;
    grid-gap: 30px;
}

.trip-container {
    width: 300px;

}

.inner-trip-container {
    background: white;
    width: 100%;
}

.inner-trip-container h5 {
    margin-top: 10px;
    margin-left: 20px;
    margin-right: 20px;
}

.inner-trip-container p {
    color: rgb(41, 35, 9);
    font-size: 12px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
}

.inner-trip-container input {
    color: rgb(90, 81, 42);
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
}

.inner-trip-container p i {
    color: rgb(104, 75, 32);
    margin-right: 4px;
}

.inner-trip-container .red {
    color:  #554410;
}

.inner-trip-container .departure {
    background: #bdb291;
    color: white;
    font-size: 12px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 20px;
    margin-bottom: 10px;
    text-align: center;
}

.inner-trip-container .readMore,
.inner-trip-container .delete_btn {
    background: #a0801f;
    color: white;
    margin-left: 20px;
    margin-right: 20px;
    margin-bottom: 0px;
    border: none;
    width: 87%;
    height: 30px;
}

.inner-trip-container .delete_btn {
    margin-bottom: 20px;
}

.inner-trip-container .readMore:hover{
    background: #6a520d;
    color: white;
}
.inner-trip-container .delete_btn:hover{
    background: #8f2525;
    color: white;
}

.trip-img {
    background: url("../assets/img/backpack.jpg") no-repeat center;
    background-size: cover;
    height: 300px;
}

.paging {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 100px;
    margin-bottom: 60px;
}

.paging a {
    color: black;
    float: left;
    padding: 8px 16px;
    text-decoration: none;
}

.paging a.active {
    background-color: rgb(189, 41, 41);
    color: white;
    border-radius: 5px;
}

.paging a:hover:not(.active) {
    background-color: black;
    color: white;
    border-radius: 5px;
}

@media(max-width: 1100px) {
    .inner-trips-list-container {
        grid-template-columns: 1fr 1fr;
    }
}

@media(max-width: 992px) {}

@media(max-width: 650px) {
    .inner-trips-list-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 10px;
        width: 90%;
    }
}

@media(max-width: 280px) {
    .trip-list-container {
        width: 100%;
    }

    .inner-trip-container p {
        margin-right: 15px;
    }

    .paging a {
        color: black;
        float: left;
        padding: 6px 10px;
        text-decoration: none;
    }
}

/*----------------------------------------------------------------If there is some trips section end*/
</style>
