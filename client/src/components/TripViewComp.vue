<template>
<div class="container">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/all.css" integrity="sha384-vp86vTRFVJgpjF9jiIGPEEqYqlDwgyBgEF109VFjmqGmIY/Y4HV4d3Gp2irVfcrp" crossorigin="anonymous" />
    <div class="inner-container">
        <div class="trip-container">
            <div class="dash"></div>
            <h2>Trip "{{ trip.title }}"</h2>
            <div class="inner-trip-container">
                <div class="trip-data">
                    <p>Description:</p>
                    <p>{{ trip.description }}</p>
                    <p>
                        <i class="fas fa-euro-sign"></i> Price:
                        <span class="red">{{ trip.trip_overall_price }}</span>
                    </p>
                    <p class="departure">
                        Created: <br />{{ trip.date_published }}
                        <span>{{ trip.time_published }}</span>
                    </p>
                    <p class="departure">
                        Last Update: <br />{{ trip.date_updated }}
                        <span>{{ trip.time_updated }}</span>
                    </p>
                </div>
                <div class="trip-btns">
                    <button v-on:click="$router.push({ path: `/update/trip/${trip_id}` })">
                        Update Trip
                    </button>
                    <button v-on:click="deleteTrip(trip)">Delete Trip</button>
                    <button v-on:click="
                $router.push({ path: `/trip/${trip_id}/create/country/` })
              ">
                        Add Country
                    </button>
                </div>
            </div>
            <div class="dash"></div>
            <div class="inner-trip-container">
                <div class="countries-container">
                    <div v-for="country in trip.countries" :key="country.id" class="inner-countries-container">
                        <div class="country-data">
                            <h3>Country "{{ country.title }}"</h3>
                            <p>
                                Population: <span>{{ country.population }}</span>
                            </p>
                            <p>
                                Religion: <span>{{ country.religion }}</span>
                            </p>
                            <p>
                                Currency: <span>{{ country.currency }}</span>
                            </p>
                            <p>
                                Time Zone: <span>{{ country.time_zone }}</span>
                            </p>
                        </div>
                        <div class="country-btns">
                            <button v-on:click="
                    $router.push({
                      path: `/trip/${trip_id}/update/country/${country.id}`,
                    })
                  ">
                                Update Country
                            </button>
                            <button v-on:click="deleteCountry(country)">
                                Delete Country
                            </button>
                            <button v-on:click="
                    $router.push({
                      path: `/trip/${trip_id}/country/${country.id}/create/city`,
                    })
                  ">
                                Add City
                            </button>
                        </div>

                        <div v-if="country.cities.length != 0" class="cities-container">
                            <div v-for="city in country.cities" :key="city.id" class="inner-cities-container">
                                <div class="city-data">
                                    <h3>City "{{ city.title }}"</h3>
                                    <p>Population: {{city.population}}</p>
                                </div>
                                <div class="city-btns">
                                    <button v-on:click="
                        $router.push({
                          path: `/trip/${trip_id}/country/${country.id}/update/city/${city.id}`,
                        })
                      ">
                                        Update City
                                    </button>
                                    <button v-on:click="deleteCity(city)">Delete City</button>
                                    <button v-on:click="
                        $router.push({
                          path: `/trip/${trip_id}/country/${country.id}/city/${city.id}/create/pointofinterest/`,
                        })
                      ">
                                        Add Point Of Interest
                                    </button>
                                </div>

                                <div class="points-container">
                                    <div v-for="point in city.pointsOfInterest" :key="point.id" class="inner-points-container">
                                        <div class="point-data">
                                            <h3>{{ point.title }}</h3>
                                            <p>Price: {{ point.price }}</p>
                                            <p>Work hours:{{ point.work_hours }}</p>
                                        </div>
                                        <div class="point-btns">
                                            <button v-on:click="
                            $router.push({
                              path: `/trip/${trip_id}/country/${country.id}/city/${city.id}/update/pointofinterest/${point.id}`,
                            })
                          ">
                                                Update Point Of Interest
                                            </button>
                                            <button v-on:click="deletePoint(point)">
                                                Delete Point Of Interest
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="dash"></div>
        </div>
    </div>
</div>
</template>

<script>
//import axios from 'axios'
import {
    getAPI
} from "../axios-api";

