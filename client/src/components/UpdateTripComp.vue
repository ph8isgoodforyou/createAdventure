<template>
<div class="create-container">
    <div class="inner-create-container">
        <div class="create-box">
            <form @submit.prevent="updateTrip" method="post">
                <h2>Update Trip</h2>
                <div class="dash"></div>
                <input v-model="newTrip.title" id="title" name="title" type="text" placeholder="Title" onfocus="placeholder=''" onblur="placeholder='Title'" v-validate="'required'">
                <select v-model="newTrip.trip_type" id="trip_type" name="trip_type" v-validate="'required'">
                    <optgroup>
                        <option selected="selected" value="1">Holiday</option>
                        <option value="2">Holiday</option>
                        <option value="3">Holiday</option>
                        <option value="4">Holiday</option>
                    </optgroup>
                </select><br>
                <input v-model="newTrip.trip_overall_price" id="trip_overall_price" name="trip_overall_price" type="text" placeholder="Budget" onfocus="placeholder=''" onblur="placeholder='Budget'" v-validate="'required'"><br>
                <textarea v-model="newTrip.description" maxlength="200" id="description" name="description" placeholder="Description" onfocus="placeholder=''" onblur="placeholder='Description'" v-validate="'required'"></textarea><br>
                <div class="dash"></div>
                <input class="create-btn" type="submit" value="Create">
            </form>
        </div>
    </div>
</div>
</template>

<script>
//import axios from 'axios'
import {
    getAPI
} from '../axios-api'

export default {
    name: "UpdateTripComp",
    data() {
        return {
            newTrip: {
                title: '',
                trip_type: '',
                trip_overall_price: '',
                description: '',
            }
        };
    },
    components: {},
    mounted() {
        getAPI.get('/trips/' + this.$route.params.id, {
                headers: {
                    'Authorization': `Bearer ${this.$store.state.accessToken}`
                }
            })
            .then(response => {
                //console.log(response.data),
                this.newTrip = response.data
            });
    },
    methods: {
        updateTrip() {
            getAPI.put('/trips/' + this.$route.params.id + '/',
                    this.newTrip, {
                        headers: {
                            'Authorization': `Bearer ${this.$store.state.accessToken}`
                        }
                    }
                )
                .then(
                    history.back(1)
                ).catch((err) => {
                    console.log(err);
                })
        }
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
}

.create-container {
    font-family: 'Poppins', sans-serif;
    background: url('../assets/img/createTrip-img.jpg') no-repeat center;
    background-size: cover;
    color: white;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.inner-create-container {
    width: auto;
    height: 100%;
    /*max-width: 80%;
            max-height: 80%;
            margin: 50px;*/
}

.create-box {
    background-color: rgba(0, 0, 0, 0.5);
    box-shadow: 0 0 15px 6px #34495e;
    /*opacity: 0.8;*/
    height: auto;
    width: auto;
    border-radius: 50px;
}

form {
    height: 100%;
    width: 100%;
    display: inline-block;
    justify-content: center;
    align-items: center;
    padding: 30px;
}

form .dash {
    background-color: white;
    width: 100%;
    height: 5px;
    border: 2px solid rgb(98, 154, 206);
    border-radius: 12px;
    margin-top: 20px;
    margin-bottom: 20px;
}

form h2 {
    font-size: 30px;
    font-weight: 100;
    margin-bottom: 10px;
    letter-spacing: 5px;
}

form input,
form select {
    width: 250px;
    height: 30px;
    border: none;
    margin: 20px;
    padding: 20px;
    border-radius: 12px;
}

form select {
    font-family: 'Poppins', sans-serif;
    color: black;
    padding: 0px;
    padding-left: 10px;
    height: 40px;
}

form select optgroup {
    font-family: 'Poppins', sans-serif;
}

form textarea {
    overflow: hidden;
    width: 540px;
    height: 90px;
    border: none;
    margin: 20px;
    padding: 20px;
    border-radius: 12px;
    line-height: 20px;
}

form input:focus,
form textarea:focus {
    background-color: rgb(24, 55, 85);
    color: white;
}

::placeholder {
    font-family: 'Poppins', sans-serif;
    font-size: 15px;
    font-weight: 100;
    color: black;
}

form .create-btn {
    background-color: rgb(98, 154, 206);
    color: white;
    margin: 0;
    padding: 0;
    float: right;
}

form .create-btn:hover {
    background-color: rgb(24, 55, 85);
    color: white;
}

@media (max-width: 700px) {
    form {
        display: grid;
        justify-content: center;
        align-items: center;
    }

    form textarea {
        width: 100%;
        margin: 0;
    }

    form input,
    form select {
        width: 100%;
        height: 30px;
        border: none;
        margin: 0px;
        padding: 20px;
        border-radius: 12px;
        display: block;
        align-self: center;
    }

    form select {
        font-family: 'Poppins', sans-serif;
        color: black;
        padding: 0px;
        padding-left: 10px;
        height: 40px;
        margin-top: 20px;

    }

    form .create-btn {
        width: 100%;
    }
}
</style>