export default {
    name: "TripViewComp",
    data() {
        return {
            trip: {},
            trip_id: this.$route.params.id,
        };
    },
    components: {},
    created() {
        getAPI
            .get(`trips/${this.trip_id}`, {
                headers: {
                    'Authorization': `Bearer ${this.$store.state.accessToken}`
                }
            })
            .then((response) => {
                (this.trip = response.data)
            })
            .catch((err) => {
                console.log(err);
            });
    },
    methods: {
        moveToTrips: function () {
            if (this.trip == {}) {
                this.$router.push({
                    name: `Trips`
                })
            } else {
                this.$router.push({
                    name: `TripView`,
                    path: `/TripView/${this.trip.id}`
                })
            }
        },
        getTripData: function () {
            getAPI
                .get(`trips/${this.trip_id}`, {
                    headers: {
                        'Authorization': `Bearer ${this.$store.state.accessToken}`
                    }
                })
                .then((response) => {
                        this.trip = response.data
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        deleteTrip: function (trip) {
            if (confirm("Delete " + trip.title)) {
                getAPI
                    .delete(`/trips/${this.trip.id}`, {
                        headers: {
                            'Authorization': `Bearer ${this.$store.state.accessToken}`
                        }
                    })
                    .then(() =>
                        this.getTripData(),
                        this.$router.push({path: `/trips/`})
                    )
            }
        },
        deleteCountry: function (country) {
            if (confirm("Delete " + country.title)) {
                getAPI.delete(`/countries/${country.id}`, {
                        headers: {
                            'Authorization': `Bearer ${this.$store.state.accessToken}`
                        }
                    })
                    .then(() =>
                        this.getTripData()
                    );
            }
        },
        deleteCity: function (city) {
            if (confirm("Delete " + city.title)) {
                getAPI.delete(`/cities/${city.id}`, {
                        headers: {
                            'Authorization': `Bearer ${this.$store.state.accessToken}`
                        }
                    })
                    .then(() =>
                        this.getTripData()
                    );
            }
        },
        deletePoint: function (point) {
            if (confirm("Delete " + point.title)) {
                getAPI.delete(`/pointsOfInterest/${point.id}`, {
                        headers: {
                            'Authorization': `Bearer ${this.$store.state.accessToken}`
                        }
                    })
                    .then(() =>
                        this.getTripData()
                    );
            }
        },
    },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Lato:wght@300;400&family=Poppins:wght@200;400&display=swap");
/*
        font-family: 'Lato', sans-serif;
        font-family: 'Poppins', sans-serif;
        */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

.dash {
    background: rgba(106, 77, 35, 0.4);
    height: 10px;
    width: 100%;
    border: 2px solid black;
    border-radius: 12px;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 90vh;
}

.inner-container {
    width: 80%;
}

.inner-container a {
    cursor: pointer;
}

.trip-container {
    background: rgba(209, 155, 73, 0.4);
    padding: 20px;
}

.inner-trip-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
}

.trip-data {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    background: cadetblue;
    padding: 10px;
    margin-bottom: 20px;
}

.trip-btns {
    display: flex;
    flex-direction: column;
    margin: 20px;
    padding: 20px;
}

.trip-btns button {
    margin: 10px;
    width: 150px;
}

.country-data {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    background: cadetblue;
    padding: 10px;
    margin-bottom: 20px;
}

.country-btns {
    display: flex;

}

.country-btns button {
    margin: 10px;
    width: 150px;
}

.city-data {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    background: cadetblue;
    padding: 10px;
    margin-bottom: 20px;
}

.city-btns {
    display: flex;
    margin: 20px;
    padding: 20px;
}

.city-btns button {
    margin: 10px;
    width: 150px;
}

.point-data {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    background: cadetblue;
    padding: 10px;
    margin-bottom: 20px;
}

.point-btns {
    display: flex;
    margin: 20px;
    padding: 20px;
}

.point-btns button {
    margin: 10px;
    width: 150px;
}

.trip-container h2 {
    font-size: 30px;
    font-weight: 300;
    letter-spacing: 1px;
    text-align: center;
    margin-bottom: 40px;
}

.trip-container p {
    margin: 10px;
}

.inner-trip-container p {
    margin: 0px;
    margin-top: 10px;
}

.countries-container {
    margin: 60px;
}

.inner-countries-container {
    background: cadetblue;
}

.inner-cities-container {}

@media (max-width: 992px) {
    * {
        margin: 0;
        padding: 0;
    }

    .container {
        display: flex;
        flex-direction: column;
    }

    .inner-container {
        width: 100%;
    }

    .trip-container {
        width: 100%;
        margin: 0px;
        padding: 0px;
    }

    .inner-trip-container {
        display: block;
        width: 100%;
    }

    .inner-countries-container {
        display: block;
        width: 100%;
    }

    .country-data {
        display: block;
        width: 100%;

    }

    .trip-data {
        display: block;
        width: 100%;

    }

    .city-data {
        display: block;
        width: 100%;

    }

    .point-data {
        display: block;
        width: 100%;

    }

    .trip-btns {
        display: block;
    }

    .country-btns {
        display: block;
    }

    .city-btns {
        display: block;
    }

    .point-btns {
        display: block;
    }
}
</style>
